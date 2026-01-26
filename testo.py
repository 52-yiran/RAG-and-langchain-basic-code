from openai import OpenAI
import os
import re

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    # api_key="ollama",  # 现在很多新版 Ollama 可以不填或填任意值
)

messages = [
    {"role": "system", "content": """你是一个乐于助人的助手。
在回答前，请先在 <think>标签内完整写出你的思考过程，思考完再给出最终简短回答。
格式严格如下：

<think>
你的详细思考过程...
</think>

最终回答：xxx"""},
    {"role": "user", "content": "我家有三个人"},
    {"role": "user", "content": "我邻居家有3个人"},
    {"role": "user", "content": "一共有几个人？"}
]

completion = client.chat.completions.create(
    model="deepseek-r1:8b",  # 或者换成 qwq-32b / marco-o1 等更擅长思考链的模型
    messages=messages,
    stream=True,
    temperature=0.6,
)

is_thinking = False
is_answering = False
think_buffer = ""

print("\n" + "=" * 30 + " 思考过程 " + "=" * 30)

for chunk in completion:
    delta = chunk.choices[0].delta
    content = delta.content if delta.content else ""
    
    if content:
        think_buffer += content
        
        # 检测到 </think> 结束标记
        if "</think>" in think_buffer:
            # 提取 <think> ... </think> 之间的内容
            match = re.search(r'<think>(.*?)</think>', think_buffer, re.DOTALL)
            if match:
                thinking = match.group(1).strip()
                print(thinking)
            
            # 剩余部分认为是正式回答
            after_think = think_buffer.split("</think>", 1)[-1].strip()
            if after_think:
                if not is_answering:
                    print("\n" + "=" * 30 + " 最终回答 " + "=" * 30)
                    is_answering = True
                print(after_think, end="", flush=True)
                
            think_buffer = ""  # 清空缓冲
            is_thinking = False
        
        # 还在思考阶段，直接累积打印（更实时）
        elif "<think>" in think_buffer and not is_answering:
            print(content, end="", flush=True)

# 如果流结束还有残余思考内容
if think_buffer:
    print(think_buffer, end="", flush=True)
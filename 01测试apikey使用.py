import os
from openai import OpenAI

# 注意: 不同地域的base_url不通用（下方示例使用北京地域的 base_url）
# - 华北2（北京）: https://dashscope.aliyuncs.com/compatible-mode/v1
# - 新加坡: https://dashscope-intl.aliyuncs.com/compatible-mode/v1

#DASHSCOPE_API_KEY
#OPENAI_API_KEY

client = OpenAI(
    #api_key=os.getenv("DASHSCOPE_API_KEY"),
    #api_key="sk-ed55963088e54b8081481af63aa6603f",
    #base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    base_url="http://127.0.0.1:11434/v1",
)
#能运行的前提是ollama软件是启动的
completion = client.chat.completions.create(
    #model="qwen3.5-plus",
    model="qwen3-vl:8b",
    messages=[{'role': 'user', 'content': '你能做什么'}]
)
print(completion.choices[0].message.content)
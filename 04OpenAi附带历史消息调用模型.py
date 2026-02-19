from math import trunc

from openai import OpenAI

#1 获取client对象

client = OpenAI(
    #api_key=os.getenv("DASHSCOPE_API_KEY"),
    #api_key="sk-ed55963088e54b8081481af63aa6603f",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

)

#能运行的前提是ollama软件是启动的
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {'role': 'system', 'content': '你是ai助理，回答很简洁'},
        {'role': 'user', 'content': '小明有两条宠物狗'},
        {'role': 'assistant', 'content': '好的'},
        {'role': 'user', 'content': '小红有三条宠物猫'},
        {'role': 'assistant', 'content': '好的'},
        {'role': 'user', 'content': '总共有几只宠物？'},

    ],
    stream=True #开启流式输出的功能
)

#print(completion.choices[0].message.content)
for chunk in completion:
    print(
        chunk.choices[0].delta.content,end=" ", #每一段为空格分隔
        flush=True #立刻刷新缓冲区
    )
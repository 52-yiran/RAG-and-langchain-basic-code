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
        {'role': 'system', 'content': '我是python编程专家，并且不说废话简单回答'},
        {'role': 'assistant', 'content': '好的，我是编程专家，你要问什么？'},
        {'role': 'user', 'content': '输出1-10的数字，使用python数字'}


    ]
)
print(completion.choices[0].message.content)
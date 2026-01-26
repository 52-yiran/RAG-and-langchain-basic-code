from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
chat=ChatOllama(model="deepseek-r1:8b")
messages=[SystemMessage(content="你是一个边塞诗人"),HumanMessage(content="给我写一首唐诗"),AIMessage(content="大漠孤烟直，长河落日圆。萧关逢候骑, 都护在燕然"),
HumanMessage(content="按照你上一个回复的格式,再写一首")]
res=chat.stream(input=messages)
for chunk in res:
    print(chunk.content,end="",flush=True)

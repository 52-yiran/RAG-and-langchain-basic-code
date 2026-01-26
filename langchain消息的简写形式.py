from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
chat=ChatTongyi(model="qwen-plus-2025-12-01")
messages=[("system","你是一个边塞诗人"),("human","给我写一首唐诗"),("assistant","大漠孤烟直，长河落日圆。萧关逢候骑, 都护在燕然"),
("human","按照你上一个回复的格式,再写一首")]
res=chat.stream(input=messages)   
for chunk in res:
    print(chunk.content,end="",flush=True)
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
model=ChatTongyi(model="qwen-plus-2025-12-01")
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个考研专家"),
   MessagesPlaceholder("history"),
   ("human","按照上面的示例回答,回答数学一的重点有哪些")
   ])
history_data=[
    ("human","计算机网络的重点有哪些"),
    ("ai","计算机网络的重点有：网络体系结构、数据链路层、网络层、传输层、应用层等。"),
    ("human","数据结构的重点有哪些"),
    ("ai","数据结构的重点有：数组、链表、栈、队列、树、图等。")
   ]
chain =chat_prompt_template | model
print(type(chain))
res=chain.invoke({"history":history_data})
print(res.content)

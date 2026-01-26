from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda
stroutputparser=StrOutputParser()
prompt1 = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},只用给出名字"
)
model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt2 = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义"
)
my_func=RunnableLambda(lambda ai_msg:{"name":ai_msg.content})
chain=prompt1 | model | my_func | prompt2  | model | stroutputparser  

res=chain.stream(input={"lastname":"张","gender":"男孩"})
for chunk in res:
    print(chunk,end="",flush=True)
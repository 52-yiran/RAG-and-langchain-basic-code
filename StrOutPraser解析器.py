from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},帮忙起名字,只给名字"
)
print(type(prompt_template))
praser=StrOutputParser()  
chain=prompt_template | model | praser |model| praser
res=chain.invoke(input={"lastname":"张","gender":"男孩"})
print(res)
print(type(res))

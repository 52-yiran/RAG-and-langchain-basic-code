from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
model=ChatTongyi(model="qwen-plus-2025-12-01")
stroutputparser=StrOutputParser()
jsonoutputparser=JsonOutputParser()
model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt1 = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},帮忙起名字,给封装json格式,并且要求key是name,value是名字,请严格遵守格式要求"
)
praser=StrOutputParser()  
prompt2 = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义,一句话即可"
)
chain=prompt1 | model | jsonoutputparser | prompt2  | model | stroutputparser
res=chain.invoke(input={"lastname":"张","gender":"男孩"})
print(res)
print(type(res))
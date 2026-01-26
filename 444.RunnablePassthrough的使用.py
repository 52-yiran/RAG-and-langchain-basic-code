from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, prompt
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

stroutputparser=StrOutputParser()
model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt=ChatPromptTemplate.from_messages(
[
    ("system", "以我提供的已知参考资料为主,简洁并专业的回答用户问题,参考资料:{content}"),
    ("human", "用户提问:{input}"),
]
)
vector_store=InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

vector_store.add_texts(["减肥就要少吃多练","在减脂期间吃东西很重要,清淡少油","跑步是很好的运动"])
input_text="怎么减肥"

retriver=vector_store.as_retriever(search_kwargs={"k":2})

def format_func(docs):
    if not docs:
        return "没有找到相关参考资料"
    reference="["
    for doc in docs:
        reference+=doc.page_content
    reference+="]"
    return reference

def print_prompt(prompt):
    print("*"*20)
    print(prompt.to_string())
    print("*"*20)
    return prompt
chain=({"input":RunnablePassthrough(),"content":retriver|format_func}) | prompt |print_prompt |model | stroutputparser
#字典可作为chain的组件
#retriver:
#输入:用户的提问 str
#输出:向量库的检索结果 list[Document]
#prompt:
#输入:用户的提问+
res=chain.invoke(input_text)
print(res)

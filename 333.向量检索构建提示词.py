from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, prompt
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.output_parsers import StrOutputParser
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
result=vector_store.similarity_search(input_text,k=2)
#print(result)  #document列表,需要转为字符串
reference="["
for doc in result:
    reference+=doc.page_content
reference+="]"
def print_prompt(prompt):
    print(prompt.to_string())
    return prompt

chain=prompt | print_prompt |model | stroutputparser
output=chain.invoke({"content":reference,"input":input_text})
print(output)

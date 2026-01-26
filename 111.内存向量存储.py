from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import PyPDFLoader,CSVLoader
vector_store=InMemoryVectorStore(
    embedding=DashScopeEmbeddings()
)

loader=CSVLoader(
    file_path="./test.csv",
    encoding="gbk",
    )
documents=loader.load()
vector_store.add_documents(
    documents=documents,   #被添加的文档,类型:list[Document]
    ids=["id"+str(i) for i in range(1,len(documents)+1)]                  #�����ӵ��ĵ��ṩid(�ַ���) list[str]
    )
result=vector_store.similarity_search("客场黄潜,主场巴萨,谁会赢",k=2)
print(result)

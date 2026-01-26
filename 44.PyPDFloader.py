from langchain_community.document_loaders import PyPDFLoader,TextLoader
loader=PyPDFLoader(file_path="./1.pdf")
i=0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print("="*20,i)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(file_path="./text.txt", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # 分段的最大字符数
    chunk_overlap=50,   # 分段之间的重叠字符数
    separators=["\n\n", "。", "！", "？", "；", "：", "，", "、"],  # 正确的参数名是 separators
    length_function=len  # 计算字符数的函数
)

split_documents = splitter.split_documents(docs)
print(len(split_documents))
for document in split_documents:
    print("="*20)
    print(document.page_content)
    print("="*20)
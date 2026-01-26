from langchain_community.embeddings import DashScopeEmbeddings
embeddings = DashScopeEmbeddings()
print(embeddings.embed_query("我喜欢你"))
# print(embeddings.embed_documents(["我喜欢你","你是一个好学生","我稀饭你"]))

from langchain_community.document_loaders import JSONLoader
loader=JSONLoader(
    file_path="./stu_json_lines.json",
    jq_schema=".name",
    text_content=False, #告知JSONloader,我抽取的不是字符串,而是整个json对象
    json_lines=True
    )
documents=loader.load()
for document in documents:
    print(document)
    print("="*20)
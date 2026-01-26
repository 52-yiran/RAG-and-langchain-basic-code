from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path="./test_processed.csv",
                  csv_args={"delimiter":","}
                   )
# documents=loader.load()
# for document in documents:
#     print(document.page_content)
#     print("="*20)
for doucument in loader.lazy_load():
    print(doucument.page_content)
    print("="*20)
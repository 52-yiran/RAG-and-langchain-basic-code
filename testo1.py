from langchain_ollama import OllamaLLM
model=OllamaLLM(model="deepseek-r1:8b")
res=model.invoke("你好")
print(res)
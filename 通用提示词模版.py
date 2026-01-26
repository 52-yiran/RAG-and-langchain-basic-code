from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},帮忙起名字,请简略回答."
)
res2=prompt_template.invoke(input={"lastname":"张","gender":"男孩"})
print(res2)
# prompt_text = prompt_template.format_prompt(lastname="张", gender="男孩")
model=Tongyi(model="qwen-plus-2025-12-01")
# res=model.invoke(input=prompt_text)
chain =prompt_template | model
res=chain.invoke(input={"lastname":"张","gender":"男孩"})
print(res)
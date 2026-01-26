from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate,ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")
examples_data = [
    {"word":"开心","antonym":"难过"},
    {"word":"好","antonym":"坏"},
    {"word":"big","antonym":"small"},
]
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=examples_data,
    prefix="告知我的单词的反义词我提供了一些示例:",    #示例之前的提示词
    suffix="基于前面的示例告诉我,{input_word}的反义词是什么?",          #示例之后的提示词
    input_variables=["input_word"],
)
# system_message="你要告诉我单词的反义词,请简略回答."
prompt_text1 = few_shot_template.invoke(input={"input_word":"快乐"}).to_string()
print(prompt_text1)
# prompt_text = system_message +"\n\n" + str(prompt_text1)
model=Tongyi(model="qwen-plus-2025-12-01")
res=model.stream(input=prompt_text1)
for chunk in res:
    print(chunk,end="",flush=True)
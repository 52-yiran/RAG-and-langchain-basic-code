from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt=PromptTemplate.from_template(
    "你需要根据会话历史记录回应用户问题.对话历史:{chat_history},用户问题:{input},请回答"
)
str_parser=StrOutputParser()
def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt
store={}
base_chain=prompt | print_prompt | model | str_parser
def get_history(session_id):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]
conversation_chain=RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history", 
)
if __name__ == "__main__":
    session_config={
        "configurable":{
            "session_id":"123"
        }
    }
    
    res = conversation_chain.invoke( {"input":"小明有两个猫"}, session_config)
    print("第一次执行",res)
    res = conversation_chain.invoke( {"input":"小刚有两个狗"}, session_config)
    print("第二次执行",res)
    res = conversation_chain.invoke( {"input":"一共有几只宠物"}, session_config)
    print("第三次执行",res)

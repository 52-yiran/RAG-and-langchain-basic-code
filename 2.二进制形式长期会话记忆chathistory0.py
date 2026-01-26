from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
import os
import pickle
from warnings import catch_warnings
from langchain_core.chat_history import BaseChatMessageHistory
# from test import messages
#message_to_dict是单个对象(Basemessage类实例)->字典
#messages_from_dict:[字典,字典,....] ->[消息,消息,....]
#AImessage和Humanmessage和Systemmessage是BaseMessage的子类
class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id=session_id              #会话id
        self.storage_path=storage_path          #存储路径
        self.file_path=os.path.join(storage_path,session_id)  #实际的文件路径
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)
    def add_messages(self,messages):
       #sequence序列类似list,tuple
       all_messages=list(self.messages)
       all_messages.extend(messages)
       #使用pickle序列化存储消息对象
       with open(self.file_path, "wb") as f:
           pickle.dump(all_messages, f)
    @property
    def messages(self):
     try:
        with open(self.file_path, "rb") as f:
            return pickle.load(f)
     except (FileNotFoundError, EOFError):
         return []
    def clear(self):
        with open(self.file_path, "wb") as f:
            pickle.dump([], f)

model=ChatTongyi(model="qwen-plus-2025-12-01")
prompt=ChatPromptTemplate.from_messages([
    ("system","你需要根据会话历史回应用户问题,简单点,对话历史:"),
    MessagesPlaceholder("chat_history"),
    ("human","请回答如下问题:{input}")
])
str_parser=StrOutputParser()
def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt
base_chain=prompt | print_prompt | model | str_parser
def get_history(session_id):
  return FileChatMessageHistory(session_id,"./chat_history0")
 
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
    
    # res = conversation_chain.invoke( {"input":"小明有两个猫"}, session_config)
    # print("第一次执行",res)
    # res = conversation_chain.invoke( {"input":"小刚有两个狗"}, session_config)
    # print("第二次执行",res)
    res = conversation_chain.invoke( {"input":"一共有几只宠物"}, session_config)
    print("第三次执行",res)

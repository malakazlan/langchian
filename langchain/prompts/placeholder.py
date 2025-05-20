from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI


import os 
os.environ["GOOGLE_API_KEY"] = "geni api key"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001"
)


#chat template
chat_template = ChatPromptTemplate([
    ('system','you are helpful customer support agent'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])


chat_history = []
#load chat history
with open('langchain/prompts/chat-history.txt') as file:
    chat_history.extend(file.readlines())
    
# print(chat_history)    

prompt = chat_template.invoke({'query' : "where is my refund?",'chat_history' : chat_history})

print(prompt)


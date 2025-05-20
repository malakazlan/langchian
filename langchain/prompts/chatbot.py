from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

import os
os.environ["GOOGLE_API_KEY"] = "geni api key"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
)

chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("Chatbot: ", response.content)
    
print(chat_history)    
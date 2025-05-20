from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

import os 
os.environ["GOOGLE_API_KEY"] = "geni api key"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",

)

messages = [
    SystemMessage(content="You are a helpful Assistance"),
    HumanMessage(content="Tell me about Langchain")
]

response = llm.invoke(messages)

messages.append(AIMessage(content=response.content))

print(response.content)

print(messages)
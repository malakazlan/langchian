from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool,Tool
from langchain_core.messages import ToolMessage
from langchain.schema.runnable import Runnable
from langchain_core.messages import HumanMessage
import requests
import os 

os.environ["GOOGLE_API_KEY"] = "AIzaSyDJz-jcQGuSM8CnxuD3wgqEekkwEMxei08"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-1.5-flash",
    temperature = 0.5,
    max_tokens = 1000
)

#create tool
@tool
def multiply(a:float, b:float)->float:
    "given two number return their product"
    return a*b

# Define a tool
@tool(description="Get the current weather in a given location")
def get_weather(location: str) -> str:
    return "It's sunny."

# print(multiply.invoke({'a':3.9,'b':4.0}))
# print(multiply.description)
# print(multiply.args)

# tool binding 
llm_tool = llm.bind_tools([multiply])


#tool calling
# print(llm_tool.invoke('product of 2 and 3').tool_calls[0]['args'])
# result = llm_tool.invoke('product of 2 and 3')
# print(multiply.invoke(result.tool_calls[0]))

query = HumanMessage('what is product of 3 and 10')

messages = [query]

result = llm_tool.invoke(messages)

# print(result)

messages.append(result)

# print(messages)

tool_result = multiply.invoke(result.tool_calls[0])

# print(tool_result)

messages.append(tool_result)

print(llm_tool.invoke(messages).content)
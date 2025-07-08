from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langchain_core.tools import InjectedToolArg
from typing import Annotated 
from langchain_core.messages import HumanMessage
import requests
import os
import json

os.environ["GOOGLE_API_KEY"] = "Your actual api here "

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.5,
    max_tokens=1000
)

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetchs the latest currency conversion between base currency and target currency
    """
    url = f'Your API HERE {base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()

@tool
def converter(base_currency_value: float,   conversion_rate: Annotated[float,InjectedToolArg]) -> float:
    """
    Given the currency conversion rate this function convert the base currency to target currency using conversion rate .
    """
    return base_currency_value * conversion_rate


# print(get_conversion_factor.invoke({'base_currency':'USD','target_currency':'PKR'}))
# print(converter.invoke({'base_currency_value':10,'conversion_rate':283.8265}))

llm_tools = llm.bind_tools([converter,get_conversion_factor])

message =[HumanMessage("First, get the conversion rate, then multiply 10 USD by that rate to get PKR")]
ai_message = llm_tools.invoke(message)
message.append(ai_message)
# print(ai_message.tool_calls)
for tool_call  in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool1 = get_conversion_factor.invoke(tool_call)
        converstion_rate=json.loads(tool1.content)['conversion_rate']
        print(converstion_rate)
        message.append(tool1)
    if tool_call['name'] == 'converter': 
        tool_call['args']['converstion_rate'] = converstion_rate
        tool2 = converter.invoke(tool_call)
        message.append(tool2)   
        
(llm_tools.invoke(message).content)
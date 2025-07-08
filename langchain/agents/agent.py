from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from langchain_community.tools import DuckDuckGoSearchRun
import requests
import os
import json

os.environ["GOOGLE_API_KEY"] = "Your API here"

model = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
)

serach_tool = DuckDuckGoSearchRun()

@tool
def get_wearther_data(city:str)->str:
    """
    This tool fetches the current weather data of given city
    """
    url = 'http://api.weatherstack.com/current?access_key=apikey&query={city}'
    response = requests.get(url)
    return response.json()


prompt = hub.pull('hwchase17/react')


agent = create_react_agent(
    llm = model,
    tools=[serach_tool,get_wearther_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[serach_tool,get_wearther_data],
    verbose=True

)


responnse = agent_executor.invoke({'input':'Find teh capital of Pakistan and its current weather condition?'})

print(responnse)


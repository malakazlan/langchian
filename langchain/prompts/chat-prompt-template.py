from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


import os 
os.environ["GOOGLE_API_KEY"] = "geni api key"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",

)

chat_template = ChatPromptTemplate([
    ('system','you are helpful {domain} expert'),
    ('human','Explain the {topic} in detial')
])
prompt = chat_template.format_prompt(domain='cricket', topic='Dusra')


response = llm.invoke(prompt)

print(response)
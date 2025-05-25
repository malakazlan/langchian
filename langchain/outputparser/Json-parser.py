from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import os

os.environ["GOOGLE_API_KEY"] ="your api key "

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

model = llm

parser = JsonOutputParser()
template = PromptTemplate(
    template="give the name age and city of the fictinol character {format_instructions}",
    input_variables = [],
    partial_variables = { 'format_instructions' : parser.get_format_instructions}
    
    
)

prmopt = template.format()

chain = template | model | parser

result = chain.invoke({'character' : "batman"})

print(result)

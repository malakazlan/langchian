from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


import os

os.environ["GOOGLE_API_KEY"] ="your api key "

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
    )

model = llm

class Person(BaseModel):
    name :str = Field (description = "the name of the person")
    age : int = Field (description = "the age of the person")
    city : str = Field (description = "the city of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template  = "give the  name age and city of the person {format_instruction}",
    input_variables = [],
    partial_variables = { 'format_instruction' : parser.get_format_instructions()}
)



chain = template | model | parser

result = chain.invoke({})

print(result)

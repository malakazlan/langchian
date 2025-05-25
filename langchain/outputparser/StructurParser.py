from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

import os

os.environ["GOOGLE_API_KEY"] = "your api key "
llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
    )

model = llm

#genrate response schema

name_schema = ResponseSchema(name = "name", description = "the name of the person")
age_schema = ResponseSchema(name = "age", description = "the age of the person")
city_schema = ResponseSchema(name = "city", description = "the city of the person")

response_schemas = [name_schema,  city_schema,age_schema]   

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template = "give the name age and city of the fictinol character {format_instructions}",
    input_variables = [],
    partial_variables = { 'format_instructions' : parser.get_format_instructions}
)

chain = template | model | parser

result = chain.invoke({})

print(result)



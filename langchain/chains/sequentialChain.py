from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GOOGLE_API_KEY"] = "your api key here"

llm = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

model = llm

#sequential chain

template1 = PromptTemplate(
    template= "generate the detail report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "generate four bullet points of the report {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({"topic": "Artificial General Intelligence"})

print(result)

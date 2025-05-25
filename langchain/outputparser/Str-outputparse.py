from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

os.environ["GOOGLE_API_KEY"] = "your api   key "

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

model = llm

#prompt1 
template1 = PromptTemplate(
    template = "expalin in detail  report on  {topic}",
    input_variables = ["topic"]
)

#summray genrate 
template2 = PromptTemplate(
    template = "generate a 4 line summary of the report on {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : "black hole"})
print(result)
# prmopt1 = template1.invoke({'topic' : "black hole"})

# result = model.invoke(prmopt1)

# print(result)

# prmopt2 = template2.invoke({"topic" : result.content})

# result2 = model.invoke(prmopt2)

# print(result2)




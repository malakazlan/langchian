from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GOOGLE_API_KEY"] = "api key "

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

model = llm

template= PromptTemplate(
    template = "generate a short story on  {topic}",
    input_variables = ["topic"]
)



parser = StrOutputParser()

chain = template | model | parser 

result = chain.invoke({"topic": "greedy dog"})

print(result)


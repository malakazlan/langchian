from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDJz-jcQGuSM8CnxuD3wgqEekkwEMxei08"

llm = ChatGoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

model = llm

template1 = PromptTemplate(
    template = "generate a short story on  {topic}",
    input_variables = ["topic"]
)

template2 = PromptTemplate(
    template = "Now tell me the moral of the story  {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model |parser

result = chain.invoke({"topic": "greedy dog"})

print(result)


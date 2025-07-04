from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDJz-jcQGuSM8CnxuD3wgqEekkwEMxei08"

model = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)
 
template1 = PromptTemplate(
    template = "tell me a joke about {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(template1,model,parser)

print(chain.invoke({"topic":'atom'}))
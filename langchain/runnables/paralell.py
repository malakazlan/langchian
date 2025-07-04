from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

import os

os.environ["GOOGLE_API_KEY"] = "ypur actual api key here "

model = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
    temperature = 0.5,
    max_tokens = 1000
)

template1 = PromptTemplate(
    template = "generate a one line tweet about {topic}",
    input_variables= ['topic']
)

template2 = PromptTemplate(
    template = "generate a   one line linkedin post about {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet':  RunnableSequence(template1,model,parser),
    'linkedIn':RunnableSequence(template2,model,parser)

}
)

print(chain.invoke({'topic':'AI'}))


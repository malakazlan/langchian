from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch

import os

os.environ["GOOGLE_API_KEY"] = "your actual api here"

model = GoogleGenerativeAI(
    model = "models/gemini-1.5-flash",
    temperature = 0.5,
    max_tokens = 1000
)

template1= PromptTemplate(
    template=("generate a Report about the  {topic}"),
    input_variables=['topic']
)

parser = StrOutputParser()

report_genrator=RunnableSequence(template1,model,parser)

template2 = PromptTemplate(
    template="Summarize the report {text}",
    input_variables=['text']
)

branch = RunnableBranch(
    (lambda x: len(x.split())>100,RunnableSequence(template2,model,parser)),
    RunnablePassthrough()
    
)

final_chain = RunnableSequence(report_genrator,branch)

intial = report_genrator.invoke({'topic':'AI'})
result= (final_chain.invoke({'topic':'AI'}))
print('word_count initial report',len(intial.split()))
print('word_count after branch',len(result.split()), result)

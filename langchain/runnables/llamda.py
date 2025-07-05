from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

import os

os.environ["GOOGLE_API_KEY"] = "your actual api key here"

model = GoogleGenerativeAI(
    model = "models/gemini-1.5-flash",
    temperature = 0.5,
    max_tokens = 1000
)


template1= PromptTemplate(
    template=("tell me the joke about {topic}"),
    input_variables=['topic']
)

parser = StrOutputParser()

joke_genrator=RunnableSequence(template1,model,parser)



chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x: len(x.split()))
})

final_chain =RunnableSequence(joke_genrator,chain)

result=final_chain.invoke({'topic':'atoms'})
print(result)
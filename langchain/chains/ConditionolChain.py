from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda,RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


import os

os.environ["GOOGLE_API_KEY"] = "your api key here"

model = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="give the sentiment of feedback")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

template = PromptTemplate(
    template = "classify the senitiment of the follwing feedback into posetive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables= {'format_instruction':parser2.get_format_instructions()}
    
)

classifier_chain = template | model | parser2
# print(classifier_chain.invoke({'feedback':'this phone is terrible'}))

# classifier_chain.invoke({'feedback':'this phone is terrible'})
template2 = PromptTemplate(
    template = "write the appropiate  short response into to this postive feedback \n {feedback} ",
    input_variables=['feedback'],
    
)
template3 = PromptTemplate(
    template = "write the appropiate  short response into to this negative feedback\n {feedback}",
    input_variables=['feedback'],
    
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', template2 | model | parser),
    (lambda x: x.sentiment == 'negative', template3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'this phone is terrible'}))









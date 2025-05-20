from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
st.title("Research Assistant")

#static prompt
# user_prompt = st.text_input("Enter a prompt")



#dynamic prompt
paper_input =st.selectbox("select research papper name",["select...", 
"Attenstion is All You Need",
"The Anomaly of Attention in Language Models",
"GPT 3: Fewshot learning"])

style_input = st.selectbox("select research style",["select...",
"Beginner_level","Code_orinted","Mathematical_level"])

length_input = st.selectbox("select research length",["select...",
"Short (1-2  paragraphs)","Medium (3-4 paragraphs)","Long (5-6 paragraphs)"])

import os
os.environ["GOOGLE_API_KEY"] = "geni api key"

# Initialize the LangChain Gemini model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-001",  
    temperature=0.7,                      
    max_output_tokens=1000
                    
)


# #prompt template
# template = PromptTemplate(
    
#     template = """
#     Please summarize the research title {paper_input} with the following explaination:
#     Explaination style: {style_input}
#     Explaination length: {length_input}
    
#     1.Mathmatical Details:
#     - include the relevant mathmatical equations and details if  present in the paper.
#     - Explain the mathmatical concept in simple terms. intutive code snippets where applicable.
    
#     2.Analogies:
#     - Use related analogies to explain the research concept in a way that is easy to understand.
#     if the certain information is not available in the paper, respond with: "Insufficient information available" 
#     instead of guessing.
    
#     Ensure the summary is concise and to the point, alinged with provided style and length.    
#     """,
    
#     input_variables = ["paper_input","style_input","length_input"]
    
# )
template = load_prompt("template.json")

prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})



if st.button("Generate Response"):
    response = llm.invoke(prompt)
    st.write(response.content)
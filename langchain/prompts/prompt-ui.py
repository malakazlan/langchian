from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
st.title("research assistant")

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
os.environ["GOOGLE_API_KEY"] = "api key here "

# Initialize the LangChain Gemini model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-001",  
    temperature=0.7,                      
    max_output_tokens=100 
                    
)

if st.button("Generate Response"):
    prompt = (
        f"Write a research summary for the paper '{paper_input}' "
        f"in a {style_input.replace('_', ' ')} style, "
        f"with a {length_input.lower()}."
    )
    response = llm.invoke(prompt)
    st.write(response.content)

from langchain.prompts import PromptTemplate

#prompt template
template = PromptTemplate(
    
    template = """
    Please summarize the research title {paper_input} with the following explaination:
    Explaination style: {style_input}
    Explaination length: {length_input}
    
    1.Mathmatical Details:
    - include the relevant mathmatical equations and details if  present in the paper.
    - Explain the mathmatical concept in simple terms. intutive code snippets where applicable.
    
    2.Analogies:
    - Use related analogies to explain the research concept in a way that is easy to understand.
    if the certain information is not available in the paper, respond with: "Insufficient information available" 
    instead of guessing.
    
    Ensure the summary is concise and to the point, alinged with provided style and length.    
    """,
    
    input_variables = ["paper_input","style_input","length_input"]
    
)

template.save("template.json")
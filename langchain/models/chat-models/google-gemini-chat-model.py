from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model_name="gemini-1.5-flash", temperature=0.7)

result = llm.invoke("what is the capital of pakistan")

print(result.content)
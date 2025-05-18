from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()



llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

result = llm.invoke("what is the capital of pakistan")

print(result.content)
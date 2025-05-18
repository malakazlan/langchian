from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

text = "Hello, how are you?"

embedding = embeddings.embed_query(text)

print(embedding)

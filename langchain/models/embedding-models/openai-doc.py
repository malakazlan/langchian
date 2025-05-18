from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

doc =[ "This is a test document", "This is another test document",
      "This is a third test document", "This is a fourth test document",
      "This is a fifth test document", "This is a sixth test document",
      "This is a seventh test document", "This is a eighth test document",
      "This is a ninth test document", "This is a tenth test document",
      "This is a eleventh test document", "This is a twelfth test document",
      "This is a thirteenth test document", "This is a fourteenth test document",
      "This is a fifteenth test document", "This is a sixteenth test document",
      ]

embeddings = embeddings.embed_documents(doc)

print(embeddings)

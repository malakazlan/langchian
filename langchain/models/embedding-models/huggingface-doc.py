from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device":"cpu"}
)

doc = [
    "This is a test document",
    "This is another test document",
    "This is a third test document",
]

embeddings = embeddings.embed_documents(doc)

print(embeddings)


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

hf_endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,
    max_new_tokens= 50,
)

llm = ChatHuggingFace(llm=hf_endpoint)

result = llm.invoke("tell me about your program or algos?")

print(result.content)
#This is for local model
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    model_kwargs=dict(
        temperature=0.7,
        max_new_tokens=100
    )
)

result = llm.invoke("what is the capital of pakistan")

print(result.content)
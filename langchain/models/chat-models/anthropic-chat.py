from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="sonnet",temperature=0.7)

result= llm.invoke("what is the capital of pakistan")

print(result.content)
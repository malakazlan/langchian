from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import requests
import os

os.environ["GOOGLE_API_KEY"] = "Your actual API KEY HERE "

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0.5,
    max_tokens=1000
)

# Tool: Get conversion rate
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    url = f'"your PI KEY HERE "/{base_currency}/{target_currency}'
    response = requests.get(url)
    data = response.json()
    if data.get("result") == "success":
        return data["conversion_rate"]
    else:
        raise Exception(f"API error: {data.get('error-type', 'Unknown error')}")

# Tool: Convert currency
def converter(base_currency_value: float, conversion_rate: float) -> float:
    return base_currency_value * conversion_rate

# 1. User asks a question
user_query = "Convert 100 USD to PKR"

# 2. Let Gemini try to parse the request (simulate tool call)
response = llm.invoke([HumanMessage(content=user_query)])
print("Gemini says:", response.content)

# 3. Manually parse the user query (or LLM output) to extract values
# For demo, we'll hardcode extraction:
amount = 100
base = "USD"
target = "PKR"

# 4. Call the tools manually
rate = get_conversion_factor(base, target)
converted = converter(amount, rate)

# 5. Feed the result back to Gemini for a natural answer
followup = (
    f"The conversion rate from {base} to {target} is {rate:.2f}. "
    f"{amount} {base} is {converted:.2f} {target}."
)
final_response = llm.invoke([HumanMessage(content=followup)])
print("Final Gemini answer:", final_response.content)
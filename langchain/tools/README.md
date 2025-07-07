# Langchain Tools

This folder contains Python tools and examples for use with LangChain, focusing on integration with Google Gemini (via `langchain_google_genai`).

## Tools Overview

### 1. `currency_exchange.py`
- **Purpose:** Provides functions to fetch currency conversion rates and perform currency conversion calculations.
- **Key Functions:**
  - `get_conversion_factor(base_currency: str, target_currency: str) -> float`: Fetches the conversion rate between two currencies using an external API.
  - `converter(base_currency_value: float, conversion_rate: float) -> float`: Converts an amount from the base currency to the target currency using the provided rate.
- **Usage Pattern:**
  - The script demonstrates how to use Gemini to generate a response, manually extract the required information, call the tools in Python, and then feed the result back to Gemini for a natural-language answer.
  - **Note:** Tool calling is simulated manually; Gemini does not support automatic function calling.

### 2. `tools.py`
- **Purpose:** Demonstrates tool definition, (attempted) tool binding, and simulated tool calling with Gemini.
- **Key Functions:**
  - `multiply(a: float, b: float) -> float`: Returns the product of two numbers.
  - `get_weather(location: str) -> str`: Returns a dummy weather string ("It's sunny.").
- **Usage Pattern:**
  - Shows how to define tools using the `@tool` decorator.
  - Attempts to use `bind_tools` with Gemini. **Note:** While the code uses `llm.bind_tools([multiply])`, Gemini does not support true function calling/tool binding as OpenAI models do. The tool calling must be handled manually in Python.
  - Demonstrates a simulated tool call: the LLM generates a message, the tool is called in Python, and the result is appended to the conversation.

## Tool Binding and Calling in LangChain

### What is Tool Binding?
Tool binding allows you to register Python functions (tools) with an LLM, so the LLM can call them automatically when it detects a relevant user request. This is supported by OpenAI models in LangChain, but **not** by Gemini models as of June 2024.

### What is Tool Calling?
Tool calling is when the LLM decides to call a registered tool/function to fulfill a user request. In OpenAI models, this is automatic. In Gemini, you must parse the LLM's output and call the tool manually in your code.

### Limitations with Gemini
- `bind_tools` and automatic tool/function calling are **not supported** by Gemini models in LangChain.
- You can define tools and call them manually in Python, but Gemini will not return tool call instructions in its output.
- To simulate tool calling, you:
  1. Let Gemini generate a response to the user query.
  2. Manually extract the needed information from the query or LLM output.
  3. Call the relevant tool in Python.
  4. Optionally, send the tool result back to Gemini for a natural-language answer.

## Example: Simulated Tool Calling with Gemini

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import requests
import os

os.environ["GOOGLE_API_KEY"] = "<YOUR_API_KEY>"

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")

def get_conversion_factor(base, target):
    # ... (see currency_exchange.py)
    pass

def converter(amount, rate):
    return amount * rate

user_query = "Convert 100 USD to PKR"
response = llm.invoke([HumanMessage(content=user_query)])
# Manually extract values from user_query or response.content
amount, base, target = 100, "USD", "PKR"
rate = get_conversion_factor(base, target)
converted = converter(amount, rate)
followup = f"{amount} {base} is {converted:.2f} {target}."
final_response = llm.invoke([HumanMessage(content=followup)])
print(final_response.content)
```

## Summary
- **Automatic tool calling is only available with OpenAI models in LangChain.**
- **With Gemini, tool calling must be handled manually in your Python code.**
- The tools in this folder are ready to use for both manual and (with OpenAI) automatic tool calling scenarios.

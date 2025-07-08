# Agents Module

This directory contains agent implementations for the LangChain-based project. Agents are autonomous entities that use language models and tools to perform complex, multi-step reasoning and actions based on user queries.

---

## What Are Agents?

**Agents** in LangChain are intelligent systems that combine the reasoning power of large language models (LLMs) with the ability to interact with external tools and APIs. Unlike simple chains (which follow a fixed sequence of steps), agents can decide dynamically which actions to take, which tools to use, and in what order, based on the user's query and the results they receive along the way.

Agents are ideal for tasks that require:
- Multi-step reasoning
- Decision making
- Dynamic tool use (e.g., searching the web, calling APIs, performing calculations)

---

## The ReAct Agent Pattern

The **ReAct** (Reasoning and Acting) pattern is a popular approach for building agents. In this pattern, the agent alternates between:
- **Reasoning**: Thinking about what to do next, based on the current state and available information.
- **Acting**: Taking an action, such as calling a tool or API, then using the result to inform the next step.

This loop continues until the agent determines it has enough information to answer the user's query. The ReAct pattern enables agents to break down complex problems into manageable steps, using tools as needed.

---

## How Does the Example Agent Work?

The provided `agent.py` demonstrates a ReAct agent that can:
- Search the web for information (using DuckDuckGo)
- Fetch current weather data for a city (using the Weatherstack API)
- Combine these capabilities to answer complex, multi-part questions

Let's break down each component:

### 1. **Model (LLM)**
```python
model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-001")
```
- Uses Google's Gemini 2.0 Flash model for advanced language understanding and reasoning.
- The LLM is responsible for interpreting the user's query, deciding which tools to use, and synthesizing the final answer.

### 2. **Tools**
```python
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    ...
```
- **DuckDuckGoSearchRun**: Allows the agent to search the web for up-to-date information.
- **get_weather_data**: A custom tool that fetches the current weather for a specified city using the Weatherstack API.
- Tools are functions or classes that the agent can call as needed during its reasoning process.

### 3. **Prompt (ReAct Prompt)**
```python
prompt = hub.pull('hwchase17/react')
```
- The prompt guides the LLM to use the ReAct pattern, encouraging it to reason step-by-step and use tools when necessary.
- The ReAct prompt is designed to help the agent break down complex queries and decide when to act.

### 4. **Agent Creation**
```python
agent = create_react_agent(
    llm=model,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)
```
- `create_react_agent` sets up the agent with the LLM, tools, and prompt.
- `AgentExecutor` manages the agent's execution, handling the loop of reasoning and acting until the task is complete.
- `verbose=True` enables detailed logging of each step.

### 5. **Execution & Example**
```python
response = agent_executor.invoke({'input': 'Find the capital of Pakistan and its current weather condition?'})
print(response)
```
- The agent receives a complex query.
- It first uses the search tool to find the capital of Pakistan (Islamabad).
- Then, it uses the weather tool to fetch the current weather for Islamabad.
- Finally, it combines the results and returns a comprehensive answer.

#### **Sample Output**
```
> Entering new AgentExecutor chain...
Invoking: `DuckDuckGoSearchRun` with `{'query': 'capital of Pakistan'}`
Invoking: `get_weather_data` with `{'city': 'Islamabad'}`
{'output': "The capital of Pakistan is Islamabad. The current weather in Islamabad is ..."}
```

---

## Why Use Agents and ReAct?
- **Flexibility:** Agents can handle a wide range of queries, even those not anticipated by the developer.
- **Transparency:** The ReAct pattern makes the agent's reasoning process interpretable and debuggable.
- **Power:** By combining LLM reasoning with external tools, agents can answer questions that require both knowledge and action.

---

## Extending the Agent
- Add more tools (e.g., currency conversion, news search) by defining new `@tool` functions.
- Swap out the LLM for another model if desired.
- Customize the prompt to guide the agent's behavior for your use case.

---

## Troubleshooting & Tips
- Ensure all API keys are set and valid.
- If the agent fails to chain tools, check tool input/output formats and prompt clarity.
- For advanced workflows, consider using [LangGraph](https://langchain-ai.github.io/langgraph/).

---

## License
This module is part of a larger project and is provided under the project license.

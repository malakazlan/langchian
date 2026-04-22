
<!-- PROJECT BANNER -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-Framework-brightgreen?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMGM2LjYyIDAgMTIgNS4zOCAxMiAxMiAwIDYuNjItNS4zOCAxMi0xMiAxMi02LjYyIDAtMTItNS4zOC0xMi0xMiAwLTYuNjIgNS4zOC0xMiAxMi0xMnoiLz48L3N2Zz4=" alt="LangChain">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</p>

<h1 align="center">🦜️ LangChain : Hands-On AI Workflows with Python</h1>

<p align="center">
  <b>Master LangChain's core concepts with real code, projects, and explanations.<br>
  Build, compose, and extend modern LLM-powered systems step by step!</b>
</p>

---

## 🚀 Project Overview

LangChain is a powerful framework for building applications with large language models (LLMs). This project covers all the essential modules of LangChain, with code, explanations, and real examples for each concept:

| 🧩 Module         | 🔍 What You'll Learn & Build |
|-------------------|-----------------------------|
| 🔗 **Chains**     | Compose multi-step workflows, build pipelines for text generation, summarization, and classification |
| 🤖 **Agents**     | Dynamic, tool-using AI that can reason and act (ReAct pattern, web search, weather, etc.) |
| 🛠️ **Tools**      | Integrate external APIs (currency, weather, math), define Python functions as tools |
| 💬 **Prompts**    | Craft effective instructions, build chatbots, save and reuse prompt templates |
| 🧠 **Models**     | Use and compare LLMs (OpenAI, Gemini, Anthropic, HuggingFace), embeddings, local models |
| 📝 **Output Parsers** | Structure and validate LLM outputs (JSON, Pydantic, text) |
| ⚙️ **Runnables**  | Build composable, reusable AI components (sequential, parallel, branching) |
| 📚 **RAG**        | Retrieval-Augmented Generation: combine retrieval and generation for grounded answers |
| 🗂️ **Indexes**    | (Reserved for future: Efficient storage and retrieval of knowledge) |

---

## 🧠 What is LangChain?

LangChain is an open-source framework for developing applications powered by LLMs. It provides abstractions for chaining together models, prompts, tools, and data sources, enabling you to build:
- Conversational agents
- Knowledge-augmented Q&A systems
- Data pipelines
- Custom AI workflows

**Core Concepts:**

- 🔗 **Chains**: Chains are modular workflows that connect multiple steps—such as prompt creation, model inference, and output parsing—into a single, reusable pipeline. They allow you to build complex reasoning and data processing flows by composing simple building blocks. Chains can be sequential (one step after another), parallel (multiple steps at once), or conditional (branching logic based on results). This enables you to automate multi-step tasks, such as summarizing text, extracting information, or making decisions based on model outputs.

- 🤖 **Agents**: Agents are intelligent entities that use LLMs to reason about which actions to take and which tools to use, dynamically, based on the user's query and the current context. Unlike static chains, agents can decide at runtime which tools or APIs to call, in what order, and how to combine their results. This makes them ideal for open-ended tasks, such as answering complex questions, searching the web, or interacting with external systems. The ReAct (Reasoning + Acting) pattern is a popular approach for building agents that alternate between thinking and taking action.

- 🛠️ **Tools**: Tools are Python functions or external APIs that can be called by agents or chains to perform specific tasks—such as fetching weather data, converting currencies, or searching the web. Tools extend the capabilities of LLMs beyond text generation, allowing them to interact with the real world, access up-to-date information, and perform calculations or lookups. In LangChain, you can easily define your own tools and integrate them into your workflows.

- 💬 **Prompts**: Prompts are templates or message structures that instruct LLMs on what to do. They can be static (fixed text) or dynamic (with variables and context). Effective prompt engineering is crucial for getting accurate and relevant responses from LLMs. LangChain provides utilities for building, saving, and reusing prompt templates, as well as managing chat history and context for conversational applications.

- 🧠 **Models**: Models refer to the LLMs and embedding models used in your workflows. LangChain supports a wide range of providers, including OpenAI (GPT-3.5, GPT-4), Google Gemini, HuggingFace, Anthropic, and more. You can use chat models for conversation, embedding models for semantic search, and even run local models for privacy or cost reasons. The framework makes it easy to swap models and experiment with different providers.

- 📝 **Output Parsers**: Output parsers are components that process and structure the raw output from LLMs. They can convert text into JSON, validate data against schemas (e.g., with Pydantic), or simply return plain text. Output parsers are essential for extracting structured information from model responses, enabling downstream processing, and ensuring data quality in your applications.

- ⚙️ **Runnables**: Runnables are composable, reusable building blocks for AI workflows. They represent operations that can be executed—such as running a model, applying a prompt, or parsing output—and can be chained together in various ways (sequentially, in parallel, with branching logic, etc.). Runnables make it easy to build complex, maintainable pipelines by combining simple components.

- 📚 **RAG (Retrieval-Augmented Generation)**: RAG is a technique that combines information retrieval (finding relevant documents or data) with LLM-based generation. This allows your applications to provide grounded, up-to-date answers by searching a knowledge base and using the retrieved context to inform the model's response. RAG is especially useful for Q&A systems, chatbots, and any scenario where accuracy and transparency are important.

- 🗂️ **Indexes**: Indexes are data structures that organize and store knowledge for efficient retrieval. In LangChain, indexes are used to power semantic search, vector databases, and retrieval systems. They enable your applications to quickly find relevant information, scale to large datasets, and support advanced use cases like RAG.

---

## 📚 Modules & What You'll Learn

<details>
<summary><b>🔗 Chains</b></summary>
Learn to compose simple, sequential, parallel, and conditional chains. Build multi-step pipelines for text generation, summarization, and classification. Example: Sentiment analysis with branching logic.
</details>

<details>
<summary><b>🤖 Agents</b></summary>
Understand what agents are and how they reason and act. Implement the ReAct (Reasoning + Acting) agent pattern. Integrate tools like web search and weather APIs. Example: An agent that finds a city's capital and fetches its weather.
</details>

<details>
<summary><b>🛠️ Tools</b></summary>
Define Python functions as tools for LLMs. Integrate APIs (currency exchange, weather, math, etc.). Learn the difference between manual and automatic tool calling. Example: Currency conversion tool with Gemini and OpenAI.
</details>

<details>
<summary><b>💬 Prompts</b></summary>
Create static and dynamic prompt templates. Build chatbots with context and history. Save and reuse prompt templates. Example: Streamlit research assistant UI, command-line chatbot.
</details>

<details>
<summary><b>🧠 Models</b></summary>
Use and compare chat models (OpenAI, Gemini, Anthropic, HuggingFace). Generate and use embeddings for semantic search. Run local models with HuggingFace. Example: Embedding documents and running local LLMs.
</details>

<details>
<summary><b>📝 Output Parsers</b></summary>
Parse LLM output as JSON, Pydantic models, or plain text. Validate and structure responses for downstream use. Example: Extracting structured data from model outputs.
</details>

<details>
<summary><b>⚙️ Runnables</b></summary>
Build and chain together reusable, composable runnables. Use sequential, parallel, passthrough, lambda, and branching runnables. Example: Multi-platform content generation pipeline.
</details>

<details>
<summary><b>📚 RAG</b></summary>
Implement RAG pipelines with YouTube transcripts. Use vector databases (FAISS) and semantic search. Build Q&A systems grounded in real documents. Example: Ask questions about YouTube video content.
</details>

<details>
<summary><b>🗂️ Indexes</b></summary>
(Reserved for future: Efficient storage and retrieval of knowledge)
</details>

---

## 🛠️ Getting Started

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Langchain
   ```
2. **Install dependencies:**
   ```bash
   pip install -r langchain/requirements.txt
   ```
3. **Set up API keys:**
   - Create a `.env` file or set environment variables for OpenAI, Google, HuggingFace, etc.
   - Example:
     ```python
     os.environ["GOOGLE_API_KEY"] = "your_google_api_key"
     ```
4. **Run examples:**
   - Each module contains scripts and notebooks you can run directly:
     ```bash
     python langchain/chains/simple-chain.py
     python langchain/agents/agent.py
     # ...and so on
     ```
   - For RAG, open and run the Jupyter notebook in `langchain/RAG/youtube_tarnscript.ipynb`

---

## 🗂️ Directory Structure

```text
Langchain/
├── agents/         # 🤖 Autonomous agents and ReAct pattern
├── chains/         # 🔗 Chaining workflows (sequential, parallel, conditional)
├── models/         # 🧠 LLMs, embeddings, and local model demos
├── outputparser/   # 📝 Output parsing and structuring
├── prompts/        # 💬 Prompt engineering and chatbots
├── runnables/      # ⚙️ Composable, reusable AI components
├── tools/          # 🛠️ Custom tools and API integrations
├── RAG/            # 📚 Retrieval-Augmented Generation (RAG) pipelines
├── indexes/        # 🗂️ (Reserved for future knowledge indexing)
├── requirements.txt
└── ...
```

---

## 🧑‍💻 How to Use This Project
- **Explore each module**: Read the README in each folder for detailed explanations and code walkthroughs.
- **Run the code**: Try the scripts and notebooks to see concepts in action.
- **Experiment**: Modify the code, add your own tools, prompts, or models.
- **Learn by doing**: Each module is designed to be hands-on and educational.

---

## 🛠️ Tech Stack & Languages
<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/LangChain-Framework-brightgreen?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMGM2LjYyIDAgMTIgNS4zOCAxMiAxMiAwIDYuNjItNS4zOCAxMi0xMiAxMi02LjYyIDAtMTItNS4zOC0xMi0xMiAwLTYuNjIgNS4zOC0xMiAxMi0xMnoiLz48L3N2Zz4=" alt="LangChain"/>
  <img src="https://img.shields.io/badge/OpenAI-API-black?logo=openai" alt="OpenAI"/>
  <img src="https://img.shields.io/badge/Google-Gemini-blue?logo=google" alt="Google Gemini"/>
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface" alt="HuggingFace"/>
  <img src="https://img.shields.io/badge/Anthropic-API-orange?logo=anthropic" alt="Anthropic"/>
  <img src="https://img.shields.io/badge/FAISS-Vector_DB-green?logo=faiss" alt="FAISS"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit" alt="Streamlit"/>
</p>

---

## 🙏 Acknowledgements & Further Reading
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Google Generative AI](https://ai.google.dev/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [FAISS Vector Database](https://github.com/facebookresearch/faiss)

---

## 📢 Contributing
Contributions, suggestions, and questions are welcome! Open an issue or pull request to help improve this educational resource.

---

## 📄 License
This project is provided under the project license. See LICENSE for details. 
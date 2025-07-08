
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
- 🔗 **Chains**: Link together prompts, models, and parsers for multi-step reasoning
- 🤖 **Agents**: LLMs that can decide which tools to use and in what order
- 🛠️ **Tools**: Python functions/APIs the agent can call
- 💬 **Prompts**: Templates and message structures for instructing LLMs
- 🧠 **Models**: LLMs and embedding models from OpenAI, Google, HuggingFace, Anthropic, etc.
- 📝 **Output Parsers**: Convert LLM output into structured data
- ⚙️ **Runnables**: Composable, reusable building blocks for AI workflows
- 📚 **RAG**: Retrieval-Augmented Generation for context-grounded answers
- 🗂️ **Indexes**: Efficient storage and retrieval of knowledge

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
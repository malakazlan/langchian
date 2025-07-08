# LangChain Project: Hands-On AI Workflows with Python

Welcome to the **LangChain** project! This repository is a comprehensive, hands-on guide to mastering LangChain's core concepts and building real-world AI applications using Python. Each module is designed to teach you not just the theory, but also the practical skills needed to create, compose, and extend modern LLM-powered systems.

---

## 🚀 Project Overview

LangChain is a powerful framework for building applications with large language models (LLMs). This project covers all the essential modules of LangChain, with code, explanations, and real examples for each concept:
- **Chains**: Composing multi-step workflows
- **Agents**: Dynamic, tool-using AI that can reason and act
- **Tools**: Integrating external functions and APIs
- **Prompts**: Crafting effective instructions for LLMs
- **Models**: Using and comparing different LLMs and embedding models
- **Output Parsers**: Structuring and validating LLM outputs
- **Runnables**: Building composable, reusable AI components
- **RAG (Retrieval-Augmented Generation)**: Combining retrieval and generation for grounded answers
- **Indexes**: Organizing and searching knowledge efficiently

Each module includes hands-on projects and code examples to reinforce your understanding.

---

## 🧠 What is LangChain?

LangChain is an open-source framework for developing applications powered by LLMs. It provides abstractions for chaining together models, prompts, tools, and data sources, enabling you to build:
- Conversational agents
- Knowledge-augmented Q&A systems
- Data pipelines
- Custom AI workflows

**Core Concepts:**
- **Chains**: Link together prompts, models, and parsers for multi-step reasoning
- **Agents**: LLMs that can decide which tools to use and in what order
- **Tools**: Python functions/APIs the agent can call
- **Prompts**: Templates and message structures for instructing LLMs
- **Models**: LLMs and embedding models from OpenAI, Google, HuggingFace, Anthropic, etc.
- **Output Parsers**: Convert LLM output into structured data
- **Runnables**: Composable, reusable building blocks for AI workflows
- **RAG**: Retrieval-Augmented Generation for context-grounded answers
- **Indexes**: Efficient storage and retrieval of knowledge

---

## 📚 Modules & What You'll Learn

### 1. `chains/` — **Chaining Workflows**
- Learn to compose simple, sequential, parallel, and conditional chains
- Build multi-step pipelines for text generation, summarization, and classification
- Example: Sentiment analysis with branching logic

### 2. `agents/` — **Autonomous Agents & ReAct Pattern**
- Understand what agents are and how they reason and act
- Implement the ReAct (Reasoning + Acting) agent pattern
- Integrate tools like web search and weather APIs
- Example: An agent that finds a city's capital and fetches its weather

### 3. `tools/` — **Custom Tools & API Integration**
- Define Python functions as tools for LLMs
- Integrate APIs (currency exchange, weather, math, etc.)
- Learn the difference between manual and automatic tool calling
- Example: Currency conversion tool with Gemini and OpenAI

### 4. `prompts/` — **Prompt Engineering & Chatbots**
- Create static and dynamic prompt templates
- Build chatbots with context and history
- Save and reuse prompt templates
- Example: Streamlit research assistant UI, command-line chatbot

### 5. `models/` — **LLMs & Embeddings**
- Use and compare chat models (OpenAI, Gemini, Anthropic, HuggingFace)
- Generate and use embeddings for semantic search
- Run local models with HuggingFace
- Example: Embedding documents and running local LLMs

### 6. `outputparser/` — **Parsing & Structuring LLM Output**
- Parse LLM output as JSON, Pydantic models, or plain text
- Validate and structure responses for downstream use
- Example: Extracting structured data from model outputs

### 7. `runnables/` — **Composable AI Components**
- Build and chain together reusable, composable runnables
- Use sequential, parallel, passthrough, lambda, and branching runnables
- Example: Multi-platform content generation pipeline

### 8. `RAG/` — **Retrieval-Augmented Generation**
- Implement RAG pipelines with YouTube transcripts
- Use vector databases (FAISS) and semantic search
- Build Q&A systems grounded in real documents
- Example: Ask questions about YouTube video content

### 9. `indexes/` — **Knowledge Indexing**
- (Reserved for future: Efficient storage and retrieval of knowledge)

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

```
Langchain/
├── agents/         # Autonomous agents and ReAct pattern
├── chains/         # Chaining workflows (sequential, parallel, conditional)
├── models/         # LLMs, embeddings, and local model demos
├── outputparser/   # Output parsing and structuring
├── prompts/        # Prompt engineering and chatbots
├── runnables/      # Composable, reusable AI components
├── tools/          # Custom tools and API integrations
├── RAG/            # Retrieval-Augmented Generation (RAG) pipelines
├── indexes/        # (Reserved for future knowledge indexing)
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
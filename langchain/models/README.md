# Models Directory Overview

This directory contains all the model-related code for the Langchain project. The structure is organized to separate different types of models and their usages, including chat models, embedding models, and local/LLM demos. Below is a detailed explanation of the folder structure and each Python file within it.

## Folder Structure

```
models/
├── chat-models/
│   ├── anthropic.py
│   ├── google-gemini.py
│   ├── huggingfh-chat.py
│   └── openai-chat.py
├── embedding-models/
│   ├── huggingface-doc.py
│   ├── huggingface.py
│   ├── openai-doc.py
│   └── openai.py
├── llm's-models/
│   └── openai_llm_demo.py
├── local-model-hugginface.py
└── README.md
```

---

## Subfolders and Files

### 1. `chat-models/`
Contains scripts for interacting with various chat-based large language models (LLMs):

- **anthropic.py**
  - Uses Anthropic's Claude model via `langchain_anthropic`.
  - Example usage: Sends a prompt to the Claude model and prints the response.
  - Useful for experimenting with Anthropic's conversational AI.

- **google-gemini.py**
  - Uses Google's Gemini model via `langchain_google_genai`.
  - Example usage: Sends a prompt to Gemini and prints the response.
  - Demonstrates integration with Google GenAI chat models.

- **huggingfh-chat.py**
  - Uses HuggingFace's Zephyr-7B-beta model for chat via `langchain_huggingface`.
  - Shows how to set parameters like temperature and max tokens.
  - Example usage: Sends a prompt and prints the model's response.

- **openai-chat.py**
  - Uses OpenAI's GPT-3.5-turbo model for chat via `langchain_openai`.
  - Example usage: Sends a prompt and prints the response.
  - Demonstrates basic OpenAI chat model integration.

### 2. `embedding-models/`
Contains scripts for generating embeddings (vector representations) from text using different providers:

- **huggingface-doc.py**
  - Uses HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` to embed a list of documents.
  - Example usage: Embeds multiple documents and prints their embeddings.

- **huggingface.py**
  - Uses HuggingFace's embedding model to embed a single query string.
  - Example usage: Embeds a single text and prints the embedding vector.

- **openai-doc.py**
  - Uses OpenAI's `text-embedding-3-small` model to embed a list of documents.
  - Example usage: Embeds multiple documents and prints their embeddings.

- **openai.py**
  - Uses OpenAI's embedding model to embed a single query string.
  - Example usage: Embeds a single text and prints the embedding vector.

### 3. `llm's-models/`
Contains demonstration scripts for working with LLMs directly:

- **openai_llm_demo.py**
  - Uses OpenAI's GPT-3.5-turbo model for direct LLM invocation (not chat-specific).
  - Example usage: Sends a prompt and prints the model's response.

### 4. `local-model-hugginface.py`
- Demonstrates how to use a HuggingFace model locally via `HuggingFacePipeline`.
- Loads the Zephyr-7B-beta model for text generation.
- Example usage: Sends a prompt to the local model and prints the response.

---

## Usage
- Each script is self-contained and can be run directly to test the respective model or embedding.
- Make sure to set up your `.env` file with the required API keys for each provider (OpenAI, HuggingFace, Google, Anthropic) before running the scripts.
- The `chat-models` and `embedding-models` folders are designed for modular experimentation and can be extended with additional models as needed.

---

## Best Practices
- **Do not commit your `.env` file with secrets to version control.**
- Use these scripts as templates for integrating new models or for quick experimentation with different LLM providers.

---

For more details on each provider or model, refer to the respective script and the official documentation of the provider.

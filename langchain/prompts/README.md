# README: `langchain/prompts` Folder

This folder contains various scripts and resources for working with prompt templates, chatbots, and message handling using LangChain and Google Gemini models.

---

## Introduction: Static and Dynamic Prompts

**Static Prompts:**
A static prompt is a fixed string or message sent to a language model. It does not change based on user input or context. Static prompts are useful for simple, repeatable tasks where the instructions or questions remain the same every time.

**Dynamic Prompts:**
A dynamic prompt is generated at runtime, often by filling in variables or placeholders with user input or contextual information. Dynamic prompts allow for more flexible and personalized interactions, adapting the prompt to the current conversation or task.

---

## LangChain Libraries and Their Usage

### 1. `ChatPromptTemplate`
- **Purpose:** Used to define multi-turn conversational templates, including system, human, and AI messages. Supports placeholders for variables and can include chat history using `MessagesPlaceholder`.
- **Usage:**
  - Define a sequence of message roles (system, human, AI) and their content.
  - Use placeholders (e.g., `{query}`) for dynamic insertion of user input or context.
  - Can include `MessagesPlaceholder` to insert previous chat history into the prompt.

### 2. `PromptTemplate`
- **Purpose:** Used for single-turn or non-conversational prompts, with support for variable placeholders.
- **Usage:**
  - Define a template string with variables (e.g., `{paper_input}`) and specify the required input variables.
  - Fill the template at runtime with actual values to generate the final prompt string.

### 3. `Messages` and Their Types
- **Purpose:** Represent individual messages in a conversation, with different roles.
- **Types:**
  - `SystemMessage`: Sets the behavior or persona of the AI (e.g., "You are a helpful assistant").
  - `HumanMessage`: Represents user input or questions.
  - `AIMessage`: Represents responses from the AI model.
- **Usage:**
  - Create a list of messages to represent the conversation history.
  - Pass this list to the language model to maintain context across turns.

---

Below is an explanation of each file and its purpose.

---

## 1. `prompt-ui.py`
**Heading:** Streamlit Research Assistant UI

**Explanation:**  
This script creates a web-based research assistant using Streamlit. Users can select a research paper, explanation style, and length from dropdown menus. The script loads a prompt template (from `template.json`), fills it with user selections, and sends it to a Gemini LLM for a generated summary. The response is displayed in the UI when the user clicks "Generate Response".

---

## 2. `placeholder.py`
**Heading:** Chat Template with Chat History Placeholder

**Explanation:**  
This script demonstrates how to use a `ChatPromptTemplate` with a `MessagesPlaceholder` to include chat history in prompts. It loads previous chat history from `chat-history.txt`, constructs a prompt with a system message, the chat history, and a new user query, and prints the resulting prompt structure. (Note: The chat history is loaded as plain text lines, but for full functionality, it should be parsed into message objects.)

---

## 3. `messages.py`
**Heading:** Basic Message Handling Example

**Explanation:**  
This script shows how to create a list of messages (system and human), send them to a Gemini LLM, and append the AI's response to the message history. It prints both the AI's response and the updated message list, demonstrating a simple conversational flow.

---

## 4. `chatbot.py`
**Heading:** Command-Line Chatbot with Persistent History

**Explanation:**  
A simple command-line chatbot that maintains a conversation history. The user can interact with the bot in a loop, and each message (from both user and AI) is appended to the history. Typing "exit" ends the chat and prints the full conversation history.

---

## 5. `chat-prompt-template.py`
**Heading:** Parameterized Chat Prompt Example

**Explanation:**  
This script demonstrates how to use a `ChatPromptTemplate` with variable placeholders (e.g., `{domain}`, `{topic}`) to generate a prompt dynamically. The filled prompt is sent to the Gemini LLM, and the response is printed.

---

## 6. `savetemplate.py`
**Heading:** Save Custom Prompt Template to File

**Explanation:**  
This script creates a detailed prompt template for summarizing research papers, with placeholders for paper name, style, and length. The template includes instructions for mathematical details and analogies. It saves the template to `template.json` for reuse in other scripts (like `prompt-ui.py`).

---

## 7. `chat-history.txt`
**Heading:** Example Chat History File

**Explanation:**  
A plain text file containing example chat history in the form of serialized message objects. Used by `placeholder.py` to demonstrate loading and including previous conversation context in prompts.

---

## 8. `template.json`
**Heading:** Serialized Prompt Template

**Explanation:**  
A JSON file (created by `savetemplate.py`) that stores the research summary prompt template. This file is loaded by `prompt-ui.py` to ensure consistent prompt formatting.

---

## Summary

The `langchain/prompts` folder provides a set of examples and utilities for:
- Building prompt templates (with or without variables)
- Saving and loading templates for reuse
- Creating chatbots (both command-line and web-based)
- Handling chat history and message objects
- Integrating with Google Gemini LLMs via LangChain

These scripts serve as a practical reference for developing conversational AI applications with prompt engineering and context management.

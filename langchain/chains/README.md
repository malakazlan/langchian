# Chains in Langchain

This directory demonstrates the concept of **chaining** in Langchain, a powerful technique for composing multiple operations (such as prompt templates, language models, and output parsers) into a single, reusable workflow. Chaining allows you to build complex data processing and reasoning pipelines by connecting simple components together.

## What is Chaining?

**Chaining** refers to the process of linking together multiple steps—such as prompt creation, model inference, and output parsing—so that the output of one step becomes the input to the next. This enables modular, readable, and maintainable code for building advanced AI applications.

## Types of Chains

This folder contains examples of several types of chains:

### 1. Simple Chain
- **File:** `simple-chain.py`
- **Description:** A basic chain that takes a topic, generates a short story using a language model, and parses the output.
- **Usage Example:**
  ```python
  chain = template | model | parser
  result = chain.invoke({"topic": "greedy dog"})
  ```

### 2. Sequential Chain
- **File:** `sequentialChain.py`
- **Description:** Chains multiple steps in sequence. For example, it first generates a detailed report on a topic, then creates bullet points from that report.
- **Usage Example:**
  ```python
  chain = template1 | model | parser | template2 | model | parser
  result = chain.invoke({"topic": "Artificial General Intelligence"})
  ```

### 3. Parallel Chain
- **File:** `parallel-chain.py`
- **Description:** Runs multiple chains in parallel on the same input, then merges their results. For example, it generates both a report and questions about a text, then combines them.
- **Usage Example:**
  ```python
  parallel_chain = RunnableParallel({
      'report': template1 | model | parser,
      'questions': template2 | model2 | parser,
  })
  merge_chain = parallel_chain | template3 | model | parser
  result = merge_chain.invoke(text)
  ```

### 4. Conditional Chain (Branching)
- **File:** `ConditionolChain.py`
- **Description:** Uses the output of one chain to decide which subsequent chain to run. For example, it classifies feedback as positive or negative, then generates an appropriate response based on the sentiment.
- **Usage Example:**
  ```python
  classifier_chain = template | model | parser2
  branch_chain = RunnableBranch(
      (lambda x: x.sentiment == 'positive', template2 | model | parser),
      (lambda x: x.sentiment == 'negative', template3 | model | parser),
      RunnableLambda(lambda x: "Could not find the sentiment")
  )
  chain = classifier_chain | branch_chain
  result = chain.invoke({'feedback': 'this phone is terrible'})
  ```

## How to Use

1. **Set your Google API key** in the environment variable `GOOGLE_API_KEY` before running the scripts.
2. Run any of the example scripts to see chaining in action:
   ```bash
   python simple-chain.py
   python sequentialChain.py
   python parallel-chain.py
   python ConditionolChain.py
   ```

## Summary

Chaining is a core concept in Langchain that enables the composition of modular, reusable, and powerful AI workflows. By combining simple, sequential, parallel, and conditional chains, you can build sophisticated applications with minimal code.

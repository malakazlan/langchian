# Output Parsers in Langchain

This folder contains different output parsers used to process and structure the outputs from language models. Each parser serves a specific purpose and is demonstrated with a usage example.

---

## 1. PydanticOutputParser (`pydantic-parser.py`)

**Explanation:**
The `PydanticOutputParser` is used to parse the output of a language model into a Pydantic model, ensuring structured and validated data. This is useful when you want the output to conform to a specific schema.

**Usage Example:**
- Define a Pydantic model (e.g., `Person` with fields `name`, `age`, `city`).
- Use `PydanticOutputParser` with this model.
- Create a prompt and chain it with the model and parser.
- The output will be a validated Pydantic object.

---

## 2. StructuredOutputParser (`StructurParser.py`)

**Explanation:**
The `StructuredOutputParser` allows you to define a schema for the expected output using `ResponseSchema` objects. It parses the model's output into a structured dictionary based on the provided schema.

**Usage Example:**
- Define response schemas for each field (e.g., `name`, `age`, `city`).
- Use `StructuredOutputParser.from_response_schemas()` to create the parser.
- Chain the prompt, model, and parser.
- The output will be a dictionary matching the schema.

---

## 3. JsonOutputParser (`Json-parser.py`)

**Explanation:**
The `JsonOutputParser` parses the output of a language model as JSON. This is useful when you expect the model to return data in JSON format and want to directly convert it to a Python dictionary.

**Usage Example:**
- Use `JsonOutputParser` in your chain.
- The prompt should instruct the model to return output in JSON format.
- The output will be parsed as a Python dictionary.

---

## 4. StrOutputParser (`Str-outputparse.py`)

**Explanation:**
The `StrOutputParser` simply returns the output as a string. It is useful for cases where you want the raw text output from the model, or when chaining multiple prompts/models together.

**Usage Example:**
- Use `StrOutputParser` in your chain.
- The output will be a plain string, which can be further processed or used in subsequent prompts.

---

Each parser is demonstrated in its respective Python file with a sample chain and print statement to show the result.

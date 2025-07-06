# RAG (Retrieval-Augmented Generation) with YouTube Transcripts

This section demonstrates how to build a **Retrieval-Augmented Generation (RAG)** system using YouTube video transcripts. The system extracts transcripts from YouTube videos, processes them, and creates an intelligent Q&A system.

## What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that combines:
- **Retrieval**: Finding relevant information from a knowledge base
- **Generation**: Using an LLM to generate responses based on retrieved context

This approach helps LLMs provide more accurate and up-to-date information by grounding their responses in specific documents or data.

## Project Overview

The notebook `youtube_tarnscript.ipynb` implements a complete RAG pipeline that:

1. **Extracts YouTube Transcripts** using the YouTube Transcript API
2. **Processes and Chunks** the transcript text for efficient retrieval
3. **Creates Vector Embeddings** using Google's Generative AI
4. **Builds a Vector Database** using FAISS for similarity search
5. **Implements Retrieval** to find relevant context for questions
6. **Generates Answers** using an LLM with retrieved context

## Key Components

### 1. **Data Extraction** (`youtube_transcript_api`)
```python
from youtube_transcript_api import YouTubeTranscriptApi
video_Id = "Q7mS1VHm3Yw"
transcript_list = YouTubeTranscriptApi.get_transcript(video_Id, languages=['en'])
transcript = " ".join(chunk['text'] for chunk in transcript_list)
```

### 2. **Text Processing** (`RecursiveCharacterTextSplitter`)
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=350)
chunks = splitter.create_documents([transcript])
```

### 3. **Vector Embeddings** (`GoogleGenerativeAIEmbeddings`)
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
```

### 4. **Vector Database** (`FAISS`)
```python
from langchain_community.vectorstores import FAISS
vector_store = FAISS.from_documents(chunks, embeddings)
```

### 5. **Retrieval System**
```python
retriever = vector_store.as_retriever(
    search_type="similarity", 
    search_kwargs={'k': 4}
)
```

### 6. **LLM Integration** (`GoogleGenerativeAI`)
```python
from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model='models/gemini-1.5-flash', temperature=0.5)
```

### 7. **Prompt Engineering**
```python
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template="""
    You are a helpful AI assistant.
    Answer only when context is provided.
    If no context is given, just say "I don't know; no context is given."
    
    {context}
    Question: {question}
    """,
    input_variables=['context', 'question']
)
```

### 8. **Runnable Chain** (Advanced Implementation)
```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

main_chain = parallel_chain | prompt | llm | StrOutputParser()
```

## Workflow Steps

### Step 1: Extract YouTube Transcript
- Use YouTube video ID to fetch transcript
- Combine all transcript chunks into a single text

### Step 2: Text Chunking
- Split long transcript into smaller, manageable chunks
- Use overlapping chunks to maintain context continuity
- Chunk size: 2000 characters, Overlap: 350 characters

### Step 3: Create Vector Embeddings
- Convert text chunks into numerical vectors
- Use Google's embedding model for semantic representation

### Step 4: Build Vector Database
- Store embeddings in FAISS vector database
- Enable fast similarity search capabilities

### Step 5: Implement Retrieval
- Create retriever with similarity search
- Retrieve top-k most relevant chunks for any query

### Step 6: Generate Responses
- Combine retrieved context with user question
- Use LLM to generate contextual answers

## Use Cases

This RAG system is perfect for:

1. **Video Content Analysis**: Extract insights from YouTube videos
2. **Educational Content**: Create Q&A systems for educational videos
3. **Content Summarization**: Generate summaries of video content
4. **Research**: Analyze and query video transcripts
5. **Documentation**: Create searchable knowledge bases from video content

## Key Features

- **Semantic Search**: Find relevant content even with different wordings
- **Context-Aware Responses**: LLM generates answers based on retrieved context
- **Scalable**: Can handle multiple videos and large transcripts
- **Flexible**: Easy to modify for different types of content
- **Efficient**: Uses vector similarity for fast retrieval

## Requirements

- `youtube-transcript-api`: For extracting YouTube transcripts
- `langchain`: Core RAG framework
- `langchain-google-genai`: Google AI integration
- `faiss-cpu`: Vector database
- `google-generativeai`: Google's Generative AI models

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install youtube-transcript-api langchain langchain-google-genai faiss-cpu google-generativeai
   ```

2. **Set API Key**:
   ```python
   import os
   os.environ["GOOGLE_API_KEY"] = "your_actual_api_key_here"
   ```

3. **Run the Notebook**: Execute cells in `youtube_tarnscript.ipynb`

## Example Usage

```python
# Ask questions about the video content
response = main_chain.invoke("What is the main topic of this video?")
print(response)

# Get specific information
response = main_chain.invoke("What techniques are discussed for book recommendations?")
print(response)
```

## Benefits of This Approach

1. **Accuracy**: Responses are grounded in actual video content
2. **Relevance**: Only uses context that's actually relevant to the question
3. **Transparency**: Can trace back to source content
4. **Efficiency**: Fast retrieval and generation
5. **Scalability**: Can handle multiple videos and large datasets

This RAG implementation demonstrates how to create intelligent systems that can understand and respond to questions about video content, making it a powerful tool for content analysis and knowledge extraction.

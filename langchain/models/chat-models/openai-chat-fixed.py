import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI

def load_environment():
    """Robust environment loading function"""
    
    # Try multiple possible locations for .env file
    env_paths = [
        ".env",                    # Current directory
        "../.env",                 # Parent directory  
        "../../.env",              # Root directory
        ".env.local",              # Local environment
    ]
    
    # Try to load from each location
    for path in env_paths:
        if Path(path).exists():
            print(f"Loading .env from: {path}")
            load_dotenv(path, override=True)
            break
    else:
        print("Warning: No .env file found in common locations")
    
    # Check if API key is loaded
    if 'OPENAI_API_KEY' not in os.environ:
        print("ERROR: OPENAI_API_KEY not found in environment variables")
        print("Please ensure your .env file contains:")
        print("OPENAI_API_KEY=sk-your-actual-key-here")
        return False
    
    print("Environment loaded successfully!")
    return True

# Load environment
if not load_environment():
    print("Failed to load environment. Exiting...")
    exit(1)

# Create the chat model
try:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    print("ChatOpenAI model created successfully!")
except Exception as e:
    print(f"Error creating ChatOpenAI model: {e}")
    exit(1)

# Test the model
try:
    result = llm.invoke("what is the capital of France?")
    print(f"Response: {result}")
except Exception as e:
    print(f"Error invoking model: {e}")
    print("This might be due to:")
    print("1. Invalid API key")
    print("2. Network connectivity issues")
    print("3. OpenAI service issues") 
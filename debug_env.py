import os
from dotenv import load_dotenv
from pathlib import Path

def debug_env_loading():
    """Debug function to help identify why load_dotenv() is not working"""
    
    print("=== Environment Loading Debug ===\n")
    
    # 1. Check current working directory
    print(f"1. Current working directory: {os.getcwd()}")
    
    # 2. Check if .env file exists in current directory
    current_env = Path(".env")
    print(f"2. .env file in current directory exists: {current_env.exists()}")
    
    # 3. Check if .env file exists in parent directory
    parent_env = Path("../.env")
    print(f"3. .env file in parent directory exists: {parent_env.exists()}")
    
    # 4. Check if .env file exists in root directory (2 levels up)
    root_env = Path("../../.env")
    print(f"4. .env file in root directory exists: {root_env.exists()}")
    
    # 5. List all .env files in current and parent directories
    print("\n5. Searching for .env files:")
    for path in Path(".").rglob(".env"):
        print(f"   Found: {path}")
    
    # 6. Try to load .env file explicitly
    print("\n6. Attempting to load .env files:")
    
    # Try current directory
    if current_env.exists():
        print("   Loading .env from current directory...")
        load_dotenv(current_env)
    elif parent_env.exists():
        print("   Loading .env from parent directory...")
        load_dotenv(parent_env)
    elif root_env.exists():
        print("   Loading .env from root directory...")
        load_dotenv(root_env)
    else:
        print("   No .env file found in common locations")
    
    # 7. Check if OPENAI_API_KEY is loaded
    print(f"\n7. OPENAI_API_KEY loaded: {'OPENAI_API_KEY' in os.environ}")
    if 'OPENAI_API_KEY' in os.environ:
        api_key = os.environ['OPENAI_API_KEY']
        print(f"   API Key (first 10 chars): {api_key[:10]}...")
        print(f"   API Key length: {len(api_key)}")
    else:
        print("   OPENAI_API_KEY not found in environment")
    
    # 8. Check for common variations of the key name
    print("\n8. Checking for common API key variations:")
    variations = ['OPENAI_API_KEY', 'OPENAI-API-KEY', 'OPENAI_API_KEY', 'OPENAIAPIKEY']
    for var in variations:
        if var in os.environ:
            print(f"   Found: {var}")
        else:
            print(f"   Not found: {var}")
    
    # 9. Show all environment variables that contain 'OPENAI'
    print("\n9. All environment variables containing 'OPENAI':")
    openai_vars = [key for key in os.environ.keys() if 'OPENAI' in key.upper()]
    if openai_vars:
        for var in openai_vars:
            print(f"   {var}: {os.environ[var][:10]}...")
    else:
        print("   No environment variables containing 'OPENAI' found")

def fix_env_loading():
    """Function to fix common load_dotenv issues"""
    
    print("\n=== Fixing Environment Loading ===\n")
    
    # Method 1: Try loading from specific path
    env_paths = [".env", "../.env", "../../.env", ".env.local"]
    
    for path in env_paths:
        if Path(path).exists():
            print(f"Loading .env from: {path}")
            load_dotenv(path, override=True)
            break
    else:
        print("No .env file found in common locations")
        return False
    
    # Method 2: Set the key manually if still not found
    if 'OPENAI_API_KEY' not in os.environ:
        print("OPENAI_API_KEY still not found. Please check your .env file format.")
        print("Your .env file should contain:")
        print("OPENAI_API_KEY=sk-your-actual-key-here")
        return False
    
    print("Environment loaded successfully!")
    return True

if __name__ == "__main__":
    debug_env_loading()
    fix_env_loading() 
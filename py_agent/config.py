"""Configuration and environment setup."""
import os
import getpass
from dotenv import load_dotenv

# Load environment variables
try:
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. To use .env files, run: pip install python-dotenv")

def setup_api_keys():
    """Set up required API keys."""
    # OpenRouter API key
    if not os.environ.get("OPENROUTER_API_KEY"):
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            api_key = getpass.getpass("Enter API key for OpenRouter: ")
        os.environ["OPENROUTER_API_KEY"] = api_key or "DUMMY_KEY"
        
    # Orchid Proxy API key
    if not os.environ.get("ORCHID_API_KEY"):
        api_key = os.getenv("ORCHID_API_KEY")
        if not api_key:
            api_key = getpass.getpass("Enter API key for Orchid Proxy: ")
        os.environ["ORCHID_API_KEY"] = api_key or "DUMMY_KEY"
        
    # SerpAPI key validation
    if not os.getenv("SERPAPI_API_KEY"):
        print("Warning: SERPAPI_API_KEY not found in environment variables.")
        print("Please set SERPAPI_API_KEY in your .env file for web search functionality.")

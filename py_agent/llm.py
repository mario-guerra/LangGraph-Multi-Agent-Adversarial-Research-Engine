import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# We expect setup_api_keys to handle the interactive parts if missing,
# but we need to ensure they are at least somewhat present for imports.
for key in ["OPENROUTER_API_KEY", "ORCHID_API_KEY"]:
    if not os.environ.get(key):
        os.environ[key] = os.getenv(key) or f"DUMMY_{key}"

# Common kwargs for all OpenRouter models
openrouter_kwargs = {
    "openai_api_key": os.environ.get("OPENROUTER_API_KEY"),
    "openai_api_base": "https://openrouter.ai/api/v1",
    "temperature": 0,
}

# 1. Fast / structured (Gemini Flash replacement)
gemini_flash = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct",
    **openrouter_kwargs
)

# 2. Planner / Optimist (o3-mini replacement)
o3_mini = ChatOpenAI(
    model="deepseek/deepseek-chat",
    **openrouter_kwargs
)

# 3. Critic / Judge (Claude Sonnet replacement)
claude_sonnet = ChatOpenAI(
    model="deepseek/deepseek-chat",
    **openrouter_kwargs
)

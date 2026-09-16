"""
config.py — LLM model setup and environment configuration.

This is the first file to set up. Import the configured model
into chain.py to build your pipeline.
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# ── LLM Configuration ──────────────────────────────────────────────────────
# Swap the model here without touching chain.py.
# Use a small, fast model for simple tasks; a larger one for complex reasoning.

default_llm = ChatOpenAI(
    model="gpt-4o-mini",   # Fast and cheap — good for most tasks
    temperature=0,          # 0 = deterministic, higher = more creative
    api_key=os.environ.get("OPENAI_API_KEY"),
)

reasoning_llm = ChatOpenAI(
    model="gpt-4o",        # Use for tasks requiring deeper reasoning
    temperature=0.2,
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# To use Anthropic instead:
# from langchain_anthropic import ChatAnthropic
# default_llm = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0)

# To use Google instead:
# from langchain_google_genai import ChatGoogleGenerativeAI
# default_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

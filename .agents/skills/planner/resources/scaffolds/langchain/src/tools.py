"""
tools.py — Optional tool definitions for the chain.

Only include this file if your chain needs to call external functions.
For simple transformation chains (prompt → LLM → parse), tools are not needed.

Tools are bound to the LLM in chain.py:
    llm_with_tools = llm.bind_tools(all_tools)
"""
from langchain_core.tools import tool


@tool
def search_web(query: str) -> str:
    """
    Search the web for current information about a query.
    Use this when you need up-to-date facts, news, or documentation.
    Input: A specific search query.
    Output: Top search results as a string.
    """
    # Replace with a real implementation discovered in Phase 3.
    # Example:
    # import requests
    # response = requests.get(
    #     "https://api.serpapi.com/search",
    #     params={"q": query, "api_key": os.environ["SERPAPI_KEY"]}
    # )
    # return str(response.json().get("organic_results", [])[:3])
    return f"[Mock result for: '{query}'] — Replace with real implementation."


@tool
def calculate(expression: str) -> str:
    """
    Safely evaluate a mathematical expression.
    Input: A Python math expression string (e.g., '2 + 2 * 10').
    Output: The result as a string.
    """
    try:
        # WARNING: eval is used here for simplicity.
        # In production, use a safe math parser like `simpleeval`.
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"


# Register all tools. Imported by chain.py.
all_tools = [search_web, calculate]

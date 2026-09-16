"""
tools.py — Custom tool definitions for this project.

Each tool is decorated with @tool. Tools are imported in graph.py
and bound to LLM models or injected into ToolNode.

Design rules:
- One tool per function.
- Write a clear docstring — the LLM reads it to decide when to use the tool.
- Keep tools pure (no side effects unless necessary).
- Import and register all tools in the `all_tools` list at the bottom.
"""
import os
from langchain_core.tools import tool


@tool
def search_web(query: str) -> str:
    """
    Search the web for up-to-date information about a query.
    Use this when you need recent news, documentation, or factual data.
    Input: A specific search query string.
    Output: A string with the top search results.
    """
    # Replace with a real implementation discovered in Phase 3.
    # Example with SerpAPI:
    # from serpapi import GoogleSearch
    # results = GoogleSearch({
    #     "q": query,
    #     "api_key": os.environ["SERPAPI_KEY"]
    # }).get_dict()
    # return "\n".join([r.get("snippet", "") for r in results.get("organic_results", [])[:5]])

    return f"[Mock web search result for: '{query}'] — Replace with real implementation."


@tool
def read_file(filepath: str) -> str:
    """
    Read the contents of a local file.
    Use this when you need to access data stored in a file on disk.
    Input: Absolute or relative path to the file.
    Output: The file's text contents, or an error message.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at path '{filepath}'."
    except Exception as e:
        return f"Error reading file: {e}"


# Register all tools here. This list is imported by graph.py.
all_tools = [search_web, read_file]

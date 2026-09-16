"""
tools/custom_tool.py — Project-specific custom tools.

Each tool is a class that inherits from BaseTool (from crewai_tools).
The agent receives the tool description and uses it to decide when to call it.

To add a new tool:
  1. Create a new class here (or a new file in tools/)
  2. Import and inject it in crew.py -> @agent method -> tools=[YourTool()]

See: https://docs.crewai.com/concepts/tools
"""
from crewai_tools import BaseTool


class ExampleSearchTool(BaseTool):
    """
    Example custom search tool.
    Replace this with your actual tool logic discovered in Phase 3.
    """
    name: str = "Example Search Tool"
    description: str = (
        "Searches for information about a given topic. "
        "Input should be a search query string. "
        "Returns a string with the top search results."
    )

    def _run(self, query: str) -> str:
        """
        Core tool logic. This is what runs when an agent calls this tool.
        Replace with your actual implementation.
        """
        # Example: call a real search API, query a database, read a file, etc.
        # from serpapi import GoogleSearch
        # results = GoogleSearch({"q": query, "api_key": os.environ["SERPAPI_KEY"]}).get_dict()
        # return str(results.get("organic_results", [])[:3])

        return f"[Mock result for query: '{query}'] — Replace this with real implementation."

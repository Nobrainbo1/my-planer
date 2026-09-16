"""
edges.py — Conditional routing logic (the "D" in SIDE).

Each function here is a routing function used in add_conditional_edges().
It reads the current state and returns the NAME of the next node to visit,
or END to terminate the graph.

Design rules:
- Routing functions must be PURE — no side effects, just read state and return a string.
- Never put business logic here; that belongs in nodes.py.
- Return values must match the keys in the routing dict passed to add_conditional_edges().
"""
from langchain_core.messages import ToolMessage
from langgraph.graph import END

from agent.state import AgentState


def should_researcher_continue(state: AgentState) -> str:
    """
    After the researcher node runs, decide what to do next.

    - If the LLM made tool calls → route to the "tools" node to execute them.
    - Otherwise → route to the "writer" node to generate the final report.
    """
    last_message = state["messages"][-1]

    # Check if the last message contains tool calls
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"

    # No tool calls — research is done, move to writing
    return "writer"


def should_continue_or_end(state: AgentState) -> str:
    """
    A generic termination check.
    Extend this for more complex routing logic (e.g., quality checks, retry limits).
    """
    # Check if a custom signal was set in state by a node
    next_step = state.get("next_step", "")
    if next_step == "error":
        return END
    if next_step == "retry":
        return "researcher"

    return END

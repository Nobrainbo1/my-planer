"""
state.py — Single Source of Truth for graph state.

This is the FIRST file to write. Every other file imports from here.

AgentState is a TypedDict that defines every piece of data that flows
through the graph. Nodes receive the full state and return a PARTIAL
update (only the keys they changed).

Design rules:
- Add a key for every piece of data that agents need to share.
- Use `Annotated[list[X], add_messages]` for chat history (auto-appends).
- Use `Annotated[list[X], operator.add]` for other lists that accumulate.
- Plain types (str, int, dict) get overwritten on each update.
"""
import operator
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """
    The graph's shared state. All nodes read from and write to this.

    Replace / extend these fields to match your project's needs.
    """
    # Chat history — the add_messages reducer automatically appends
    # new messages instead of overwriting the list.
    messages: Annotated[list[BaseMessage], add_messages]

    # Accumulated documents / research results
    documents: Annotated[list[str], operator.add]

    # The topic or query being processed
    topic: str

    # A signal for routing decisions (e.g., "continue", "done", "error")
    next_step: str

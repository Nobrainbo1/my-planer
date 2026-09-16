"""
nodes.py — Node functions (business logic).

Each function is a graph node. Nodes:
- Receive the full AgentState as input.
- Return a PARTIAL state update (only the keys they changed).
- Must never mutate the input state directly.

Import: state (for type hints), prompts (for system prompts), tools (for models).
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from agent.state import AgentState
from agent.prompts import researcher_prompt, writer_prompt
from agent.tools import all_tools


# ──────────────────────────────────────────
# LLM Model Setup
# ──────────────────────────────────────────
# The researcher uses a tool-calling model; the writer does not.
researcher_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
).bind_tools(all_tools)

writer_llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
)


# ──────────────────────────────────────────
# Node Functions
# ──────────────────────────────────────────

def researcher_node(state: AgentState) -> dict:
    """
    Research node — calls the LLM with search tools to gather information.
    Returns partial state update: {"messages": [...new messages...]}
    """
    chain = researcher_prompt | researcher_llm
    response = chain.invoke({
        "messages": state["messages"],
    })
    return {"messages": [response]}


def writer_node(state: AgentState) -> dict:
    """
    Writer node — transforms accumulated documents into a final report.
    Returns partial state update: {"messages": [...new messages...]}
    """
    chain = writer_prompt | writer_llm
    response = chain.invoke({
        "documents": "\n\n---\n\n".join(state.get("documents", [])),
        "topic": state.get("topic", "the given topic"),
    })
    return {"messages": [response]}

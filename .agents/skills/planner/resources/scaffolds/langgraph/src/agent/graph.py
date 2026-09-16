"""
graph.py — Graph assembly and compilation.

This is the LAST file to write. It imports from all other modules
and wires them into a compiled StateGraph.

The exported `graph` object is referenced by langgraph.json for
serving via the LangGraph Platform / dev server.
"""
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from agent.state import AgentState
from agent.nodes import researcher_node, writer_node
from agent.edges import should_researcher_continue
from agent.tools import all_tools


def build_graph() -> StateGraph:
    """
    Assembles and compiles the agent graph.

    Graph flow:
      START → researcher → [tools → researcher (loop)] → writer → END

    The researcher loops through tool calls until it has enough information,
    then routes to the writer for final report generation.
    """
    workflow = StateGraph(AgentState)

    # ── Add Nodes ──────────────────────────────────────────────────────────
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("tools", ToolNode(all_tools))   # Pre-built tool executor
    workflow.add_node("writer", writer_node)

    # ── Add Edges ──────────────────────────────────────────────────────────
    # Entry point
    workflow.add_edge(START, "researcher")

    # After researcher: either call tools or move to writer
    workflow.add_conditional_edges(
        "researcher",
        should_researcher_continue,
        {
            "tools": "tools",    # Route to tool execution
            "writer": "writer",  # Route to final writing
        },
    )

    # After tools: always loop back to researcher
    workflow.add_edge("tools", "researcher")

    # After writer: done
    workflow.add_edge("writer", END)

    return workflow.compile()
    # To add persistence/checkpointing:
    # from langgraph.checkpoint.sqlite import SqliteSaver
    # memory = SqliteSaver.from_conn_string(":memory:")
    # return workflow.compile(checkpointer=memory)


# Compile the graph on import.
# langgraph.json points to this variable: "./src/agent/graph.py:graph"
graph = build_graph()

# LangGraph Scaffold

## When to Use This Framework

Choose **LangGraph** when your project needs:
- **Complex conditional logic** — agents that branch, loop, or retry based on state
- **Strict state management** — you need to track exactly what has happened at every step
- **Tool-calling agents with feedback loops** — e.g., an agent that calls tools, checks results, and decides whether to call more tools or stop
- **Multi-agent systems with dynamic routing** — e.g., a supervisor that routes work to specialist subgraphs
- **Long-running processes** — with checkpointing/persistence between runs

**Don't use LangGraph if** your workflow is simple and sequential with clear roles — use CrewAI instead.

---

## File Structure (SIDE Pattern)

```
your_project/
├── src/
│   └── agent/
│       ├── __init__.py
│       ├── state.py         # S — State: TypedDict schemas (single source of truth)
│       ├── prompts.py       # I — Instructions: system prompts and templates
│       ├── edges.py         # D — Decisions: conditional routing functions
│       ├── nodes.py         # E — Execution: node functions (business logic)
│       ├── tools.py         # Tool definitions (@tool decorated functions)
│       └── graph.py         # Graph assembly, wiring, and compilation
├── main.py                  # Entry point
├── langgraph.json           # LangGraph Platform config (entry points)
├── .env                     # API keys — never commit this
├── .env.example
└── requirements.txt
```

---

## How the Files Wire Together

```
state.py ──────────────────────────────────────────► (imported by all)
tools.py ────────────────────────────────────────┐
prompts.py ──────────────────────────────────┐   │
nodes.py  (imports state, prompts, tools) ───┤   │
edges.py  (imports state)                ────┤   │
                                             ▼   ▼
                                          graph.py  (imports all above)
                                             │
                                          main.py  (imports compiled graph)
```

**Key rule:** State flows through everything. Nodes receive state, return partial updates. Edges read state, return the name of the next node.

---

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env template and fill in your API keys
cp .env.example .env

# Run locally
python main.py

# Run with LangGraph dev server (hot reload)
pip install "langgraph-cli[inmem]"
langgraph dev
```

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **Start with state** — define `AgentState` in `state.py` first. Everything else depends on it.
2. **Nodes return partial updates** — never mutate state in-place; always return a dict with only the changed keys.
3. **Use `add_messages` reducer** for chat history — `Annotated[list[BaseMessage], add_messages]`.
4. **Keep routing logic in `edges.py`** — never put `if/else` routing inside node functions.
5. **Compile once in `graph.py`** — export the compiled `graph` object; `langgraph.json` points to it.
6. **For multi-agent systems** — each agent is its own subgraph in its own folder, imported as a node in the parent `graph.py`.

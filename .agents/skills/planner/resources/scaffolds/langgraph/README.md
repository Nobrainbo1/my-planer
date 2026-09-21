# LangGraph Scaffold

> **Adaptation only — not a validated runnable starter.** This is a reference for an approved target project, not a working quickstart. Static inspection found startup, research handoff, and file-access safety gaps. No compatible dependency set or passing runtime tests are established. This documentation update does not repair the code.

## When to Use This Framework

Choose **LangGraph** when your project needs:
- **Complex conditional logic** — agents that branch, loop, or retry based on state
- **Strict state management** — you need to track exactly what has happened at every step
- **Tool-calling agents with feedback loops** — e.g., an agent that calls tools, checks results, and decides whether to call more tools or stop
- **Multi-agent systems with dynamic routing** — e.g., a supervisor that routes work to specialist subgraphs
- **Long-running processes** — the framework supports checkpointing and persistence when configured; this scaffold's local script does not configure them

For a simple sequential workflow, consider a smaller chain or CrewAI if distinct roles are useful. Framework capabilities are not implemented features of this scaffold.

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

`nodes.py` uses state types, prompts, and tools. `edges.py` reads state to choose a route. `graph.py` combines state, nodes, routing, and a tool executor, then exports the compiled graph imported by `main.py` and referenced by `langgraph.json`.

The intended flow is researcher → optional tools → researcher → writer. The current implementation does not transfer the research messages into the writer's document input; see the known gaps below.

**Key rule:** State flows through everything. Nodes receive state, return partial updates. Edges read state, return the name of the next node.

---

## Known Gaps to Repair in the Target Project

- **Startup:** `main.py:10` imports `agent.graph`, but `agent` lives under `src/`. No packaging metadata or local-package installation is supplied. Installing third-party requirements does not make the documented local command import this package from a clean project root. Validate the server's import/dependency setup separately.
- **Local environment loading:** `src/agent/nodes.py:24–32` constructs models during import. The local Python entry point never calls `load_dotenv`. The `.env` setting in `langgraph.json` is for the server route, not ordinary Python execution. Load and validate target-project configuration before model construction.
- **OpenAI only:** The researcher and writer explicitly use OpenAI models. The `.env.example` phrase “choose one” does not configure Anthropic or Google. Alternative providers need approved integration dependencies and code changes.
- **Broken research handoff:** `main.py:21` starts `documents` empty. The researcher and tools update messages, but no implemented node populates documents. `src/agent/nodes.py:58` passes only that empty document collection and the topic to the writer. Research calls therefore do not supply the final report's evidence.
- **Mock research:** `src/agent/tools.py:34` returns placeholder search text while the researcher prompt requests recent facts and citations. The researcher/writer roles, quantum-computing input, and state fields are examples, not completed project requirements. A report is not proof that research occurred.
- **Unsafe default file access:** `src/agent/tools.py:37–55` registers unrestricted `read_file`. It accepts arbitrary paths and reads whole files without a permitted-directory boundary, secret exclusions, size limits, or approval. Tool results enter messages sent to the researcher model. Remove this default capability before live use, or constrain it to explicitly approved data and transfers.
- **Unimplemented local persistence:** `src/agent/graph.py:56` compiles without a checkpointer. The commented SQLite suggestion follows an unconditional return, lacks the separate checkpoint dependency and caller thread configuration, and uses volatile in-memory storage. Simply uncommenting it is not a complete persistence setup. Validate connection lifetime against the selected API. Server-managed persistence is a separate path and is not evidence that this local script resumes across runs.
- **Routing and output:** The tool loop has no explicit application call/cost budget. `should_continue_or_end` and the `next_step` signal are not wired into the active graph. `main.py:32` prints only the first 500 characters of each message, with no separate complete final report. `build_graph` annotates a compiled result as `StateGraph`.
- **Reproducibility and checks:** Requirements contain lower bounds only. There is no lockfile, supported Python declaration, offline test suite, development dependency manifest, or configured lint/typecheck command. The optional CLI and search/checkpoint integrations need separately selected and validated dependencies.

## Approval, Data, Cost, and Output Boundaries

1. Obtain approval of the intent, plan, and target directory before copying or adapting this scaffold. Preserve shipped code originals; make application repairs in the approved target project. See [planner rules](../../../SKILL.md#step-2--choose-mode).
2. Dependency installation needs separate approval, including the optional server CLI. First select a supported Python environment and dependency set for validation, with an isolated environment, exact shell, and working directory. No compatible versions are asserted here.
3. Live execution sends prompts and message history to OpenAI. The researcher uses `gpt-4o-mini`; the writer uses `gpt-4o`. Tool loops can cause repeated paid requests. Obtain explicit paid-call/data-transfer approval and set request/retry/tool-call/cost limits; framework recursion limits are not a spending budget. Mock search does not make execution offline.
4. The default file reader can expose local file contents to remote model calls, terminal output, and enabled traces. Windows network-share paths can also cause network filesystem access. Remove it before a live demo unless scoped access is explicitly approved and enforced.
5. LangSmith tracing settings are commented out, not enabled by the template. Inherited settings can change that. Enabling tracing can send inputs and outputs to a remote service. Local API serving, hosted Studio debugging, and production serving have different prerequisites and data/storage effects. Check the selected CLI's Python, account, authentication, and storage requirements; none are validated here.
6. The displayed `.env` is a target-project setup artifact, not a shipped file. No `.gitignore` is supplied. Exclude credentials before adding real keys. The local script prints truncated output and does not explicitly save a report; truncation is not redaction. Server/checkpoint paths can create persisted state or other artifacts and require approved storage locations, retention, and collision handling.

Workflow instructions do not enforce runtime permissions inside this Python application. No human approval interrupt is configured. Do not treat this graph as an implementation of the surrounding approval policies.

## Existing Commands — Illustrative, Not a Working Quickstart

These commands are retained for orientation only. They have not been validated and must not be run as a sequence against the shipped scaffold. The approved target-project plan must repair setup, state the exact shell/cwd, and replace these examples with verified instructions. `cp` is shell-dependent.

| Existing example | Purpose and restriction |
|------------------|-------------------------|
| `pip install -r requirements.txt` | Installs third-party dependencies; needs install approval and does not install the local package. |
| `cp .env.example .env` | Creates a credential file; review destination, ignore rules, and any existing file first. Local Python execution does not currently load it. |
| `python main.py` | Intended live run; import, environment, data-flow, and file-access gaps must be repaired first. |
| `pip install "langgraph-cli[inmem]"` | Separate unpinned CLI installation; needs approval and version-specific prerequisite review. |
| `langgraph dev` | Starts a development server, not an offline test. Validate configuration, account/network behavior, and storage separately. |
| `langgraph up` | Mentioned in the entry-point docstring; serving/infrastructure operation, not a test or a validated production recipe. Requires separate authorization and prerequisite review. |

## Offline-Test-First Acceptance Checklist

All items below are target-project acceptance work, not completed checks. No test, lint, typecheck, or compatible-version claim is made here.

- [ ] Record the approved target directory, Python/dependency baseline, isolated environment, shell/cwd, and exact verification commands from the target project's actual configuration. Obtain separate install permission if tools are missing.
- [ ] Configure offline tests with fake model/tool responses, no real credentials, blocked network access, tracing disabled, and isolated approved output locations. Ensure graph imports do not require live credentials.
- [ ] Verify package discovery and configuration loading for local execution. Treat server setup as a separate acceptance path, not a substitute for local validation.
- [ ] Assert that a known research fixture reaches the writer prompt, that missing evidence cannot yield an accepted research report, and that the complete final result is available.
- [ ] Remove or constrain the file reader. Test denied access outside approved data, secret exclusions, size limits, and the absence of unapproved transfers. Do not use real private files as fixtures.
- [ ] Verify tool/no-tool routing, bounded repeated calls, error handling, meaningful failure exits, and approved output/retention behavior.
- [ ] If persistence or human approval is required, implement and test thread identity, storage lifetime, resume behavior, and approval boundaries. Otherwise document those features as absent.
- [ ] Run and record configured offline tests, lint, typecheck, and other required gates only when authorized. Missing commands or execution evidence remain blocked or not run. See [Phase 2 planning rules](../../../references/02_PLANNING.md).
- [ ] Request separate approval for live provider calls, remote tracing, or server/infrastructure checks after offline acceptance. Record observed results and side effects; an offline pass does not prove live integration.

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **Start with state** — define `AgentState` in `state.py` first. Everything else depends on it.
2. **Nodes return partial updates** — never mutate state in-place; always return a dict with only the changed keys.
3. **Use `add_messages` reducer** for chat history — `Annotated[list[BaseMessage], add_messages]`.
4. **Keep routing logic in `edges.py`** — never put `if/else` routing inside node functions.
5. **Compile once in `graph.py`** — export the compiled `graph` object; `langgraph.json` points to it.
6. **For multi-agent systems** — each agent is its own subgraph in its own folder, imported as a node in the parent `graph.py`.

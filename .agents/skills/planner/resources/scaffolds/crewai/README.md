# CrewAI Scaffold

## When to Use This Framework

Choose **CrewAI** when your project needs:
- **Multiple specialized AI agents** working together as a "crew" (e.g., a researcher + a writer + an editor)
- **Role-based orchestration** where each agent has a clear responsibility
- **Sequential or hierarchical task flows** (Task A must complete before Task B)
- **Simple-to-moderate complexity** — no complex looping logic or state machines

**Don't use CrewAI if** your workflow requires agents to loop back, retry based on conditional state, or manage complex branching logic — use LangGraph instead.

---

## File Structure

```
your_project/
├── src/
│   └── your_project/
│       ├── __init__.py
│       ├── main.py              # CLI entry point (run, train, test)
│       ├── crew.py              # @CrewBase class — wires everything together
│       ├── config/
│       │   ├── agents.yaml      # Agent definitions (role, goal, backstory)
│       │   └── tasks.yaml       # Task definitions (description, expected_output)
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py   # Project-specific custom tools
├── .env                         # API keys — never commit this
├── .env.example                 # Committed — shows required keys
└── requirements.txt
```

---

## How the Files Wire Together

```
agents.yaml ──┐
              ├──► crew.py (@CrewBase) ──► main.py (kickoff)
tasks.yaml ───┘         │
                    tools/*.py (injected into agents)
```

1. `crew.py` loads `config/agents.yaml` and `config/tasks.yaml` automatically via `@CrewBase`.
2. Each `@agent` method instantiates an `Agent` with optional tool injection from `tools/`.
3. Each `@task` method instantiates a `Task` referencing its agent.
4. The `@crew` method assembles all agents and tasks into a `Crew` and sets the process.
5. `main.py` calls `YourProjectCrew().crew().kickoff(inputs={...})`.

---

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env template and fill in your API keys
cp .env.example .env

# Run the crew
python -m your_project.main

# Or using CrewAI CLI (if installed with crewai package)
crewai run
```

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **One agent per role** — never combine responsibilities into a single agent.
2. **Define agents in YAML** — role, goal, and backstory go in `agents.yaml`; tool injection happens in `crew.py`.
3. **Tasks flow from input to output** — each task takes the prior task's output as context using `context:` in `tasks.yaml`.
4. **Custom tools go in `tools/`** — one file per tool class.
5. **Use `Process.sequential`** by default; only use `Process.hierarchical` if agents need to delegate.

# CrewAI Scaffold

> **Adaptation only — not a validated runnable starter.** This is a reference for an approved target project, not a working quickstart. Static inspection found startup, CLI, and research gaps. No compatible dependency set or passing runtime tests are established. This documentation update does not repair the code.

## When to Use This Framework

Choose **CrewAI** when your project needs:
- **Multiple specialized AI agents** working together as a "crew" (e.g., a researcher + a writer + an editor)
- **Role-based orchestration** where each agent has a clear responsibility
- **Sequential or hierarchical task flows** (Task A must complete before Task B)
- **Simple-to-moderate complexity** — no complex looping logic or state machines

For explicit state-driven loops and complex branching, compare LangGraph. This scaffold demonstrates only sequential coordination; framework capabilities and alternative processes require separate implementation and validation.

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

## Known Gaps to Repair in the Target Project

- **Startup:** `src/your_project/main.py:11` imports a package under `src/`, but no packaging metadata or local-package installation is provided. Installing `requirements.txt` alone does not make `python -m your_project.main` work from a clean project root. The `crewai run` alternative also lacks project metadata and script configuration.
- **Tool API compatibility:** `src/your_project/tools/custom_tool.py:13` imports `BaseTool` from `crewai_tools`; current official examples use `crewai.tools`. Verify the import against the selected release; the open-ended requirements do not establish compatibility.
- **Broken train/test arguments:** `src/your_project/main.py:33` and `:48` convert `sys.argv[1]` to an integer, although dispatch uses that argument for `train` or `test`. Supplying an additional iteration count does not repair this. Unknown commands do not explicitly return a failure exit status.
- **Mock research, real model:** `src/your_project/tools/custom_tool.py:38` returns mock text, but `src/your_project/config/tasks.yaml:24–29` requires five sources and cited findings. The researcher and reporting analyst are generic example roles, not an implemented project contract. Generated citations are not evidence of actual research.
- **Provider setup:** OpenAI is the only intended default provider path; agents leave model selection to framework defaults. No alternative provider is configured. The `.env.example` phrase “choose one” does not implement switching. Select the provider/model explicitly and verify environment loading before model construction rather than relying on framework defaults.
- **Reproducibility and checks:** Requirements contain lower bounds only. There is no lockfile, supported Python declaration, offline test suite, development dependency manifest, or configured lint/typecheck command. The commented search integration needs its own approved dependency and missing `os` import.

## Approval, Data, Cost, and Output Boundaries

1. Obtain approval of the intent, plan, and target directory before copying or adapting this scaffold. Preserve shipped code originals; make application repairs in the approved target project. See [planner rules](../../../SKILL.md#step-2--choose-mode).
2. Dependency installation needs separate approval. First select a supported Python environment and dependency set for validation, with an isolated environment, exact shell, and working directory. No compatible versions are asserted here.
3. OpenAI model calls require credentials, network access, and explicit approval for paid execution. Kickoff can make multiple calls. CrewAI `test` is repeated live execution and model evaluation, not an offline unit suite; training can also repeat billable work. Do not repair the CLI and then treat these operations as free checks.
4. Current CrewAI documentation describes default usage telemetry, including role and tool names. The researcher role includes the input topic. Review version-specific telemetry and tracing controls, including inherited user preferences, before execution; keep additional tracing opt-in. Mock search does not make the application offline.
5. The displayed `.env` is a target-project setup artifact, not a shipped file. No `.gitignore` is supplied. Exclude credentials and sensitive artifacts from version control before adding real keys. Verbose agents and final-result printing can reveal input and output data; truncation or verbosity settings are not redaction.
6. `src/your_project/config/tasks.yaml:54` configures a relative `report.md` write. Training targets `training_data.pkl`. Approve output locations and collision handling before execution; repeat runs may replace outputs. Framework-managed artifacts also depend on the selected release. Never load untrusted pickle data.

Workflow instructions do not enforce runtime permissions inside this Python application. Define approved data access and call/retry/cost limits in the target project.

## Existing Commands — Illustrative, Not a Working Quickstart

These commands are retained for orientation only. They have not been validated and must not be run as a sequence against the shipped scaffold. The approved target-project plan must repair setup, state the exact shell/cwd, and replace these examples with verified instructions. `cp` is shell-dependent.

| Existing example | Purpose and restriction |
|------------------|-------------------------|
| `pip install -r requirements.txt` | Installs third-party dependencies; needs install approval and does not install the local package. |
| `cp .env.example .env` | Creates a credential file; review destination, ignore rules, and any existing file first. |
| `python -m your_project.main` | Intended live run; package discovery and tool import must be repaired first. |
| `crewai run` | Intended CLI alternative; project metadata and script setup are missing. |
| `python -m your_project.main train` | Documented in the entry point; argument parsing is broken and training is not an offline check. |
| `python -m your_project.main test` | Documented in the entry point; argument parsing is broken and this is live evaluation, not unit testing. |

## Offline-Test-First Acceptance Checklist

All items below are target-project acceptance work, not completed checks. No test, lint, typecheck, or compatible-version claim is made here.

- [ ] Record the approved target directory, Python/dependency baseline, isolated environment, shell/cwd, and exact verification commands from the target project's actual configuration. Obtain separate install permission if tools are missing.
- [ ] Configure offline tests with fake model responses, no real credentials, blocked network access, telemetry disabled, and isolated approved output locations. Ensure imports do not require live credentials.
- [ ] Verify package discovery, tool imports, YAML agent/task/context wiring, valid and invalid CLI arguments, and meaningful failure exit statuses.
- [ ] Replace placeholder roles and mock research with approved behavior or clearly labelled fixtures. Assert that research evidence reaches the report and that missing sources cannot masquerade as successful research.
- [ ] Verify output collision protection, credential exclusion, redaction, and bounded execution. Record artifact locations and observed side effects.
- [ ] Run and record configured offline tests, lint, typecheck, and other required gates only when authorized. Missing commands or execution evidence remain blocked or not run. See [Phase 2 planning rules](../../../references/02_PLANNING.md).
- [ ] Request separate approval for any live provider evaluation after offline acceptance. Record observed results and cost/data boundaries; an offline pass does not prove live integration.

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **Use only needed roles** — retain distinct agents where the approved requirements justify them; generic personas are not acceptance criteria.
2. **Define agents in YAML** — role, goal, and backstory go in `agents.yaml`; tool injection happens in `crew.py`.
3. **Tasks flow from input to output** — each task takes the prior task's output as context using `context:` in `tasks.yaml`.
4. **Custom tools go in `tools/`** — one file per tool class.
5. **Use `Process.sequential`** by default; only use `Process.hierarchical` if agents need to delegate.

# LangChain Scaffold

> **Adaptation only — not a validated runnable starter.** This is a reference for an approved target project, not a working quickstart. Static inspection found setup and optional-tool safety gaps. No compatible dependency set or passing runtime tests are established. This documentation update does not repair the code.

## When to Use This Framework

Choose **LangChain (LCEL)** when your project needs:
- **A single chain of operations** — prompt → LLM → parse output (e.g., "summarize this document")
- **Optional tool integration** — requires an explicit tool executor; the shipped analysis chain does not execute tools
- **Rapid prototyping** — getting something working quickly before committing to CrewAI or LangGraph
- **LLM-powered functions** — embedding an LLM call inside a larger traditional application

**Upgrade to CrewAI** if you need multiple agents with distinct roles.  
**Upgrade to LangGraph** if you need conditional branching, loops, or persistent state.

---

## File Structure

```
your_project/
├── src/
│   ├── __init__.py
│   ├── config.py            # LLM model setup, environment loading
│   ├── prompts.py           # PromptTemplate / ChatPromptTemplate definitions
│   ├── tools.py             # @tool decorated functions
│   ├── output_parsers.py    # Pydantic output schemas, parser definitions
│   └── chain.py             # LCEL chain assembly (the pipeline)
├── main.py                  # Entry point
├── .env                     # API keys — never commit this
├── .env.example
└── requirements.txt
```

---

## How the Files Wire Together

`chain.py` imports models from `config.py`, templates from `prompts.py`, and schemas from `output_parsers.py`. It assembles analysis and summarization chains using structured model output. `main.py` invokes only the analysis example by default.

**LCEL pipe syntax:** Each `|` passes the left component's output to the right component. `bind_tools` supplies tool schemas to a model; it does not execute requested tools or return their results. A separate executor and response-handling flow are required. `tools.py` is not imported by the active chains; its integration example is commented out.

---

## Known Gaps to Repair in the Target Project

- **Working-directory dependence:** `main.py:5` adds the relative path `src` to imports. That path follows the current working directory, not the script location. There is no package-install setup. Define a reliable entry point and exact working directory.
- **OpenAI only:** `src/config.py:17–27` creates OpenAI clients during import. The `.env.example` phrase “choose one” does not switch providers. Commented Anthropic and Google alternatives need undeclared integration packages; replacing only `default_llm` leaves `reasoning_llm` constructing an OpenAI client. Instantiate only the selected models and validate environment loading before client construction.
- **Optional tools are not an implemented default feature:** `src/chain.py:38–43` contains only a commented tool-agent example and imports `langgraph`, which is not declared in this scaffold's requirements. Tool binding alone does not execute tools.
- **Unsafe optional calculator:** `src/tools.py:32–46` calls `eval` despite its “Safely evaluate” description. Empty builtins do not provide a sandbox or resource limits. This tool is not active in the default chain. Remove it or use an approved arithmetic-only implementation before enabling tools; the suggested parser dependency is not declared.
- **Mock search:** `src/tools.py:29` returns placeholder text. Its commented HTTP implementation needs an approved dependency and missing `os` import. No search runs in the default analysis chain.
- **Example contracts:** The analyst prompt, example input, and output schemas are generic. Adapt them to approved requirements and validate malformed, missing, or refused model output. Temperature zero reduces sampling variability; it does not guarantee deterministic answers.
- **Reproducibility and checks:** Requirements contain lower bounds only. There is no lockfile, supported Python declaration, offline test suite, development dependency manifest, or configured lint/typecheck command. Compatible framework and structured-output behavior are not established.

## Approval, Data, Cost, and Output Boundaries

1. Obtain approval of the intent, plan, and target directory before copying or adapting this scaffold. Preserve shipped code originals; make application repairs in the approved target project. See [planner execution rules](../../../SKILL.md#step-4a--execute-mode-a).
2. Dependency installation needs separate approval. First select a supported Python environment and dependency set for validation, with an isolated environment, exact shell, and working directory. No compatible versions are asserted here.
3. The default example sends its analysis prompt/input to OpenAI when invoked. This needs credentials, network access, and explicit approval for paid execution. The summarization invocation is commented out; the separate reasoning client is constructed but not invoked by the default demo. Client construction is not evidence of a completed model call.
4. LangSmith tracing settings are commented out, not enabled by the template. Enabling tracing, or inheriting enabled environment settings, can send inputs and outputs to a remote tracing service. Review destinations and data consent before execution; keep tracing opt-in.
5. The displayed `.env` is a target-project setup artifact, not a shipped file. No `.gitignore` is supplied. Exclude credentials before adding real keys. The default script prints its analysis result; it does not explicitly save a report. Terminal logs and optional traces can still retain sensitive output.
6. Before enabling optional tools, approve their dependencies, data access, network destinations, and effects. Set explicit request/retry/cost limits and replace unsafe or mock implementations. Installing packages is not approval to invoke a live model or tool.

Workflow instructions do not enforce runtime permissions inside this Python application. No offline demonstration mode is currently provided.

## Existing Commands — Illustrative, Not a Working Quickstart

These commands are retained for orientation only. They have not been validated and must not be run as a sequence against the shipped scaffold. The approved target-project plan must repair setup, state the exact shell/cwd, and replace these examples with verified instructions. `cp` is shell-dependent.

| Existing example | Purpose and restriction |
|------------------|-------------------------|
| `pip install -r requirements.txt` | Installs third-party dependencies; needs install approval and a selected environment. |
| `cp .env.example .env` | Creates a credential file; review destination, ignore rules, and any existing file first. |
| `python main.py` | Intended live OpenAI demonstration, not a test. Requires repaired/validated setup and paid-call approval. |

## Offline-Test-First Acceptance Checklist

All items below are target-project acceptance work, not completed checks. No test, lint, typecheck, or compatible-version claim is made here.

- [ ] Record the approved target directory, Python/dependency baseline, isolated environment, shell/cwd, and exact verification commands from the target project's actual configuration. Obtain separate install permission if tools are missing.
- [ ] Configure offline tests with fake model responses, no real credentials, blocked network access, and tracing disabled. Ensure imports and model selection can be tested without live clients.
- [ ] Verify entry-point imports, environment selection, prompt inputs, structured-output validation, model refusal/error handling, and meaningful failure exits.
- [ ] Replace generic prompts and schemas with approved contracts. Assert correct handling of valid and invalid fake responses instead of expecting identical live output at temperature zero.
- [ ] If tools are required, verify actual tool dispatch separately from binding, reject unsafe calculation inputs, and label search fixtures honestly. Keep unapproved tools disabled.
- [ ] Verify credential exclusion, output redaction/retention, no unexpected file writes or network calls, and bounded execution.
- [ ] Run and record configured offline tests, lint, typecheck, and other required gates only when authorized. Missing commands or execution evidence remain blocked or not run. See [verification rules](../../../references/05_VERIFICATION.md).
- [ ] Request separate approval for any live provider evaluation after offline acceptance. Record observed results and cost/data boundaries; an offline pass does not prove live integration.

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **Define the LLM in `config.py`** — one place to swap models or adjust temperature.
2. **Keep prompts in `prompts.py`** — never hardcode prompt strings inside `chain.py`.
3. **Use Pydantic models in `output_parsers.py`** for structured output — more reliable than string parsing.
4. **Tools are optional** — only add `tools.py` if the chain needs to call external functions.
5. **`chain.py` is the integration point** — it wires models, prompts, and schemas. Add tool execution only when required and approved.

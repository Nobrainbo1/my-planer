# LangChain Scaffold

## When to Use This Framework

Choose **LangChain (LCEL)** when your project needs:
- **A single chain of operations** — prompt → LLM → parse output (e.g., "summarize this document")
- **Simple tool use** — one agent calling a fixed set of tools, no complex loops
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

```
config.py ──────────────────────────────────────┐
prompts.py ─────────────────────────────────┐   │
tools.py ───────────────────────────────┐   │   │
output_parsers.py ──────────────────┐   │   │   │
                                    ▼   ▼   ▼   ▼
                                    chain.py  (LCEL pipe: prompt | llm | parser)
                                        │
                                    main.py  (invokes chain)
```

**LCEL pipe syntax:** `chain = prompt | llm.bind_tools(tools) | parser` — each `|` passes output of the left as input to the right.

---

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env template and fill in your API keys
cp .env.example .env

# Run the chain
python main.py
```

---

## Key Design Decisions for Mode A Generation

When generating a project from an Intent Brief:
1. **Define the LLM in `config.py`** — one place to swap models or adjust temperature.
2. **Keep prompts in `prompts.py`** — never hardcode prompt strings inside `chain.py`.
3. **Use Pydantic models in `output_parsers.py`** for structured output — more reliable than string parsing.
4. **Tools are optional** — only add `tools.py` if the chain needs to call external functions.
5. **`chain.py` is the integration point** — it imports from all other modules and wires the LCEL pipeline.

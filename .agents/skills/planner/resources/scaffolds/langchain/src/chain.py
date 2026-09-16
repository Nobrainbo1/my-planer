"""
chain.py — LCEL chain assembly (the integration layer).

This file imports from all other modules and wires them together
using LangChain Expression Language (LCEL) pipe syntax.

LCEL pipe syntax: chain = prompt | llm | parser
Each `|` passes the output of the left component as input to the right.

This is the only file that should import from config.py, prompts.py,
output_parsers.py, and tools.py — it is the integration point.
"""
from config import default_llm
from prompts import main_prompt, summarize_prompt
from output_parsers import AnalysisResult, DocumentSummary

# ──────────────────────────────────────────
# Chain 1: Main Analysis Chain (Structured Output)
# Input:  {"input": "your question or text here"}
# Output: AnalysisResult (Pydantic model)
# ──────────────────────────────────────────
analysis_chain = (
    main_prompt
    | default_llm.with_structured_output(AnalysisResult)
)

# ──────────────────────────────────────────
# Chain 2: Summarization Chain (Structured Output)
# Input:  {"text": "long document text here"}
# Output: DocumentSummary (Pydantic model)
# ──────────────────────────────────────────
summarize_chain = (
    summarize_prompt
    | default_llm.with_structured_output(DocumentSummary)
)

# ──────────────────────────────────────────
# Chain with Tools (Optional)
# Uncomment if your chain needs to call tools.
# ──────────────────────────────────────────
# from tools import all_tools
# from langgraph.prebuilt import create_react_agent
# agent_chain = create_react_agent(default_llm, all_tools)

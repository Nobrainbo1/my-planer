"""
prompts.py — All system prompts and prompt templates in one place.

Never hardcode prompt strings inside node functions.
Keep them here so they are easy to version, review, and iterate on.
"""
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

# ──────────────────────────────────────────
# System Prompts (plain strings)
# ──────────────────────────────────────────

RESEARCHER_SYSTEM_PROMPT = """You are a senior research analyst with deep expertise in synthesizing 
complex information from multiple sources. Your goal is to find accurate, 
recent, and relevant information about the topic you are given.

When you need more information, use your available search tools.
When you have enough information, summarize your findings clearly and concisely.
Always cite your sources."""

WRITER_SYSTEM_PROMPT = """You are a professional technical writer. Your goal is to transform 
raw research findings into a clear, well-structured, and actionable report.

Structure your output with clear headings, bullet points where appropriate,
and a concise executive summary at the top."""

# ──────────────────────────────────────────
# Chat Prompt Templates (for use with LangChain runnables)
# ──────────────────────────────────────────

researcher_prompt = ChatPromptTemplate.from_messages([
    ("system", RESEARCHER_SYSTEM_PROMPT),
    ("placeholder", "{messages}"),
])

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", WRITER_SYSTEM_PROMPT),
    ("human", "Here is the research to write about:\n\n{documents}\n\nTopic: {topic}"),
])

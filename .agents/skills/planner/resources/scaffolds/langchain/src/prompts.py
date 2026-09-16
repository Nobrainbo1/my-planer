"""
prompts.py — All prompt templates for the chain.

Never write prompt strings directly in chain.py.
Keep them here so they are easy to iterate on and version-control.
"""
from langchain_core.prompts import ChatPromptTemplate

# ──────────────────────────────────────────
# Main chain prompt
# Replace this with your actual task's prompt.
# ──────────────────────────────────────────
main_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional analyst. Your task is to process the user's 
input and provide a well-structured, accurate, and concise response.

Format your output as requested by the user.
If you are unsure about any detail, state it clearly rather than guessing.""",
    ),
    ("human", "{input}"),
])

# ──────────────────────────────────────────
# Summarization prompt (example of a second prompt)
# ──────────────────────────────────────────
summarize_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert at summarizing content. Produce a clear, "
        "bullet-pointed summary of the provided text. "
        "Focus on the most important points."
    ),
    ("human", "Please summarize the following:\n\n{text}"),
])

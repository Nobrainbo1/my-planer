"""
output_parsers.py — Structured output schemas and parsers.

Use Pydantic models to enforce a specific output structure from the LLM.
This is more reliable than asking the LLM to "output JSON" in the prompt.

Usage in chain.py:
    from output_parsers import AnalysisResult
    chain = prompt | llm.with_structured_output(AnalysisResult)
"""
from pydantic import BaseModel, Field
from typing import List


class AnalysisResult(BaseModel):
    """
    Structured output schema for the main analysis chain.
    Replace these fields with what your project actually needs.
    """
    summary: str = Field(description="A 1-2 sentence summary of the findings.")
    key_points: List[str] = Field(description="A list of the 3-5 most important findings.")
    confidence: str = Field(
        description="Confidence level in the analysis: 'high', 'medium', or 'low'.",
        pattern="^(high|medium|low)$",
    )
    recommendations: List[str] = Field(
        description="A list of concrete, actionable next steps based on the analysis."
    )


class DocumentSummary(BaseModel):
    """Schema for document summarization output."""
    title: str = Field(description="A short title for the document.")
    summary: str = Field(description="A concise 2-3 sentence summary.")
    topics: List[str] = Field(description="The main topics covered in the document.")

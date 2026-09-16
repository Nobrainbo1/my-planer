"""
main.py — Entry point for the LangChain application.
"""
import sys
sys.path.insert(0, "src")  # Allow imports from src/ without installing the package

from chain import analysis_chain, summarize_chain


def main():
    print("Running LangChain pipeline...\n")

    # ── Example 1: Run the analysis chain ──────────────────────────────────
    result = analysis_chain.invoke({
        "input": "What are the main benefits and risks of using AI agents in software development?"
    })
    print("── Analysis Result ──")
    print(f"Summary: {result.summary}")
    print(f"Confidence: {result.confidence}")
    print("Key Points:")
    for point in result.key_points:
        print(f"  - {point}")
    print("Recommendations:")
    for rec in result.recommendations:
        print(f"  • {rec}")

    # ── Example 2: Run the summarization chain ─────────────────────────────
    # doc = summarize_chain.invoke({"text": "Your long document text here..."})
    # print(f"\nSummary: {doc.summary}")


if __name__ == "__main__":
    main()

"""
main.py — Entry point for running the graph locally.

For development with hot reload, use:
    langgraph dev

For production serving, configure langgraph.json and use:
    langgraph up
"""
from agent.graph import graph


def main():
    print("Starting agent graph...\n")

    # Initial state — only provide the keys required to start the graph.
    # The rest of the state is populated by nodes as the graph runs.
    initial_state = {
        "messages": [("user", "Research the latest advances in quantum computing.")],
        "topic": "quantum computing",
        "documents": [],
        "next_step": "",
    }

    # Stream mode shows each node's output as it runs.
    for step in graph.stream(initial_state, stream_mode="updates"):
        node_name = list(step.keys())[0]
        print(f"\n── Node: {node_name} ──")
        output = step[node_name]
        if "messages" in output and output["messages"]:
            last_msg = output["messages"][-1]
            print(getattr(last_msg, "content", str(last_msg))[:500])

    print("\n\n── Graph Run Complete ──")


if __name__ == "__main__":
    main()

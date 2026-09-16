#!/usr/bin/env python3
"""
Main entry point for the crew.

Usage:
    python -m your_project.main         # Run the crew
    python -m your_project.main train   # Train the crew
    python -m your_project.main test    # Test the crew
"""
import sys
from your_project.crew import YourProjectCrew


def run():
    """Run the crew with the given inputs."""
    inputs = {
        "topic": "AI Agents in 2025",  # Replace with your project's input variables
    }
    result = YourProjectCrew().crew().kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Crew Run Complete")
    print("########################\n")
    print(result)


def train():
    """Train the crew for a given number of iterations."""
    inputs = {
        "topic": "AI Agents in 2025",
    }
    try:
        YourProjectCrew().crew().train(
            n_iterations=int(sys.argv[1]) if len(sys.argv) > 1 else 3,
            inputs=inputs,
            filename="training_data.pkl",
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def test():
    """Test the crew execution and returns the results."""
    inputs = {
        "topic": "AI Agents in 2025",
    }
    try:
        YourProjectCrew().crew().test(
            n_iterations=int(sys.argv[1]) if len(sys.argv) > 1 else 3,
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "run"
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}. Use 'run', 'train', or 'test'.")

"""
crew.py — The heart of the CrewAI project.

This file uses the @CrewBase decorator to automatically load agent and task
configurations from YAML files and wire them into a Crew.

To add a new agent:
  1. Add its definition to config/agents.yaml
  2. Add an @agent method here that instantiates it

To add a new task:
  1. Add its definition to config/tasks.yaml
  2. Add a @task method here that instantiates it

The @crew method assembles everything into the final Crew object.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Import your custom tools (discovered in Phase 3 / 03_TOOLING.md)
from your_project.tools.custom_tool import ExampleSearchTool


@CrewBase
class YourProjectCrew:
    """Your Project Crew — orchestrates all agents and tasks."""

    # These paths are relative to this file's location.
    # @CrewBase auto-loads them and makes them available as self.agents_config
    # and self.tasks_config dictionaries.
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ──────────────────────────────────────────
    # AGENTS
    # Each @agent method returns a fully configured Agent.
    # The method name MUST match the key in agents.yaml.
    # ──────────────────────────────────────────

    @agent
    def researcher(self) -> Agent:
        """Senior researcher agent — gathers and synthesizes information."""
        return Agent(
            config=self.agents_config["researcher"],
            tools=[ExampleSearchTool()],  # Inject Phase 3 tools here
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Analyst agent — converts research into structured reports."""
        return Agent(
            config=self.agents_config["reporting_analyst"],
            tools=[],  # This agent needs no external tools
            verbose=True,
        )

    # ──────────────────────────────────────────
    # TASKS
    # Each @task method returns a fully configured Task.
    # The method name MUST match the key in tasks.yaml.
    # ──────────────────────────────────────────

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            # output_file is set in tasks.yaml
        )

    # ──────────────────────────────────────────
    # CREW
    # The @crew method assembles agents and tasks.
    # self.agents and self.tasks are auto-gathered from the @agent/@task methods above.
    # ──────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates and returns the assembled Crew."""
        return Crew(
            agents=self.agents,    # Automatically collected from @agent methods
            tasks=self.tasks,      # Automatically collected from @task methods
            process=Process.sequential,
            verbose=True,
            # memory=True,         # Uncomment to enable agent memory
            # embedder={...},      # Uncomment to configure a custom embedder
        )

# IntentFlow (Planner Edition)

**A simple, AI-assisted software planning toolkit.**

Welcome! If you're building software with an AI coding assistant (like ECC, Superpower, Cline, or Cursor), you know that AI works best when it has a clear plan. 

**IntentFlow** helps your AI figure out exactly *what* to build, *why* to build it, and *which tools* to use, **before** writing a single line of code.

---

## 🎯 What this toolkit does

This is a **Planner-Only** toolkit. It acts as the brain behind the operation, focusing entirely on **Phases 1-3** of the software development lifecycle:

1. **Discovery:** Interviews you to understand your goals and constraints.
2. **Planning:** Drafts a step-by-step Execution Plan for your project.
3. **Tooling:** Recommends the best frameworks, libraries, and MCP servers (like `rtk-ai/rtk` for token optimization) to use.

> **💡 The Handoff:** Once the Execution Plan is approved, the Planner's job is done! You then hand that plan over to your execution agent (like ECC) to actually write the code (Phases 4-6).

---

## 🚀 How to Use It

Using IntentFlow is incredibly simple. Just give your AI assistant access to the `.agents/` folder and ask it to start planning!

**Example Prompt to start a project:**

> "Read `.agents/AGENTS.md` and `.agents/skills/planner/SKILL.md`. I want to build a new [insert project idea here]. Act as my Planner. Walk me through the Discovery phase, ask me clarifying questions, and let's draft an Execution Plan."

### The 3 Steps to Success:

1. **Answer Questions:** The AI will ask you a few targeted questions to figure out exactly what you want.
2. **Review the Plan:** The AI will generate an `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md`. Read them over.
3. **Approve & Handoff:** Once you approve the plan, give those markdown files to your execution agent (ECC, Superpower, etc.) and let it start building!

---

## 📁 What's inside the `.agents/` folder?

- `AGENTS.md`: The core rules and boundaries for the AI. It tells the AI to plan and *not* to execute.
- `skills/planner/`: The step-by-step instructions the AI uses to interview you and write the plan.
- `skills/planner/references/`: The deep-dive guides for Phase 1, Phase 2, and Phase 3.
- `skills/planner/resources/templates/`: The blank templates the AI uses to generate your project's markdown files.

---

## 🛑 Important Note on Execution

This main branch is strictly for **Planning**. It deliberately does not contain instructions for writing code, running tests, or deploying. This is to ensure it never conflicts with your external execution scaffolder (like ECC). 

*(If you ever want to explore a monolithic version of this framework that attempts to do everything from planning to deployment internally, check out the `backup-full-framework-idea` branch!)*

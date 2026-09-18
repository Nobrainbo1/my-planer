---
description: "Reference guide for the Handoff Phase. Details how to transition from the Planner to external execution scaffolders like ECC, Superpowers, Cursor, Cline, or OpenHands."
alwaysApply: false
---

# Handoff & Scaffolder Transition Guide

> **Purpose:** When you finish Phase 3 (Tooling), your blueprint (`EXECUTION_PLAN.md`) is approved and your tools are selected. This guide details how to transition governance from the **Planner** to your chosen **Execution Agent / Scaffolder**.

---

## The Transition Lifecycle

```
┌────────────────────────────────────────────────────────┐
│ 1. FINALIZE PLANNING (IntentFlow)                      │
│    • Approved INTENT_BRIEF.md & EXECUTION_PLAN.md      │
│    • Live domain vocabulary in CONTEXT.md              │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. IN-PROJECT TOOL SETUP & CONFLICT RESOLUTION         │
│    • Check port, .env, and dependency conflicts        │
│    • Install rtk-ai/rtk (token & log optimizer)        │
│    • Configure project MCP servers                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. HANDOFF & REPOSITORY REORGANIZATION                 │
│    • Move planner internal references to .planning/    │
│    • Resolve AGENTS.md for the chosen execution tool   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. EXECUTION HANDOFF                                   │
│    • Scaffolder executes tasks from EXECUTION_PLAN.md  │
└────────────────────────────────────────────────────────┘
```

---

## How to Handoff to Specific Scaffolders

### 1. Handoff to Superpowers (`obra/superpowers`)
* **Philosophy:** Rigorous engineering discipline, mandatory TDD (Red-Green-Refactor), subagent reviews.
* **How to transition:**
  1. Install Superpowers in Claude Code / CLI:
     ```bash
     /plugin marketplace add obra/superpowers-marketplace
     /plugin install superpowers@superpowers-marketplace
     ```
  2. Superpowers auto-detects `EXECUTION_PLAN.md` and uses its bite-sized tasks to drive subagents through Red-Green-Refactor cycles.
  3. Archive `.agents/skills/planner/references/` into `.planning/`.

### 2. Handoff to ECC (Everything Claude Code)
* **Philosophy:** Full Agent OS with hundreds of skills, cross-session memory, AgentShield security, and compaction.
* **How to transition:**
  1. Follow ECC's setup instructions to initialize ECC in your workspace.
  2. ECC introduces its own rules and skills. Yield root `AGENTS.md` governance to ECC.
  3. Point ECC to `EXECUTION_PLAN.md` as the target project backlog.

### 3. Handoff to Roo Code (Roo-Cline) / Cline (VS Code)
* **Philosophy:** Role-based autonomous editing inside VS Code with strict user oversight.
* **How to transition:**
  1. Open the project in VS Code.
  2. In Roo Code, switch to **Architect Mode** first to review `EXECUTION_PLAN.md` and `CONTEXT.md`.
  3. Switch to **Code Mode** to implement each task sequentially.
  4. Update `AGENTS.md` to:
     ```markdown
     # Project Rules (Execution Mode)
     You are an Autonomous Coder. Implement tasks from EXECUTION_PLAN.md.
     Do not modify architectural contracts without approval.
     ```

### 4. Handoff to OpenHands (All-Hands-AI)
* **Philosophy:** Docker-sandboxed autonomous developer that runs commands, tests, and web browsing.
* **How to transition:**
  1. Start OpenHands Docker container mounting your project directory.
  2. In the initial prompt, tell OpenHands:
     > *"Read `EXECUTION_PLAN.md` and `CONTEXT.md`. Execute Task 1 through Task N sequentially, running tests in the sandbox for each task before marking it complete."*

### 5. Handoff to Aider
* **Philosophy:** Git-diff terminal pair programmer that makes clean commits.
* **How to transition:**
  1. Launch Aider: `aider --model [your-model]`
  2. Add the plan: `/add EXECUTION_PLAN.md CONTEXT.md`
  3. Prompt: *"Let's implement Task 1 from EXECUTION_PLAN.md. Show the proposed diff and run test commands."*

---

## Workspace Hygiene Checklist

Before starting implementation:
- [ ] **`EXECUTION_PLAN.md` is approved** with exact file paths and test commands.
- [ ] **`rtk-ai/rtk` is installed** to protect the context window from runaway error logs.
- [ ] **`.env.example` is created** with placeholder variables; no secrets in version control.
- [ ] **Planner reference guides are moved to `.planning/`** so the coding agent doesn't read obsolete planning instructions.
- [ ] **`AGENTS.md` reflects Execution Mode** so the coding agent is not blocked by planner restrictions.

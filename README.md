# 💡 IntentFlow — Your AI Architect & Planner

> **Type `/planner` to turn any software idea into a bulletproof blueprint before writing a single line of code.**

---

### 🤔 Why IntentFlow?

Have you ever asked an AI coding tool to "build me an app," only to watch it get confused, hallucinate wrong assumptions, waste your tokens, or produce code that doesn't work?

AI models are brilliant coders, but they perform best when they have a **clear, structured plan** first. 

**IntentFlow** acts as your AI's **System Architect**. Activated by the **`/planner`** command, your AI sits down with you, asks a few friendly questions to clarify your vision, and creates a step-by-step **Blueprint (`EXECUTION_PLAN.md`)**.

---

## 🛠️ How It Works (The 2-Step Workflow)

IntentFlow separates **Thinking** from **Building** so you always stay in control:

```
┌─────────────────────────────────────────────────┐
│  STEP 1: THINK & PLAN  (/planner)               │
│  Your AI acts as an Architect.                  │
│  It interviews you & writes the Blueprint.      │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│  STEP 2: BUILD & EXECUTE (Your AI Coding Tool)  │
│  You hand the approved Blueprint to any AI      │
│  coder (Cursor, Claude Code, Cline, ECC, etc.)  │
└─────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start Guide (How to Use It)

### 1. Make sure `.agents/` is in your project directory.

### 2. Trigger the Planner:

* **⚡ Method A: Slash Command (Fastest & Recommended)**
  Simply type:
  > **`/planner`** *I want to build a [your app idea here]*

* **💬 Method B: Standard Prompt**
  If your AI tool doesn't support slash commands, copy and paste this:
  > *"Read `.agents/AGENTS.md` and `.agents/skills/planner/SKILL.md`. I want to plan a project called [your app idea here]. Act as my Planner: walk me through a few questions to clarify my goals, then help me draft the plan."*

---

## 🪄 What Happens When You Run `/planner`?

1. **Interactive Interview:** The AI uses the `planner` and `grill-with-docs` skills to ask you 1–3 simple questions at a time about your goals, features, and tech stack.
2. **Blueprint Generation:** The AI creates three plain-text files in your project root, powered by **Advanced AI Planning Architectures (ReWOO, Plan-and-Execute, LLMCompiler, Reflexion)**:
   - 📄 **`INTENT_BRIEF.md`** — *What we're building:* Goals, scope, and target features.
   - 📖 **`CONTEXT.md`** — *Vocabulary:* A simple glossary of terms so the AI doesn't mix up concepts.
   - 🗺️ **`EXECUTION_PLAN.md`** — *The Master Blueprint:* A step-by-step roadmap that maps dependencies (DAG), parallelizes tasks, and includes self-correcting feedback loops.
3. **Environment Profiling & Lean Tool Setup (Anti-Bloat):** The AI automatically detects your **Host OS** (Windows, macOS, Linux) and **Active AI Harness** (Antigravity, Claude Code, Cursor, Cline, etc.). It prioritizes tools with verified tutorials for your harness, disqualifies dangerous platform hazards (e.g., native Unix daemons on Windows or unverified harness hooks), enforces a strict **Anti-Bloat Tool Budget** (≤ 3–5 active tools), prioritizes token-efficient [AXI CLIs](https://axi.md/) over heavy MCP servers, and installs required tools (like `rtk-ai/rtk`) directly in your project upon your approval.
4. **Clean Transition & Handoff:** The AI archives internal planner guides into `.planning/` and transitions `AGENTS.md` to authorize execution, leaving your project completely ready for your AI coding tool (Cursor, Cline, Claude Code, ECC, Superpowers, Firstmate, etc.) to build!

---

## 📁 What's Inside the Toolkit?

If you inspect the `.agents/` folder, here is what powers the `/planner`:

- 📜 **`AGENTS.md`**: The core rules for the AI. It instructs the AI to listen to you, ask questions, enforce lean tooling, and focus strictly on planning.
- 🧰 **`skills/planner/SKILL.md`**: The main `/planner` skill that orchestrates discovery, architecture decisions, anti-bloat advice, and task breakdowns.
- 🔍 **`skills/grill-with-docs/SKILL.md`**: The interview skill the AI uses to ask targeted decision questions without overwhelming you.
- 📚 **`skills/planner/references/`**: Detailed guides on project discovery, architecture decisions, AXI vs MCP comparisons, and discovering battle-tested tools/libraries.

---

## 🤝 Recommended Execution Tools & Scaffolds

Once IntentFlow generates your `EXECUTION_PLAN.md`, you can hand it off to any of these battle-tested tools:

| Tool | Specialty | Best When | Compatibility & Overhead |
| :--- | :--- | :--- | :--- |
| **[Superpowers](https://github.com/obra/superpowers)** | Strict TDD & Engineering Discipline | You want mandatory Red-Green-Refactor testing and subagent code reviews. | Universal (Claude Code, Cursor, Cline, Antigravity). Low-to-moderate overhead. |
| **[ECC](https://github.com/affaan-m/ECC)** | Full Agent Operating System | You want persistent memory across sessions and hundreds of specialized skills. | Best on Claude Code. Needs adaptation for other harnesses. |
| **[Firstmate](https://github.com/kunchenguid/firstmate)** | Agent Distro & Crew Fleet | You have a large or production pipeline requiring multiple agents working in parallel in tmux/zellij worktrees. | **Heavy overhead:** Requires macOS/Linux (WSL on Windows). Overpowered for small projects. |
| **[no-mistakes](https://github.com/kunchenguid/no-mistakes)** | Pre-Push AI Gatekeeper & Clean PRs | You use unopinionated tools (Aider, Claude Code, Cline) and want an automated worktree QA pipeline. | Universal git worktrees. Skip if using Superpowers. |
| **[Roo Code](https://github.com/RooVetGit/Roo-Code) / Cline** | VS Code Autonomous Roles | You want fine-grained role control (Architect, Code, Test) inside VS Code. | VS Code / JetBrains extension. Minimal overhead. |
| **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** | Sandboxed Full-Stack Dev | You want autonomous Docker-isolated code generation and testing. | Requires Docker sandbox across all platforms. |

---

## ❓ Frequently Asked Questions

**Q: Does `/planner` write code or install dependencies automatically?**  
*A:* No! The `/planner` command is **Planner-Only**. It focuses 100% on getting the requirements, architecture, and task breakdown right. It will never modify your codebase or run code without your explicit approval.

**Q: What coding tools can I use to build the plan?**  
*A:* Any tool you like! Once you have `EXECUTION_PLAN.md`, you can give it to Superpowers, ECC, Roo Code, Cline, Cursor, OpenHands, or any human developer.

**Q: What if I want a single tool that does both planning and execution?**  
*A:* We keep the main branch lightweight and dedicated to planning so it won't conflict with external coding agents. If you want to see our full monolithic framework design, check out the `backup-full-framework-idea` branch!

---

💡 *Happy Planning! Just type `/planner` in your chat anytime you want to start a new project!*

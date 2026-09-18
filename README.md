# 💡 IntentFlow — Your AI Architect & Planner

> **Turn your software ideas into bulletproof blueprints before writing a single line of code.**

---

### 🤔 Why IntentFlow?

Have you ever asked an AI coding tool to "build me an app," only to watch it get confused, hallucinate wrong assumptions, waste your tokens, or produce code that doesn't work?

AI models are brilliant coders, but they perform best when they have a **clear, structured plan** first. 

**IntentFlow** acts as your AI's **System Architect**. Before anyone writes code, your AI sits down with you, asks a few friendly questions, helps you figure out exactly what you want, and creates a step-by-step **Blueprint (`EXECUTION_PLAN.md`)**.

---

## 🛠️ How It Works (The 2-Step Workflow)

IntentFlow separates **Thinking** from **Building** so you always stay in control:

```
┌─────────────────────────────────────────────────┐
│  STEP 1: THINK & PLAN (IntentFlow)              │
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

### 1. Give your AI access to `.agents/`
Make sure the `.agents/` folder is in your project directory.

### 2. Copy & paste this prompt to start:
> *"Read `.agents/AGENTS.md` and `.agents/skills/planner/SKILL.md`. I want to plan a project called [Your Project Idea]. Act as my Planner: walk me through a few questions to clarify my goals, then help me draft the plan."*

### 3. What happens next?
1. **Friendly Q&A:** The AI will ask you 1–3 simple questions at a time to clarify your requirements, tech preferences, and features.
2. **Blueprint Creation:** The AI generates three plain-text files in your project root:
   - 📄 **`INTENT_BRIEF.md`** — *What we're building:* Goals, scope, and target features.
   - 📖 **`CONTEXT.md`** — *Vocabulary:* A simple glossary of terms so the AI doesn't mix up concepts.
   - 🗺️ **`EXECUTION_PLAN.md`** — *The Blueprint:* A step-by-step roadmap breaking down every task, file, and test needed.
3. **Review & Approve:** Read over the blueprint. Ask the AI to change anything you don't like. Once you approve it, you're done planning!
4. **Handoff & Build:** Pass `EXECUTION_PLAN.md` to your favorite AI coding tool (like Cursor, Cline, or ECC) and let it build your project step-by-step.

---

## 📁 What's Inside the Toolkit?

If you inspect the `.agents/` folder, here is what you'll find:

- 📜 **`AGENTS.md`**: The core rules for the AI. It instructs the AI to listen to you, ask questions, and focus strictly on planning.
- 🧰 **`skills/planner/`**: Step-by-step guides and ready-to-use templates for generating `INTENT_BRIEF.md` and `EXECUTION_PLAN.md`.
- 🔍 **`skills/grill-with-docs/`**: The interview skill the AI uses to ask targeted decision questions without overwhelming you.
- 📚 **`skills/planner/references/`**: Detailed guides on project discovery, architecture decisions, and discovering battle-tested tools/libraries.

---

## ❓ Frequently Asked Questions

**Q: Does IntentFlow write code or install dependencies automatically?**  
*A:* No! IntentFlow is **Planner-Only**. It focuses 100% on getting the requirements, architecture, and task breakdown right. It will never modify your codebase or run code without your explicit approval.

**Q: What coding tools can I use to build the plan?**  
*A:* Any tool you like! Once you have `EXECUTION_PLAN.md`, you can give it to Cursor, Claude Code, Cline, ECC (Everything Claude Code), Superpower, or any developer.

**Q: What if I want a single tool that does both planning and execution?**  
*A:* We keep the main branch lightweight and dedicated to planning so it won't conflict with external coding agents. If you want to see our full monolithic framework design, check out the `backup-full-framework-idea` branch!

---

💡 *Happy Planning! If you ever get stuck, just ask your AI assistant: "How do we start using the planner?"*

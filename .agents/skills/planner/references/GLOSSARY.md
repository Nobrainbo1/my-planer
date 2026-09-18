---
description: "Quick-reference glossary of AI coding terms. Look up words you encounter in the template or in agent conversations."
alwaysApply: false
---

# Glossary of AI Coding Terms

> **Source:** Adapted from Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding) — the most comprehensive plain-English reference for AI coding vocabulary.
> **Purpose:** Quick-reference when you encounter unfamiliar terms in this template, in agent output, or in documentation.

---

## The Model Layer

| Term | Plain English |
|------|--------------|
| **Model** | The parameters (weights). Stateless — does next-token prediction and nothing else. "Claude Opus 5" and "GPT-6" are models. On its own a model can't read files, run commands, or remember yesterday. |
| **Parameters / Weights** | The billions of numbers inside a model, set during training. Everything the model "knows" lives in them. They are frozen after training — nothing you do in a session changes them. |
| **Training** | The one-time process that sets a model's parameters. Done by the model provider. You can't do this — when the model doesn't know your codebase, the fix is context, not training. |
| **Inference** | Running a trained model to generate output. What happens every time you chat. Parameters stay fixed. Billed per token. |
| **Token** | The atomic unit a model reads and writes. Roughly ¾ of an English word. Context window size, cost, and speed are all measured in tokens. |
| **Next-token prediction** | What the model actually does. Given context, it predicts one next token, appends it, and repeats. Every output is built one token at a time. The model never checks if a token is *true*, only if it's *likely* — this is why hallucination happens. |
| **Non-determinism** | The same input can produce different output. Run a model twice with identical context and you may get different answers. Retrying is a legitimate strategy. |
| **Effort** | A dial for how much reasoning the model does before answering. Higher = smarter but slower and costlier. Match effort to the task, not the session. |
| **Model Provider** | Whatever serves a model for inference — Anthropic, OpenAI, Google (remote), or Ollama/LM Studio (local). |

## The Harness Layer

| Term | Plain English |
|------|--------------|
| **Harness** | Everything around the model that turns it into an agent: tools, system prompt, context management, permissions, hooks. Claude Code and Claude.ai use the *same model* but behave differently because their *harnesses* differ. **This template IS a harness blueprint.** |
| **System Prompt** | The instructions the harness prepends to every request — the agent's standing brief. Who it is, how to behave, what rules to follow. Your AGENTS.md content becomes part of this. |
| **Agent** | A model harnessed with tools, a system prompt, and a context window. Claude Code is an agent. Cursor is an agent. The agent is what you actually talk to — model in motion, configured for a purpose. |
| **AGENTS.md** | A file at the project root containing instructions loaded into every agent session. The cross-harness standard for steering agent behavior. |
| **Skill** | A packaged set of instructions (SKILL.md) that teaches the agent how to perform a specific task. Loaded on demand — the agent reads the skill when the task matches. |
| **Subagent** | A second agent spawned by the first to handle a subtask. Runs in its own context window with its own instructions. |

## Context & Sessions

| Term | Plain English |
|------|--------------|
| **Context** | The relevant information the agent has access to right now. Not the raw input (that's the context window), not the history (that's the session), but *what the agent knows that's pertinent to the task*. |
| **Context Window** | Everything the model sees on each request. Finite, model-specific. If something isn't in the window, the model doesn't know it exists. Treat it as a budget. |
| **Session** | One continuous conversation. Stateful across turns (context accumulates), stateless across sessions (next session starts empty unless memory is loaded). |
| **Turn** | One exchange: you say something, the agent responds. A single turn can spawn many model provider requests if the agent calls tools. |
| **Stateless** | The model carries no information forward. Each request re-sends the full context. The model doesn't learn from corrections, doesn't remember yesterday, isn't getting to know you. |
| **Prefix Cache** | Provider-side optimization that skips re-processing repeated context. Why long sessions are affordable — history only changes at the end, so the shared prefix is cached cheaply. |

## Tools & Environment

| Term | Plain English |
|------|--------------|
| **Tool** | Something the agent can call to interact with the outside world — reading files, running commands, querying APIs. The model outputs a structured request; the harness executes it. |
| **Tool Call** | The model asking the harness to execute a tool. A structured string parsed out of the output stream. The model doesn't "decide" to call a tool — it's next-token prediction that happens to produce a tool-call format. |
| **MCP (Model Context Protocol)** | An open standard that lets agents connect to external systems (databases, APIs, file systems) through a unified protocol. Think "USB-C for AI tools." |
| **Sandbox** | An isolated environment where the agent runs code. Limits blast radius — a sandbox crash doesn't affect your real system. |
| **Permission Mode** | Whether the agent asks before acting (ask mode) or acts autonomously (agent mode / YOLO mode). |

## Failure Modes

| Term | Plain English |
|------|--------------|
| **Hallucination** | The model confidently states something false. Happens because next-token prediction optimizes for *likely*, not *true*. The fix is providing correct context, not correcting the model. |
| **Sycophancy** | The model agrees with you even when you're wrong, because agreement is statistically likely in its training data. |
| **Attention Degradation** | As context grows, the model's ability to focus on specific parts degrades. Information in the middle of a long context gets less attention than information at the start or end. This is why long sessions feel "dumber." |
| **Smart Zone** | The region of context usage where the model performs best — typically 40-70% of the context window. Too little context = not enough information. Too much = attention degradation. |
| **Knowledge Cutoff** | The date when training data ends. The model hasn't seen anything published after this date. |

## Handoffs & Memory

| Term | Plain English |
|------|--------------|
| **Handoff** | Passing work from one session/agent to another. The key challenge: the receiving agent starts with zero context, so you must write down everything it needs to know. |
| **Handoff Artifact** | A document written specifically to transfer context between sessions. Contains: what was done, what's left, key decisions, file locations. The bridge between stateless sessions. |
| **Clearing** | Deliberately starting a fresh session, discarding accumulated context. Useful when context has degraded or when switching tasks. |
| **Compaction** | Summarizing the conversation so far to free up context window space. Loses detail but extends the session's useful life. |
| **Autocompact** | When the harness automatically compacts without asking. Happens when the context window approaches its limit. |
| **Primary Source** | The file or artifact an agent should read FIRST — the authoritative document for a task (e.g., the spec, the AGENTS.md). |
| **Memory System** | Any mechanism that persists information across sessions — AGENTS.md files, memory databases (Mem0), handoff artifacts. |
| **Progressive Disclosure** | Loading context in layers: first show metadata (file names, function signatures), then drill into detail only when needed. Prevents context bloat. |

## Patterns of Work

| Term | Plain English |
|------|--------------|
| **Human-in-the-loop** | A human reviews and approves at key checkpoints. The agent proposes; the human decides. This template uses three numbered checkpoints: after Phase 2 (Plan Approval), after Phase 4 (Implementation Review), and in Phase 6 (Deployment Approval, when requested). Explicit intent approval and delivery-readiness approval are also required. Installation and restricted delivery actions each need separate authorization. |
| **Vibe Coding** | Prompting an AI without structure — ad-hoc, conversational, no spec, no verification. Fast for prototypes, expensive for production (low CapEx, high OpEx). |
| **Agentic Engineering** | Structured orchestration of AI agents through defined workflows — spec-driven, tool-assisted, verified. What this template teaches (medium CapEx, low OpEx). |
| **Grilling** | An intensive Q&A session where the agent interviews you to extract requirements. The agent asks; you answer. Used in Phase 1 Discovery. |
| **AFK (Away From Keyboard)** | Running the agent autonomously while you do something else. Only safe when automated checks can catch failures. |
| **AX (Agent Experience)** | How well-configured the environment is for the agent to work in — clear AGENTS.md, available tools, well-structured code. The agent equivalent of DX (Developer Experience). |
| **Context Engineering** | The discipline of curating what information an agent receives. Displaces "prompt engineering" — it's not about how you ask, it's about what the agent knows when it answers. |

---

## Further Reading

- **Full dictionary with examples:** [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding) — every term above has extended explanations with usage examples
- **The paper:** *"The New SDLC With Vibe Coding"* by Addy Osmani, Shubham Saboo, and Sokratis Kartakis
- **System prompt studies:** [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) — see how Claude Code, Cursor, Codex, and Gemini are actually configured under the hood. Useful for understanding what good system prompts look like (study the patterns, don't copy-paste).

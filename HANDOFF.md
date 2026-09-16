# 🔄 SESSION HANDOFF — Agentic Engineering Workflow Template

> **From Session:** `793c57b8-7e07-4208-80e5-0a86b3b3d1e5` (Antigravity)
> **Date:** 2026-09-16
> **Orchestrator:** natth
> **Workspace:** `c:\Users\natth\Downloads\template_workflow`
> **Status:** Audit complete, fixes approved, implementation NOT started

---

## What This Project Is

An **Agentic Engineering Workflow Template** — a harness-agnostic system of Markdown files that guides AI agents through a 6-phase software development lifecycle. Inspired by the paper *"The New SDLC With Vibe Coding"* by Addy Osmani, Shubham Saboo, and Sokratis Kartakis (Google, 2026).

It is NOT a project — it is a **template/blueprint** that gets copied into any project to structure how AI agents work on that project.

---

## Current File Structure (17 files, ~125KB)

```
template_workflow/
├── README.md                          (10.4KB) — Main overview, structure table, harness compat, reading order
├── WHY_THIS_WORKS.md                  (12.9KB) — Educational "why" behind every design decision
├── GLOSSARY.md                        (9.7KB)  — 40+ AI coding terms in plain English (from Matt Pocock's dictionary)
├── AGENTS.md                          (6.3KB)  — Agent identity, rules, communication protocol, context discipline
├── SCAFFOLDS.md                       (18.7KB) — Catalog of scaffolds, skills, MCP servers (8 categories)
├── 01_DISCOVERY.md                    (5.5KB)  — Phase 1: Intent definition
├── 02_PLANNING.md                     (8.9KB)  — Phase 2: Context engineering, execution plan
├── 03_TOOLING.md                      (11KB)   — Phase 3: Tool/skill discovery
├── 04_IMPLEMENTATION.md               (9.5KB)  — Phase 4: Builder-Validator loop
├── 05_VERIFICATION.md                 (7.2KB)  — Phase 5: Testing, security, DoD
├── 06_DELIVERY.md                     (6.9KB)  — Phase 6: Deployment, retrospective
├── references/                        (EMPTY)  — Orphaned empty directory
└── templates/
    ├── intent_brief.md                (3KB)    — Phase 1 template
    ├── execution_plan.md              (2.7KB)  — Phase 2 template
    ├── tool_discovery_report.md       (2.6KB)  — Phase 3 template
    ├── retrospective.md               (1.8KB)  — Phase 6 template
    └── skill_creation_guide.md        (11KB)   — Guide for creating SKILL.md files
```

---

## What Was Done Across All Sessions

### Session 1 — Foundation (2026-09-08)
- Created all 6 phase files, AGENTS.md, README.md, 4 templates
- Based on the Osmani/Saboo/Kartakis paper
- Added HIGH/LOW detail level toggle to Phase 2
- Added Discovery Protocol for starting from zero
- Added MCP tool discovery and evaluation

### Session 2 — Scaffolds & Skills (2026-09-09)
- Created SCAFFOLDS.md with 8 categories of scaffolds
- Deep-studied ECC scaffold, addyosmani/agent-skills, anthropics/skills, mukul975/cybersecurity-skills
- Created `templates/skill_creation_guide.md` with 5 body patterns
- Added Orchestrator Mindset, Context Discipline, Scaffold-First Development to AGENTS.md
- Removed version from README

### Session 3 — Educational Layer (2026-09-16)
- Created WHY_THIS_WORKS.md (the thinking behind every design decision)
- Created GLOSSARY.md (adapted from mattpocock/dictionary-of-ai-coding)
- Added "💡 Why This Phase Exists" boxes to all 6 phase files
- Added Reading Order for Humans to README
- Assessed system_prompts_leaks repo (referenced, not integrated)

### Session 3 (cont.) — Full Audit
- Two independent audits (agent + subagent) found **28 issues**
- User reviewed and approved all fixes with specific instructions
- **Implementation NOT started** — handoff requested instead

---

## APPROVED FIXES — Implementation Instructions

The user approved ALL fixes. Below is every fix with the user's exact decision.

### Batch 1: Simple Find-and-Replace Fixes (~15 min)

#### Fix C3 — Category reference in 03_TOOLING.md
- **File:** `03_TOOLING.md` line 30
- **Change:** `Category 6 in SCAFFOLDS.md` → `Category 8 in SCAFFOLDS.md`

#### Fix C4 — Step reference in 03_TOOLING.md
- **File:** `03_TOOLING.md` line 110
- **Change:** `(Step 3.3)` → `(Step 3.4)`

#### Fix C6 — Hallucinated Twitter handles in SCAFFOLDS.md
- **File:** `SCAFFOLDS.md` line 276
- **Change:** Replace `@anthropaborgs` and `@mcaborgs` with verified real handles
- **User instruction:** *"be sure that those new replacement also exist"*
- **Action:** Verify each handle exists before replacing. Use `@AnthropicAI` (verified), `@addyosmani` (verified). Remove `@mcaborgs` entirely.

#### Fix C7 — Dead `pip search` command + add `uv` support
- **File:** `SCAFFOLDS.md` line 267
- **Change:** Replace `pip search mcp-server` with browser search `https://pypi.org/search/?q=mcp-server`
- **User instruction:** *"fix it that depreciation. and also try to have it utilizing more on to the uv for python https://docs.astral.sh/uv/"*
- **Action:** Add `uv` as the recommended Python package manager. Reference `https://docs.astral.sh/uv/`. Example: `uv add mcp-server-*`

#### Fix C8 — MoSCoW label mismatch
- **File:** `01_DISCOVERY.md` line 75
- **Change:** `Nice to Have` → `Could Have`

#### Fix C12 — Deprecated create-react-app
- **File:** `SCAFFOLDS.md` line 178
- **Change:** `create-react-app` → `Vite`

#### Fix P3 — Literal placeholder links in templates
- **Files:** `templates/execution_plan.md` line 9, `templates/tool_discovery_report.md` line 9
- **Change:** `[link to intent_brief.md]` → `[Intent Brief](./intent_brief.md)` (proper markdown links)

#### Fix P4 — Obsolete git-secrets reference
- **File:** `05_VERIFICATION.md` line 114
- **Change:** Remove `git-secrets`, recommend `gitleaks` as primary

---

### Batch 2: Cross-References & Checkpoint Standardization (~20 min)

#### Fix C9 — AGENTS.md phase file index
- **File:** `AGENTS.md`
- **Action:** Add a compact section listing all 6 phase files with links, so agents who load AGENTS.md can find the workflow

#### Fix C10 — Link templates from phase files
- **Files:** `02_PLANNING.md`, `03_TOOLING.md`, `06_DELIVERY.md`
- **Action:** Add explicit template links at end of each phase (like `01_DISCOVERY.md` line 160 does)
- Pattern: `> Use the template at [templates/X.md](./templates/X.md)`

#### Fix C11 — Checkpoint standardization
- **Files:** `GLOSSARY.md` line 86, `README.md` diagram, `01_DISCOVERY.md` frontmatter, `05_VERIFICATION.md` frontmatter
- **Action:** Define 3 checkpoints consistently everywhere:
  - Checkpoint 1: End of Phase 2 (Plan Approval)
  - Checkpoint 2: End of Phase 4 (Implementation Review)
  - Checkpoint 3: Phase 6 (Deployment Approval)
- Update `01_DISCOVERY.md` to remove contradictory checkpoint reference or set `checkpoint: true`
- Update `05_VERIFICATION.md` to add human gate before delivery

---

### Batch 3: Handoff Step & Template (~30 min)

#### Fix C1 — Create handoff system
- **File (modify):** `06_DELIVERY.md` — Add `Step 6.3.5 — Session Handoff Artifact` between Documentation and Retrospective
- **File (create):** `templates/handoff_artifact.md` — New template with:
  - System State (what exists now)
  - Decisions Made (and rationale)
  - Unresolved Blockers / Tech Debt
  - Key Entry Points (where to start)
  - Next Session Action Items

---

### Batch 4: Template Alignment & Content Sync (~30 min)

#### Fix C2 — Reorder tool_discovery_report.md
- **File:** `templates/tool_discovery_report.md` lines 26-56
- **New order:** Built-in → Skills → MCP → Packages → APIs → Custom (matching 03_TOOLING.md and WHY_THIS_WORKS.md)

#### Fix C5 — Fix broken markdown nesting
- **File:** `06_DELIVERY.md` lines 67-103
- **User instruction:** *"split into 2 blocks"*
- **Action:** Close the first code block before the checkpoint, then open a new one for the checkpoint request

#### Fix C13 — Chicken-and-egg tool ordering + memory alternatives
- **Files:** `SCAFFOLDS.md`, `02_PLANNING.md`
- **User instruction:** *"could you also add a way to use obsidian vault as a memory as well? or any other alternative that is free, easy to use and setup"*
- **Action:** Clarify pre-flight tooling for existing codebases. Add memory alternatives:
  - Obsidian vault (free, local, markdown-based)
  - Plain markdown files in a `.memory/` directory
  - codebase-memory-mcp (if MCP available)
  - Any free/local alternatives found during research

#### Fix I2 — Sync diverged templates
- **User instruction:** *"keep the latest one"*
- **Action:** For retrospective: keep `templates/retrospective.md` (the richer version) and update `06_DELIVERY.md` inline to reference it instead of duplicating. Same for tool discovery.

#### Fix I4 — Complete execution_plan.md LOW-LEVEL sections
- **User instruction:** *"add in more detail by researching more into the topic to complete it"*
- **Action:** Research best practices for execution plans and add the 6 missing sections: File Change Plan, Dependency Graph, Code Interaction Map, Edge Case Analysis, Migration Plan, Rollback Strategy

#### Fix I7 — Remove HIGH-LEVEL toggle, go LOW-LEVEL only
- **User instruction:** *"let delete the part where it have a high-level and just go on for low-level"*
- **Files:** `templates/intent_brief.md` line 11, `02_PLANNING.md` Step 2.0
- **Action:** Remove the HIGH/LOW toggle. Default everything to LOW-LEVEL (full detail). Remove or simplify the HIGH-LEVEL description.

#### Fix I8 — Intent Brief approval table
- **File:** `templates/intent_brief.md` Section 9 (lines 124-132)
- **Action:** Remove downstream phase approval rows. Keep only Intent Brief approval.

---

### Batch 5: Missing Content & New Sections (~45 min)

#### Fix I1 — Quick Start in README
- **User instruction:** *"try your best to refactor it for it to be more simple"*
- **Action:** Add a "Quick Start — Minimal Path" section showing the 3-step minimum for small projects

#### Fix I3 — Create Phase 4 and Phase 5 templates
- **User instruction:** *"add one by searching for top templates on the internet"*
- **Action:** Research popular task execution log and verification report templates. Create:
  - `templates/task_execution_log.md` (for Phase 4: tracking Builder-Validator runs, retries, commits)
  - `templates/verification_report.md` (for Phase 5: test results, security audit, DoD checklist)

#### Fix I5 — Context compaction guidance in Phase 4
- **User instruction:** *"these should have a small reminder when the context is getting close to full. not an automation. it should have enough room of context to be able to do a handoff as well. as compact could ruin the project if not use right by human hand."*
- **File:** `04_IMPLEMENTATION.md`
- **Action:** Add a "Context Health" section with:
  - A reminder (not automation) when context approaches ~70% full
  - Warning to leave room for a handoff artifact before compacting
  - Explicit guidance that compaction requires human approval (not agent-initiated)

#### Fix I6 — Git rollback instructions on escalation
- **User instruction:** *"add a way for the project to utilize git for these problem and also advice to start a repo before doing any project as a progress tracker plus a version control"*
- **File:** `04_IMPLEMENTATION.md` Step 4.1.3 (escalation block)
- **Action:** Add git-based rollback instructions:
  - `git stash` before risky changes
  - `git checkout -- .` to revert on failure
  - Commit after each successful task
  - Add advice in Phase 1 or AGENTS.md: "Initialize git repo before starting any project"

#### Fix I9 — Secret management guidance
- **User instruction:** *"add those instruction into this planer project"*
- **Files:** `04_IMPLEMENTATION.md` or `AGENTS.md`
- **Action:** Add secret management rules:
  - Never hardcode secrets in source code
  - Use `.env.example` (committed) + `.env` (gitignored)
  - Add `.env` to `.gitignore` before first commit
  - Redaction rules for agent output (never echo secrets in chat)

#### Fix I10 — Concrete context gathering heuristics
- **File:** `02_PLANNING.md` Step 2.1
- **Action:** Add specific commands/patterns for each context gathering bullet (e.g., `cat package.json`, `find . -name "*.openapi.yaml"`, `grep -r "TODO\|FIXME"`)

---

### Batch 6: Polish (~15 min)

#### Fix P1 — Empty references/ directory
- **Action:** Either add a `references/README.md` explaining purpose ("place paper PDFs, design docs, competitor analysis here") or delete the directory

#### Fix P2 — AGENTS.md "under 150 lines" limit
- **File:** `AGENTS.md` line 104
- **Action:** Change to "Keep AGENTS.md concise — move phase-specific detail to the phase files" (remove specific number)

#### Fix P5 — README ASCII diagram
- **File:** `README.md` lines 89-118
- **Action:** Redraw as sequential vertical flow with 3 checkpoints clearly positioned

---

## Key Design Decisions Already Made

These are load-bearing decisions made across sessions that the next agent should NOT change:

1. **Harness-agnostic format** — Standard Markdown + YAML frontmatter. Must work with Cursor, Claude Code, Cline, Copilot, Antigravity, Windsurf, Kiro, OpenCode, Codex, etc.
2. **6 phases, sequential** — Discovery → Planning → Tooling → Implementation → Verification → Delivery
3. **AGENTS.md at root** — Cross-harness standard for agent identity and rules
4. **Discover before build** — Always search for existing tools/skills before building custom
5. **Builder-Validator pattern** — Core implementation loop with 3-retry escalation
6. **3 checkpoints** — After Phase 2, Phase 4, and before deployment in Phase 6
7. **Human judgment at checkpoints** — Agent proposes, human approves
8. **Skill creation guide** — Template can generate its own SKILL.md files using 5 proven body patterns
9. **LOW-LEVEL by default** — User decided to remove HIGH-LEVEL toggle (Fix I7)
10. **No automation of compaction** — Human must approve context compaction (Fix I5)

---

## Sources Studied (for context)

| Source | What We Learned | Where It's Used |
|--------|----------------|----------------|
| *"The New SDLC With Vibe Coding"* (Osmani et al.) | 6-phase SDLC, Builder-Validator, Context Engineering, "Evals not vibes" | Entire template structure |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Gated Workflow pattern, `npx skills add` CLI | SCAFFOLDS.md, skill_creation_guide.md |
| [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | Mantra, Outsider Review, Decision Table patterns | skill_creation_guide.md body patterns |
| [anthropics/skills](https://github.com/anthropics/skills) | Canonical SKILL.md format | skill_creation_guide.md anatomy |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Playbook pattern (817 skills) | skill_creation_guide.md body patterns |
| [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding) | 40+ terms in plain English, handoff concepts | GLOSSARY.md |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | System prompt architecture patterns | Referenced in GLOSSARY.md (study, don't copy) |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Memory persistence, security scanning, context compaction patterns | SCAFFOLDS.md Category 1 |
| [uv docs](https://docs.astral.sh/uv/) | User wants uv as recommended Python tool manager | To be added in Fix C7 |

---

## How to Start the Next Session

1. **Load this file into context** — paste or reference `HANDOFF.md` at session start
2. **Tell the agent:** *"Read the HANDOFF.md in the workspace root. Execute all approved fixes in the order listed (Batch 1 through Batch 6). Research as needed for I3, I4, and I10."*
3. **The agent should work through batches sequentially**, committing after each batch
4. **After all fixes:** Run a verification listing and update the walkthrough

> **Estimated total effort:** ~2.5 hours for all 28 fixes

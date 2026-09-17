---
description: "Reusable Session Handoff Artifact template. Use when passing work between sessions, agents, or team members."
type: template
---

# Session Handoff — [Project/Feature Name]

> **Date:** [YYYY-MM-DD]  
> **From:** [Session ID / Agent / Team member]  
> **To:** [Next session / Agent / Team member]  
> **Status:** [In Progress / Blocked / Ready for Next Phase]

---

## System State — What Exists Now

### Files & Structure
| Path | Status | Description |
|------|--------|-------------|
| [file/directory] | [Created / Modified / Unchanged] | [what it does, current state] |

### Dependencies & Environment
- **Runtime:** [e.g., Node.js 22, Python 3.12]
- **Package Manager:** [e.g., pnpm, uv]
- **Key Dependencies:** [list with versions]
- **Environment Variables Required:** [list — names only, no values]

### What Is Working
- [Feature/component that is complete and verified]
- [Feature/component that is complete and verified]

### What Is Partially Complete
- [Feature/component] — [what's done, what remains]
- [Feature/component] — [what's done, what remains]

---

## Decisions Made — And Why

| Decision | Rationale | Alternatives Considered | Impact |
|----------|-----------|------------------------|--------|
| [e.g., Chose PostgreSQL over SQLite] | [e.g., Need concurrent writes for multi-user] | [e.g., SQLite, MongoDB] | [e.g., Requires DB server setup] |
| [e.g., Used Server Components for data fetching] | [e.g., Reduces client bundle, better SEO] | [e.g., Client-side fetch, tRPC] | [e.g., Some components can't use hooks] |

---

## Unresolved Blockers / Tech Debt

| ID | Issue | Severity | Context | Suggested Resolution |
|----|-------|----------|---------|---------------------|
| B-01 | [blocker or debt item] | [Critical / High / Medium / Low] | [why it exists, what caused it] | [proposed fix or workaround] |

---

## Key Entry Points — Where to Start

> **Read these files first** to get up to speed quickly:

1. **Primary source of truth:** [e.g., `AGENTS.md` — project rules and agent identity]
2. **Current spec:** `INTENT_BRIEF.md` at the target project root — approved requirements and revision; `CONTEXT.md` alongside it contains resolved domain terms.
3. **Current plan:** `EXECUTION_PLAN.md` at the target project root — approved task breakdown; include the exact project-local execution ledger path. Do not point to the shipped blank templates.
4. **Main entry point:** [e.g., `src/index.ts` — application entry]
5. **Test suite:** [e.g., `tests/` — run with `npm test`]

---

## Next Session Action Items

| Priority | Task | Context | Phase |
|----------|------|---------|-------|
| 🔴 Must Do | [task] | [why it's urgent, any deadlines] | [Phase X] |
| 🟡 Should Do | [task] | [context] | [Phase X] |
| 🟢 Could Do | [task] | [context] | [Phase X] |

---

## Context Warnings

> **Things the next agent/session should know that aren't obvious:**

- [e.g., "The `users` table migration has NOT been run on staging yet"]
- [e.g., "The API rate limit from provider X is 100 req/min — the batch job needs throttling"]
- [e.g., "File X is auto-generated — don't edit manually, modify the template instead"]
- [e.g., "The required test for feature Y failed intermittently. This remains a blocker pending investigation; preserve the failing run evidence, assign an owner, and revalidate the fix before readiness."]

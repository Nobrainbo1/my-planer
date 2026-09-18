---
description: "Phase 3: Tool Discovery, Evaluation & Creation. Equip the agent harness with the right tools. Always discover existing solutions before building custom ones."
phase: 3
checkpoint: false
---

# Phase 3: Tooling — Discover, Evaluate, Equip

> **Goal:** Equip the agent's **harness** with the tools it needs to execute the plan. This phase follows the paper's core principle: the agent = **Model + Harness**, and the harness is where engineering effort should be concentrated.

> **Critical Rule:** **DISCOVER before you BUILD.** For every capability needed, the agent must first search for existing, battle-tested tools. Only create custom tooling when no adequate solution exists or when integration cost exceeds build cost.

> **💡 Why This Phase Exists:** Without this, you reinvent the wheel. You spend 3 hours writing a custom tool when a well-maintained npm package does the same thing. The ecosystem of skills, MCP servers, and packages is huge — your custom tool should be the last resort, not the first instinct. **On paper:** For each capability you need, Google for 5 minutes before building it yourself.

---

## Step 3.0 — Scaffold Consultation

Reuse the existing project structure and harness by default. No new tooling is a valid outcome when available tools meet the approved plan. Consider a scaffold only for approved greenfield work or an explicitly approved migration; a small existing-project change does not authorize replacing its structure.

> **Consult [`SCAFFOLDS.md`](./SCAFFOLDS.md)** — the reference catalog of scaffolds, frameworks, harnesses, and starter templates organized by project type.

**Decision Matrix:**

| Situation | Action |
|-----------|--------|
| Existing project and adequate tools | Reuse them; record that no new tooling is needed. |
| A scaffold exists that covers 80%+ of approved greenfield or migration needs | Evaluate adoption; record affected tasks and permissions before acting. |
| A scaffold covers 50-80% of approved greenfield or migration needs | Evaluate a fork or extension; plan gaps and permissions before acting. |
| No adequate scaffold exists | **Proceed to Step 3.1** — assemble tools individually. |
| Starting from absolute zero (no codebase, no tech stack) | **Check Category 8 in SCAFFOLDS.md** for project-type starters (Next.js, FastAPI, etc.) and **Category 1** for agent harness scaffolds (ECC, agent-project, etc.) |

---

## Step 3.1 — Tool Needs Assessment

Based on the Execution Plan from Phase 2, identify every capability the agent needs.

```markdown
### Tool Needs Inventory

| ID | Capability Needed | Category | Example |
|----|------------------|----------|---------|
| T-01 | [e.g., Read and modify files in workspace] | Codebase Access | File system tools |
| T-02 | [e.g., Run terminal commands safely] | Execution / Sandbox | Shell access |
| T-03 | [e.g., Query a PostgreSQL database] | Data Access | DB client |
| T-04 | [e.g., Search the web for documentation] | Research | Web search |
| T-05 | [e.g., Generate UI components from design] | AI Augmentation | Image-to-code |
| T-06 | [e.g., Deploy to staging environment] | CI/CD | Deployment tool |
| T-07 | [e.g., Manage GitHub issues and PRs] | Project Management | GitHub API |
```

---

## Step 3.2 — Discovery: Search for Existing Tools

For each capability in the inventory, follow this discovery protocol **in order**:

### Discovery Protocol

```
For each Tool Need (T-XX):

1. CHECK BUILT-IN TOOLS
   └─ Does your current AI harness already provide this?
      (e.g., Antigravity has file editing, search, terminal; Cursor has codebase indexing)
      → If YES: Document it and move to next need.

2. SEARCH AGENT SKILLS (SKILL.md Ecosystem)
   └─ Is there a pre-built skill that handles this task?
      Sources to check (in order):
      • addyosmani/agent-skills — SDLC skills (/spec, /plan, /build, /test, /review)
      • VoltAgent/awesome-agent-skills — 1000+ curated skills by category
      • anthropics/skills — Official Anthropic skill patterns
      • skills-hub.ai — Aggregated skill discovery
      • agenticskills.io — Security-audited skills
      • npx skills search <keyword> — CLI search across skill registries
      • GitHub: "SKILL.md" in:path <your-domain>
      → If YES: Record the candidate; evaluate it before the approval gate in Step 3.3.

2b. FOR MODE A PIPELINE AGENTS: SEARCH PERSONA LIBRARIES
   └─ Does an existing persona match each agent the pipeline will create?
      Sources to check (in order):
      • msitarzewski/agency-agents — 279+ division-organized personas (engineering,
        design, product, testing, security, and 13 more divisions)
      • VoltAgent/awesome-agent-skills and the sources above for persona variants
      → If YES: Map each pipeline agent to the single most relevant persona file.
        Record exact repository-relative paths plus a pinned commit SHA in
        EXECUTION_PLAN.md. Do NOT clone or install during planning. Retrieval
        happens during approved execution before adapting prompts, using
        anchored exact-file sparse patterns. See planner SKILL.md Step 4A
        for illustrative commands, pinned-revision retrieval, and acceptance
        checks. Sparse checkout limits working-tree files, not all metadata
        or network traffic. Evaluate fetched personas with Step 3.3 before use.
   → If NO: Document why no persona fits; write the role from the intent.

3. SEARCH MCP SERVER REGISTRIES
   └─ Is there an existing MCP server that provides this capability?
      Sources to check (in order):
      • registry.modelcontextprotocol.io — Official MCP registry
      • mcp.directory — Large searchable directory, one-click install
      • mcp.so — Marketplace browsable by category
      • smithery.ai — Registry with install commands
      • github.com/modelcontextprotocol/servers — Reference implementations
      • GitHub: "modelcontextprotocol" OR "mcp server" <your-capability>
      → If YES: Record the candidate; evaluate it before the approval gate in Step 3.3.

4. SEARCH PACKAGE REGISTRIES
   └─ Is there a well-maintained library/CLI that does this?
      Sources to check:
      • npm / PyPI / crates.io / Go modules (language-specific)
      • GitHub search for "[capability] CLI tool"
      • Awesome lists (e.g., awesome-mcp-servers, awesome-devtools)
      → If YES: Record the candidate; evaluate it before the approval gate in Step 3.3.

5. SEARCH FOR EXISTING APIs
   └─ Is there a hosted API/service that provides this?
      Sources to check:
      • RapidAPI, Postman API Network
      • Official service documentation (e.g., GitHub API, Stripe API)
      → If YES: Record the candidate; evaluate it before the approval gate in Step 3.3.

6. BUILD CUSTOM (Last Resort)
   └─ If nothing adequate was found in steps 1-5:
      • Document why existing solutions are insufficient.
      • Design the minimal custom tool needed.
      • Follow the Custom Tool Creation template (Step 3.4).
```

---

## Step 3.3 — Evaluation: Score Each Candidate

For every discovered tool, score it before adopting.

```markdown
### Tool Evaluation Matrix

| Criteria | Weight | Score (1-5) | Notes |
|----------|--------|-------------|-------|
| **Functionality Match** | 30% | [1-5] | Does it do what we need? |
| **Maintenance & Community** | 20% | [1-5] | Active development? Stars? Last commit? |
| **Security & Trust** | 20% | [1-5] | Known CVEs? Trusted publisher? Open source? |
| **Integration Effort** | 15% | [1-5] | How easy to plug into our harness? |
| **Documentation Quality** | 10% | [1-5] | Can the agent understand how to use it? |
| **Cost** | 5% | [1-5] | Free? Token costs? API pricing? |
| **TOTAL** | 100% | [weighted] | |
```

**Decision Thresholds:**
- **Score ≥ 4.0:** Recommend adoption, subject to security and approval gates.
- **Score 3.0–3.9:** Recommend adoption with documented caveats, subject to the same gates.
- **Score 2.0–2.9:** Consider planning a custom tool or look for alternatives.
- **Score < 2.0:** Reject.

### Installation and Change Approval Gate

Discovery is read-only. Evaluate source, version, security, permissions, and side effects before installation or adoption; a score is not authorization. Do not use a discovery command that downloads or executes an unapproved package. If evaluation needs restricted access or execution, request that permission first.

Record the exact pinned source/version, proposed command, shell, working directory, destination, configuration changes, and side effects. Obtain separate explicit installation approval with approver, date, and message/reference before installing. Configuration, retrieval, and integration must stay within approved scope and permissions. Record actual validation evidence after the approved action; harness approval alone is not installation permission.

If discovery changes architecture, dependencies, owned files, or implementation tasks, return to Phase 2. Update tasks, tests, ownership, and preflight, and obtain renewed approval of affected intent/plan revisions before acting. Custom tooling and scaffold implementation use Phase 4's checks and ordered reviews, not an unreviewed Phase 3 shortcut.

---

## Step 3.4 — Custom Tool Creation (When Discovery Fails)

If no existing tool meets the need, propose a minimal custom tool in the execution plan. Obtain any required renewed plan and action approvals, then implement through Phase 4. Choose the right format:

| What You Need | Create | Guide |
|---------------|--------|-------|
| **Agent behavior / workflow / methodology** (e.g., debugging discipline, review process, deployment checklist) | A `SKILL.md` file | See [`skill_creation_guide.md`](../resources/templates/skill_creation_guide.md) — 5 proven body patterns, starter templates, quality checklist |
| **External capability** (e.g., database migration, API wrapper, file processor) | A CLI tool or MCP server | See the specification template below |
| **Both** (methodology + tool) | A skill directory with `SKILL.md` + `scripts/` | Combine both guides — the skill instructs, the script executes |

```markdown
### Custom Tool Specification

**Tool Name:** [e.g., `project-db-migrator`]
**Purpose:** [What capability does this provide?]
**Why Custom:** [Why were existing tools insufficient? Reference discovery results.]

#### Interface
- **Input:** [What the tool accepts — arguments, stdin, file paths]
- **Output:** [What the tool returns — stdout, files, status codes]
- **Side Effects:** [What the tool changes — files, database, network calls]

#### Implementation Plan
- **Language:** [e.g., Python, Node.js, Bash]
- **Dependencies:** [Minimal dependency list]
- **Estimated LOC:** [Rough size]
- **Test Strategy:** [How to verify the tool works]

#### MCP Server Wrapper (if applicable)
If this tool should be available to agents via MCP:
- **Server Name:** [e.g., `mcp-project-db`]
- **Protocol:** `stdio` / `sse`
- **Tools Exposed:**
  - `tool_name_1` — [description, params, return]
  - `tool_name_2` — [description, params, return]
```

---

## Step 3.5 — Harness Assembly

Compile the final tool inventory into a harness configuration.

```markdown
### Harness Configuration

#### Built-in Tools (from harness)
| Tool | Capability | Notes |
|------|-----------|-------|
| [e.g., file_editor] | Read/write files | Native to harness |
| [e.g., terminal] | Run shell commands | Sandboxed |
| [e.g., web_search] | Search the internet | Built-in |

#### MCP Servers
| Server | Source | Capability | Config |
|--------|--------|-----------|--------|
| [e.g., @modelcontextprotocol/server-filesystem] | Official | File system access | `stdio` |
| [e.g., @modelcontextprotocol/server-github] | Official | GitHub API access | `stdio`, needs PAT |
| [e.g., @modelcontextprotocol/server-postgres] | Official | PostgreSQL queries | `stdio`, needs conn string |
| **RTK (Run Time context)** | [rtk-ai/rtk] | Log & error tracking | **MANDATORY**: Token optimization |

#### External APIs
| API | Provider | Auth Method | Rate Limits |
|-----|----------|-------------|-------------|
| [e.g., GitHub REST API] | GitHub | OAuth token | 5000 req/hr |
| [e.g., OpenAI API] | OpenAI | API key | Tier-based |

#### Custom Tools
| Tool | Location | Purpose | Status |
|------|----------|---------|--------|
| [e.g., db-migrator] | `tools/db-migrator/` | Database migrations | To be built |

#### Agent Skills / Plugins
| Skill | Source | Capability |
|-------|--------|-----------|
| [e.g., graphify] | Workspace skill | Codebase knowledge graph |
| [e.g., generative_ui] | Built-in | Rich HTML widget rendering |
```

---

## Step 3.6 — Greenfield Project Toolkit

When starting a project from zero, the agent should recommend a **starter toolkit** based on the tech stack chosen in Phase 2.

```markdown
### Recommended Starter Toolkit

Based on the tech stack [chosen in Phase 2], here are the recommended tools:

#### Development Environment
- **Package Manager:** [e.g., pnpm, uv, cargo]
- **Language Runtime:** [e.g., Node.js 22 LTS, Python 3.12, Rust 1.80]
- **Framework:** [e.g., Next.js 15, FastAPI 0.115, Axum 0.7]

#### Code Quality
- **Linter:** [e.g., ESLint 9, Ruff, Clippy]
- **Formatter:** [e.g., Prettier 3, Black, rustfmt]
- **Type Checker:** [e.g., TypeScript 5.6, mypy, built-in]

#### Testing
- **Unit Testing:** [e.g., Vitest, pytest, cargo test]
- **Integration Testing:** [e.g., Playwright, httpx, reqwest]
- **Coverage:** [e.g., c8/istanbul, coverage.py, tarpaulin]

#### AI & Agent Tools
- **MCP Servers:** [Recommended based on project needs]
- **AI APIs:** [e.g., Claude API, OpenAI API, Gemini API]
- **Embedding/RAG:** [e.g., Chroma, Pinecone, local FAISS]

#### CI/CD
- **Pipeline:** [e.g., GitHub Actions, GitLab CI]
- **Deployment:** [e.g., Vercel, Railway, Fly.io]
- **Monitoring:** [e.g., Sentry, Datadog, self-hosted]
```

---

## Phase 3 Output

A fully documented **Harness Configuration** listing every tool the agent has access to, how it was sourced (discovered vs. built), and how to configure it.

> Use the template at [`tool_discovery_report.md`](../resources/templates/tool_discovery_report.md) to document the discovery process.

> **Handoff Complete!** Once the tool discovery and execution plan are approved, your role as the Planner is finished. Provide the `execution_plan.md` to your external Agentic Scaffolder (e.g., ECC, Superpower, etc.) so it can begin the actual implementation.

---
description: "Phase 3: Tool Discovery, Evaluation & Creation. Equip the agent harness with the right tools. Always discover existing solutions before building custom ones."
phase: 3
checkpoint: false
---

# Phase 3: Tooling — Discover, Evaluate, Equip

> **Goal:** Equip the agent's **harness** with the tools it needs to execute the plan. This phase follows the paper's core principle: the agent = **Model + Harness**, and the harness is where engineering effort should be concentrated.

> **Critical Rule:** **DISCOVER before you BUILD.** For every capability needed, the agent must first search for existing, battle-tested tools. Only create custom tooling when no adequate solution exists or when integration cost exceeds build cost.

---

## Step 3.0 — Scaffold Consultation

Before discovering individual tools, check if an existing scaffold can jumpstart the entire project.

> **Consult [`SCAFFOLDS.md`](./SCAFFOLDS.md)** — the reference catalog of scaffolds, frameworks, harnesses, and starter templates organized by project type.

**Decision Matrix:**

| Situation | Action |
|-----------|--------|
| A scaffold exists that covers 80%+ of needs | **Adopt it.** Layer project-specific rules on top. |
| A scaffold covers 50-80% of needs | **Fork or extend it.** Fill gaps with individual tools below. |
| No adequate scaffold exists | **Proceed to Step 3.1** — assemble tools individually. |
| Starting from absolute zero (no codebase, no tech stack) | **Check Category 6 in SCAFFOLDS.md** for project-type starters (Next.js, FastAPI, etc.) and **Category 1** for agent harness scaffolds (ECC, agent-project, etc.) |

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
      → If YES: Install with `npx skills add <repo> --skill <name>`, evaluate (Step 3.3).

3. SEARCH MCP SERVER REGISTRIES
   └─ Is there an existing MCP server that provides this capability?
      Sources to check (in order):
      • registry.modelcontextprotocol.io — Official MCP registry
      • mcp.directory — Large searchable directory, one-click install
      • mcp.so — Marketplace browsable by category
      • smithery.ai — Registry with install commands
      • github.com/modelcontextprotocol/servers — Reference implementations
      • GitHub: "modelcontextprotocol" OR "mcp server" <your-capability>
      → If YES: Evaluate it (Step 3.3), then install/configure.

4. SEARCH PACKAGE REGISTRIES
   └─ Is there a well-maintained library/CLI that does this?
      Sources to check:
      • npm / PyPI / crates.io / Go modules (language-specific)
      • GitHub search for "[capability] CLI tool"
      • Awesome lists (e.g., awesome-mcp-servers, awesome-devtools)
      → If YES: Evaluate it (Step 3.3), then integrate.

5. SEARCH FOR EXISTING APIs
   └─ Is there a hosted API/service that provides this?
      Sources to check:
      • RapidAPI, Postman API Network
      • Official service documentation (e.g., GitHub API, Stripe API)
      → If YES: Evaluate it (Step 3.3), then integrate.

6. BUILD CUSTOM (Last Resort)
   └─ If nothing adequate was found in steps 1-5:
      • Document why existing solutions are insufficient.
      • Design the minimal custom tool needed.
      • Follow the Custom Tool Creation template (Step 3.3).
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
- **Score ≥ 4.0:** Adopt immediately.
- **Score 3.0–3.9:** Adopt with caveats (document limitations).
- **Score 2.0–2.9:** Consider building custom or look for alternatives.
- **Score < 2.0:** Reject.

---

## Step 3.4 — Custom Tool Creation (When Discovery Fails)

If no existing tool meets the need, create a minimal custom tool. Choose the right format:

| What You Need | Create | Guide |
|---------------|--------|-------|
| **Agent behavior / workflow / methodology** (e.g., debugging discipline, review process, deployment checklist) | A `SKILL.md` file | See [`templates/skill_creation_guide.md`](./templates/skill_creation_guide.md) — 5 proven body patterns, starter templates, quality checklist |
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

> **Proceed to [Phase 4: Implementation](./04_IMPLEMENTATION.md)** once the harness is assembled.

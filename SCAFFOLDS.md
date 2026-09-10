---
description: "Reference catalog of scaffolds, frameworks, and harnesses that can accelerate project implementation. Discover before you build."
alwaysApply: false
---

# Scaffold & Framework Reference

> **Purpose:** When starting a new project (Phase 3: Tooling), consult this catalog to find existing scaffolds, frameworks, and harnesses that can accelerate your implementation. This catalog is organized by what kind of project or task you are building.

> **Principle:** *"Discover before you build."* — Never start from zero when a battle-tested scaffold exists.

---

## How to Use This Catalog

1. **Identify your project type** from the categories below.
2. **Evaluate candidates** using the Tool Evaluation Matrix from [03_TOOLING.md](./03_TOOLING.md).
3. **Adopt the scaffold** that best fits, then layer your project-specific `AGENTS.md` and rules on top.

---

## Category 1: Agent Harness & Meta-Scaffolds

*These scaffolds structure how your AI agent operates. They provide the "operating system" layer on top of the model.*

| Scaffold | GitHub / Source | What It Does | Best For |
|----------|----------------|-------------|----------|
| **ECC (Everything Claude Code)** | [affaan-m/ECC](https://github.com/affaan-m/ECC) | A full harness OS for AI agents: skills, instincts, memory, security (AgentShield), context compaction. Enforces Plan → Test → Implement → Review → Verify → Remember → Improve. | Teams wanting a turnkey, opinionated agent harness with hundreds of pre-built skills |
| **agent-harness-generator** | [ruvnet/agent-harness-generator](https://github.com/ruvnet/agent-harness-generator) | Meta-harness that scaffolds your own branded agent environment. Manages skills, memory, and learning loops. | Building a custom-branded agent environment from scratch |
| **agent-project** | [SuperiorByteWorks-LLC/agent-project](https://github.com/SuperiorByteWorks-LLC/agent-project) | Production-grade template using `AGENTS.md` as entry point for repo standards, CI/CD integration, AI review policies. | Enterprise repos that need agent-friendly governance baked in |
| **CodelyTV/agent-harness** | [CodelyTV/agent-harness](https://github.com/CodelyTV/agent-harness) | Collection of skills, hooks, and utilities to enforce development conventions. | Teams wanting modular, plug-and-play quality enforcement |

### ECC Deep Dive (Reference Scaffold)

ECC is the most comprehensive example of a "harness as OS" approach. Key architectural patterns to learn from:

```
ECC Architecture:
├── Skills/          # Hundreds of specialized behaviors (TDD, security, architecture)
│   └── SKILL.md     # Each skill has instructions + scripts + resources
├── Agents/          # Specialized subagent definitions (reviewer, architect, security)
├── Rules/           # Always-active guardrails injected into every session
├── Memory/          # Persistent knowledge across sessions (team patterns, decisions)
├── Security/        # AgentShield — scans MCP servers, tool permissions, configs
└── Context/         # Strategic context compaction to optimize token budget
```

**Key Patterns from ECC:**
- **Selective Installation:** Don't load everything — pick only the skills/agents relevant to your project.
- **Memory Persistence:** Agent "remembers" team patterns, past decisions, and coding standards across sessions.
- **Security Scanning:** Agent audits its own tool permissions and MCP server configs for vulnerabilities.
- **Context Compaction:** Automatically compress intermediate results to stay within token budgets.

---

## Category 2: Orchestration Frameworks

*These provide the runtime infrastructure for multi-agent workflows, state management, and task routing.*

| Framework | Source | What It Does | Best For |
|-----------|--------|-------------|----------|
| **LangGraph** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Stateful multi-agent workflows as graphs. Built-in persistence, human-in-the-loop checkpoints, flow control. | Complex, production-grade orchestration logic |
| **CrewAI** | [crewai](https://github.com/joaomfg/crewai) | Role-based agent teams (coder, reviewer, researcher) collaborating on shared goals. | Multi-role collaboration projects |
| **Mastra** | [mastra.ai](https://mastra.ai/) | TypeScript-native framework with built-in agents, workflows, memory, and observability. | TypeScript-first teams wanting integrated DX |
| **Pydantic AI** | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | Type-safe agentic pipelines for Python with Pydantic validation. | Python teams prioritizing type safety |
| **OpenAI Swarm** | [openai/swarm](https://github.com/openai/swarm) | Lightweight agent handoffs and routing between specialized agents. | Simple multi-agent routing |
| **AutoGen** | [microsoft/autogen](https://github.com/microsoft/autogen) | Multi-agent conversation framework with code execution. | Research and experimentation |

---

## Category 3: Open-Source Coding Agents

*Drop-in alternatives or complements to commercial coding agents. Use these when you need a fully customizable agent.*

| Agent | Source | What It Does | Best For |
|-------|--------|-------------|----------|
| **OpenCode** | [opencode-ai/opencode](https://github.com/opencode-ai/opencode) | Dual-agent (Plan/Build) terminal coding agent. Wide model support, TUI. | Open-source alternative to Claude Code |
| **Aider** | [aider.chat](https://aider.chat/) | Terminal pair programmer with git-diff workflows. Preserves Git history. | Working within existing repos with clean git history |
| **Cline** | [cline/cline](https://github.com/cline/cline) | VS Code extension for multi-file autonomous edits with step-by-step oversight. | VS Code users wanting autonomous but supervised editing |
| **Kilo CLI** | [kilo-code/kilo](https://github.com/kilo-code/kilo) | Model-agnostic configurable agent connecting terminal to cloud/team workflows. | Teams needing flexible, cloud-connected terminal agent |

---

## Category 4: Context & Memory Tools

*These solve the "goldfish problem" — agents forgetting everything between sessions.*

| Tool | Source | What It Does | Best For |
|------|--------|-------------|----------|
| **Mem0** | [mem0.ai](https://mem0.ai/) | Universal memory layer with long-term, persistent context across sessions. | Preventing agent amnesia across sessions |
| **OpenViking** | Community | Context database as virtual filesystem (`viking://`). Agents browse history with `ls`, `tree`, `find`. | Teams wanting navigable agent memory |
| **SDL-MCP** | Community | Symbol Delta Ledger — compacts large codebases into high-signal context for coding agents. | Large codebases with token budget pressure |
| **Basemind** | Community | Unified context layer (code-maps, RAG, shared memory) over MCP. | Coding agents needing structured codebase awareness |

---

## Category 5: Agent Skills (SKILL.md Ecosystem)

*Modular, packaged expertise that extends what your agent can DO. Each skill is a `SKILL.md` file with instructions, scripts, and resources that agents auto-discover and activate on demand.*

### General-Purpose Skill Collections

| Skill Collection | Source | What It Does | Best For |
|-----------------|--------|-------------|----------|
| **addyosmani/agent-skills** | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 25 production SDLC skills by the author of "The New SDLC" paper. Slash-command mapped (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`). Includes red-flag detection, gated workflows, and `/build auto` mode. Works with 70+ harnesses. | **The single best starting point** for any project — enforces structured development across all phases |
| **thananon/9arm-skills** | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | Opinionated engineering meta-skills: `debug-mantra` (4-step debugging discipline), `scrutinize` (outsider code review), `qwenchance` (context budget + loop detection), `post-mortem` (canonical bug records). Bucketed into engineering/productivity/misc. | **Agent self-discipline** — debugging methodology, staying on track during long tasks, preventing looping |
| **VoltAgent/awesome-agent-skills** | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Curated collection of 1000+ real-world skills used by engineering teams. | Browsing for skills by category when you need something specific |
| **anthropics/skills** | [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic skill examples for creative, technical, and enterprise workflows. Includes the document creation skills (docx, pdf, pptx, xlsx) that power Claude's built-in features. | Learning the canonical SKILL.md patterns, creative + enterprise skills |

### Domain-Specific Skills

| Skill | Source | What It Does | Best For |
|-------|--------|-------------|----------|
| **Anthropic-Cybersecurity-Skills** | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 817 cybersecurity playbooks mapped to MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND. Covers threat intel, DFIR, red teaming, DevSecOps, cloud security. | Security audits in Phase 5, compliance verification, any project handling sensitive data |
| **detect-skill** | [resemble-ai/detect-skill](https://github.com/resemble-ai/detect-skill) | Deepfake/synthetic media detection via Resemble AI API. Audio fingerprinting, video forensics, source attribution. | Projects with user-generated media, content moderation, anti-fraud pipelines |
| **archify** | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Generates interactive, schema-validated architecture diagrams (architecture, workflow, sequence, data-flow, lifecycle) from code or specs. Typed JSON IR → deterministic HTML/SVG. | Phase 2 planning visualization, PR architecture diffs, living documentation |

### Creating Your Own Skills

When no existing skill covers your need, create a custom one using the **[Skill Creation Guide](./templates/skill_creation_guide.md)**.

The guide includes:
- **SKILL.md anatomy** — the two critical YAML fields and how to write effective trigger descriptions
- **5 body patterns** distilled from 850+ skills across 4 repos: Mantra, Gated Workflow, Decision Table, Outsider Review, Playbook
- **Starter templates** — copy-paste skeletons for engineering and guardrail skills
- **Harness installation paths** — where each agent looks for skills
- **Quality checklist** — 9-point verification before shipping

### Key Pattern: How Skills Work
```
my-project/
├── .claude/skills/          # Claude Code auto-discovers these
├── .cursor/skills/          # Cursor auto-discovers these
├── .gemini/config/skills/   # Antigravity auto-discovers these
└── skills/
    └── my-custom-skill/
        ├── SKILL.md          # Instructions + YAML frontmatter (name, description, use_when)
        ├── scripts/          # Helper scripts the skill can invoke
        ├── references/       # Documentation the skill can read
        └── examples/         # Reference implementations
```

**Install pattern:** `npx skills add addyosmani/agent-skills --skill <name>`

---

## Category 6: Codebase Intelligence & Memory (MCP Servers)

*MCP servers that give agents deep understanding of existing codebases and persistent memory across sessions.*

| Tool | Source | What It Does | Best For |
|------|--------|-------------|----------|
| **codebase-memory-mcp** | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Parses code via Tree-Sitter into a persistent SQLite knowledge graph. 14+ MCP tools: `search_graph`, `trace_call_path`, `query_graph` (Cypher), impact analysis, dead-code detection. ~120x more token-efficient than file reading. Single binary, zero dependencies, 100% local. | **Any project with an existing codebase** — Phase 2 context gathering, Phase 4 impact analysis before refactoring |
| **Mem0** | [mem0.ai](https://mem0.ai/) | Universal memory layer — persistent long-term context across agent sessions. | Preventing agent amnesia, remembering team patterns and decisions |
| **SDL-MCP** | Community | Symbol Delta Ledger — compacts large codebases into high-signal context. | Large monorepos with tight token budgets |
| **Basemind** | Community | Unified context layer (code-maps, RAG, shared memory) over MCP. | Multi-agent coding setups needing shared codebase awareness |
| **MCP Memory Server** | [Official](https://github.com/modelcontextprotocol/servers) | Stores entities, relations, and observations in local JSONL. | Lightweight project memory without full knowledge graph |

---

## Category 7: Repository Automation Scaffolds

*For CI/CD, issue management, PR workflows, and repo-level automation.*

| Scaffold | Source | What It Does | Best For |
|----------|--------|-------------|----------|
| **GitHub Agentic Workflows (gh-aw)** | [GitHub Next](https://githubnext.github.io/gh-aw) | Define workflows in Markdown → compiled to GitHub Actions. MemoryOps for state across runs. | Repository automation (triage, PR reviews, docs) |
| **harness/harness-skills** | [harness/harness-skills](https://github.com/harness/harness-skills) | Natural language CI/CD pipeline integration. | DevOps teams wanting NL-driven pipelines |

---

## Category 8: Project-Type Starter Templates

*When you know what kind of app you're building, start with a domain-specific scaffold.*

| Project Type | Recommended Scaffolds | Notes |
|-------------|----------------------|-------|
| **Web App (Full-Stack)** | Next.js starter, T3 Stack, create-react-app | Layer your AGENTS.md on top |
| **API / Backend** | FastAPI template, Express generator, Hono starter | Add OpenAPI spec for agent context |
| **CLI Tool** | oclif, Commander.js, Click (Python), Clap (Rust) | Agents excel at CLI tools |
| **Mobile App** | Expo (React Native), Flutter starter | Specify platform constraints in Intent Brief |
| **Data Pipeline** | Dagster, Prefect, Airflow starters | Map pipeline DAG to execution plan |
| **ML / AI Project** | Cookiecutter Data Science, Lightning AI template | Include model eval in Definition of Done |
| **Browser Extension** | Plasmo, WXT, chrome-extension-boilerplate | Tight security constraints needed |
| **MCP Server** | MCP TypeScript SDK, MCP Python SDK | Use official SDK templates |
| **Documentation Site** | Docusaurus, Astro Starlight, MkDocs | Agents can generate + maintain docs |

---

## How Scaffolds Fit Into the Workflow

```
Phase 1: DISCOVERY
  └─ Define WHAT you're building
       │
Phase 2: PLANNING
  ├─ Choose tech stack
  └─ Use codebase-memory-mcp (Cat 6) to understand existing code
       │
Phase 3: TOOLING  ◄──── CONSULT THIS CATALOG
  ├─ Pick an Agent Harness (Category 1-2)
  ├─ Pick a Coding Agent (Category 3)
  ├─ Install relevant Agent Skills (Category 5)
  ├─ Add Codebase Intelligence MCP servers (Category 6)
  ├─ Set up Automation scaffold (Category 7)
  └─ Pick a Project starter template (Category 8)
       │
Phase 4: IMPLEMENTATION
  ├─ Execute using the assembled scaffold + harness
  └─ Skills like /build, /test, /review guide each step
       │
Phase 5: VERIFICATION
  ├─ Security skills (Cybersecurity-Skills) for audit
  ├─ archify for architecture diff verification
  └─ codebase-memory-mcp for dependency impact analysis
       │
Phase 6: DELIVERY
  └─ archify for living documentation diagrams
```

---

## 🔍 Discovery Guide: How to Find More Tools Like These

The landscape of agent skills, MCP servers, and scaffolds evolves weekly. Here is a systematic approach to finding new tools when this catalog doesn't cover your need.

### Tier 1: Registries & Directories (Search Here First)

| Registry | URL | What It Indexes |
|----------|-----|----------------|
| **Official MCP Registry** | https://registry.modelcontextprotocol.io/ | Authoritative MCP server registry, community-owned |
| **MCP.Directory** | https://mcp.directory/ | Thousands of MCP servers, one-click install paths |
| **MCP.so** | https://mcp.so/ | Searchable marketplace by category (DB, search, dev tools) |
| **Smithery** | https://smithery.ai/ | MCP server registry with install commands |
| **Skills Hub** | https://skills-hub.ai/ | Agent skills aggregated from GitHub repos |
| **AgenticSkills.io** | https://agenticskills.io/ | Security-audited MCP servers and skills |
| **Awesome MCP Servers** | https://github.com/modelcontextprotocol/servers | Official reference implementations |
| **awesome-agent-skills** | https://github.com/VoltAgent/awesome-agent-skills | 1000+ curated skills for coding agents |

### Tier 2: GitHub Search Patterns

When registries don't have what you need, search GitHub directly using these queries:

```
# Find SKILL.md-based agent skills
"SKILL.md" in:path <your-domain>

# Find MCP servers by capability
"modelcontextprotocol" OR "mcp server" <your-capability>

# Find agent rules/configuration repos
"AGENTS.md" OR "CLAUDE.md" OR ".cursorrules" <your-tech-stack>

# Find specific skill types
"agent-skill" OR "claude-code-skill" <your-domain>

# Find tool collections
topic:mcp-server OR topic:agent-skills OR topic:agentic-workflow
```

### Tier 3: Package Registries

| Registry | Search For | Example |
|----------|-----------|---------|
| **npm** | `npx skills search <keyword>` | `npx skills search security` |
| **npm** | Search `mcp-server-*` packages | `npm search mcp-server-postgres` |
| **PyPI** | Search `mcp-server-*` packages | `pip search mcp-server` |
| **crates.io** | Search `mcp` tagged crates | For Rust MCP servers |

### Tier 4: Community & Social

| Source | What to Look For |
|--------|-----------------|
| **GitHub Trending** | Repos tagged `mcp`, `agent-skills`, `agentic` |
| **Reddit** | r/ClaudeAI, r/cursor, r/LocalLLaMA for community tools |
| **X/Twitter** | Follow @anthropaborgs, @addyosmani, @mcaborgs for skill announcements |
| **Discord** | Claude Code, Cursor, Cline community servers |

### Evaluation Checklist for New Discoveries

Before adopting any discovered tool, verify:

- [ ] **Last commit < 3 months ago** — actively maintained?
- [ ] **Stars / forks** — community validation signal
- [ ] **README quality** — can the agent understand how to use it?
- [ ] **License** — compatible with your project?
- [ ] **Security** — does it need file access, network access, or API keys? Is that justified?
- [ ] **SKILL.md / MCP compliance** — follows the standard format?
- [ ] **Cross-harness** — works with your specific agent (Claude Code, Cursor, Antigravity, etc.)?

---

## Contributing to This Catalog

After each project retrospective (Phase 6), update this catalog:
- Add scaffolds, skills, and MCP servers you discovered and found useful.
- Remove entries that are deprecated or unmaintained.
- Update notes based on real-world experience.
- Add new GitHub search patterns that yielded good results.

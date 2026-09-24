# Scaffold and framework discovery map

Use this as a **starting map**, not an approved install list or a complete catalog. Being listed here is not evidence that a tool is better. Start with the project requirements and existing capabilities, include no new tool as a candidate, and search outside this map when relevant.
First inspect the target project and its existing workflow. Keep a working stack;
for a new project, look in the row matching the product. Search beyond these
examples when the requirement calls for it. Recheck official documentation,
current versions, host/OS support, and setup steps before recommending anything.

| Need | Starting points | Look for | Avoid when |
| --- | --- | --- | --- |
| A coding workflow after planning | [Superpowers](https://github.com/obra/superpowers), [ECC](https://github.com/affaan-m/ECC) | Whether the chosen coding host is supported and whether its planning/review steps overlap with IntentFlow | The current agent workflow already implements the plan adequately |
| A new web app | [Next.js starter](https://nextjs.org/docs/app/getting-started/installation), [Vite starter](https://vite.dev/guide/) | Server-rendering/full-stack needs versus a simpler client app, deployment target, team stack | The repository already has a working web framework |
| A new Python API | [FastAPI project guidance](https://fastapi.tiangolo.com/project-generation/) | Whether an API-only app is enough or the full-stack template's database, frontend, and operations are actually needed | A small existing service only needs a route or two |
| A new mobile app | [Expo create-a-project](https://docs.expo.dev/get-started/create-a-project/) | Android/iOS requirements, native modules, build and device workflow | Mobile is only an optional future interface |
| An application that itself runs agent workflows | [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), [CrewAI](https://docs.crewai.com/en/introduction) | Durable state and control flow versus role-based collaboration; evaluation and operational burden | AI is only the coding assistant, not part of the delivered product |
| A coding agent needs access to a service or browser | [AXI catalog](https://axi.md/), the service owner's CLI or API, or a supported MCP/connector | Whether a specific tool covers the required operation, works in the current host/OS, and improves on what is already installed | Access is not needed or an existing tool is sufficient |
| A service that exposes tools to agents | [MCP SDKs](https://modelcontextprotocol.io/docs/sdk) | Existing official SDK and client compatibility | A normal API or CLI already meets the requirement |

For a skill or external integration, search the current coding host's official
skill/plugin documentation and the service owner's documentation. A repository
link alone is not an installation instruction. Check what gets copied or replaced,
especially `AGENTS.md`, `.agents/`, and host-specific config.

For AXI, inspect the individual tool's own source and current instructions; the catalog includes community entries with different maintainers. Do not infer cost or speed benefits for the project from a catalog claim alone.

Compare the relevant lead with **no new scaffold** and, when the choice is
consequential, one alternative. Record the reason for the choice in `PLAN.md`.
Put only selected, verified setup steps in `SETUP.md`; mark unresolved items as
such. Do not copy old starter code into the plan or install from this map.

# IntentFlow

**Describe your idea. Answer a few useful questions. Get a plan and a setup guide.**

One planner command runs the whole process:

`grill-with-docs questions → plan → tool and skill selection → setup guide`

You do not need to call `grill-with-docs` separately. It asks for missing details,
records your answers, and passes them back to the planner. If your idea is already
clear, it skips unnecessary questions.

## 1. Put the skills in your project

If you are using this repository, they are already here.

For another project, copy **both complete folders**, including their contents:

```text
your-project/
└── .agents/
    └── skills/
        ├── planner/
        └── grill-with-docs/
```

Keep your project's existing files. Do not replace its whole `.agents` folder.
IntentFlow itself needs no package installation. If you use Claude Code or Cline,
also copy this repository's `.claude/skills/planner/` and
`.claude/skills/grill-with-docs/` folders into the same paths in your project.
These small adapters point to the canonical `.agents/skills/` files, so copy both
sets together. For Gemini CLI or OpenCode, also copy the relevant `planner` command
file from `.gemini/commands/` or `.opencode/commands/` if you want `/planner`.

The root `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` describe **this IntentFlow
repository**. Do not overwrite a target project's own instruction files with
them. In a target project with an existing root `AGENTS.md`, a new `CLAUDE.md`
can contain `@AGENTS.md` and a new `GEMINI.md` can contain `@./AGENTS.md` if those
hosts need to read the same project rules. Merge with any existing host files.

## 2. Start the planner

Open your project in your coding tool and start a new chat.

Use the form for your coding tool, followed by your idea:

| Coding tool | Start with | Extra files needed |
| --- | --- | --- |
| [Antigravity](https://antigravity.google/docs/migration/workflows-to-skills) | `/planner` | None |
| [Codex](https://developers.openai.com/plugins/build/skills) | `$planner` | None |
| [Cursor](https://prod.cursor.com/docs/skills) | `/planner` in Agent chat | None |
| [Claude Code](https://code.claude.com/docs/en/skills) | `/planner` | Both `.claude/skills/` adapters |
| [Gemini CLI](https://geminicli.com/docs/cli/custom-commands/) | `/planner` | `.gemini/commands/planner.toml` |
| [OpenCode](https://opencode.ai/docs/commands) | `/planner` | `.opencode/commands/planner.md` |
| [Cascade / Devin Desktop](https://docs.devin.ai/desktop/cascade/skills) | `@planner` | None |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | `Use the planner skill to ...` | None |
| [Cline](https://docs.cline.bot/customization/skills) | `Use the planner skill to ...` | Both `.claude/skills/` adapters |

Gemini CLI may ask you to activate the skill. These are documented discovery
paths and invocation forms; this repository has not been live-tested in every
coding tool. If your tool does not show the skill, check its skill list and
restart or refresh the session after copying files.

If the shortcut is not recognized, use this in any coding agent with file access:

```text
Read .agents/skills/planner/SKILL.md and follow the complete workflow.
My idea is: [describe your idea].
```

## 3. Answer the questions

The planner uses `grill-with-docs` to ask about who the project is for, what it
should do, and constraints that change the design. It asks a few questions at a
time and continues automatically after you answer.

You can say **"Use sensible defaults for the remaining details"** at any time.
It will record its assumptions instead of asking about every small choice.

## 4. Use the two output files

The files go together in your project's documentation folder, or its root if
there is no existing convention. Existing plans are reused where appropriate.

| File | What's inside | What you do with it |
| --- | --- | --- |
| `PLAN.md` | Scope, decisions, acceptance checks, and implementation tasks | Give it to your coding agent or chosen development workflow |
| `SETUP.md` | Required tools and skills, versions, sources, install steps, and verification | Follow it yourself or use its included AI setup prompt |

**To install things yourself:** open `SETUP.md` and follow "Install in order."
Already installed items are checked first. Optional tools stay separate.

**To let an AI install them:** give a coding AI `SETUP.md` and the relevant project
files, then send the prompt in "Let an AI do the setup." It will check the machine,
install the required verified items, and report the results. It needs command or
browser access; sign-in and other human-only steps may still need you.

**To start building after setup:**

```text
Read PLAN.md and SETUP.md. Implement the plan in this project and run its checks.
```

Use the actual paths if the files are in a documentation folder. Planning creates
instructions; it does not install or build until you ask. If nothing new is needed,
`SETUP.md` says so. If a tool choice cannot yet be verified, it marks that item
unresolved instead of giving you guessed installation commands.

## When to use it

Use IntentFlow when you want to clarify an idea and prepare a handoff. It may
recommend a smaller version, an experiment, or not building yet. If your existing
workflow already does this well, you can use that directly.

## For maintainers

- [Shared project instructions](AGENTS.md)
- [Planner instructions](.agents/skills/planner/SKILL.md)
- [Interview skill](.agents/skills/grill-with-docs/SKILL.md)
- [Claude and Cline planner adapter](.claude/skills/planner/SKILL.md)
- [OpenCode planner command](.opencode/commands/planner.md)
- [Plan template](.agents/skills/planner/resources/templates/execution_plan.md)
- [Setup template](.agents/skills/planner/resources/templates/setup.md)
- [Scaffold discovery map](.agents/skills/planner/references/SCAFFOLDS.md)
- [Behavioral evaluation cases](.agents/skills/planner/references/EVALUATION.md)

Check local documentation links and the link-checker regression tests:

```sh
python scripts/verify_links.py
python -B -m unittest discover -s scripts -p "test_*.py"
```

These checks do not prove planning quality or test command discovery in each host.

# References Directory

This directory is intended for **immutable project context**. 

This shipped directory is read-only during project work. Place project-specific reference materials in an explicitly approved directory in the target project, not here. Record that directory's exact path in the execution plan. 

### Examples for the approved target-project reference directory:
- API Documentation PDFs or Markdown exports
- Brand guidelines and design tokens
- External library guides or SDK docs that aren't well-known by the base model
- Examples of code architecture you want the agent to mimic
- Database schemas from external systems

> **Rule of Thumb:** Read shipped templates as sources only. Create `INTENT_BRIEF.md`, `CONTEXT.md`, and `EXECUTION_PLAN.md` at the target project root, and other live artifacts at approved paths recorded in the plan. Keep external reference material in the approved target-project reference directory. Never store project outputs in shipped `resources/templates/` or `resources/references/`.

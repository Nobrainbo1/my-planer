# References Directory

This directory is intended for **immutable project context**. 

As an Orchestrator, you should place reference materials here that you want the agent to read but **not modify**. 

### Examples of what goes here:
- API Documentation PDFs or Markdown exports
- Brand guidelines and design tokens
- External library guides or SDK docs that aren't well-known by the base model
- Examples of code architecture you want the agent to mimic
- Database schemas from external systems

> **Rule of Thumb:** If it's a living document that changes during the project (like an Execution Plan), put it in `templates/` or the root. If it's a fixed reference from the outside world, put it in `references/`.

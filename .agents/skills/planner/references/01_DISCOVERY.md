# Discovery: decide what is worth building

Use this reference for uncertain ideas. Skip questions already answered by the
user, existing documents, or repository evidence.

## Find the decision that changes the plan

Start with the intended user, their current workflow, the painful step, and an
observable improvement. Establish the smallest useful outcome before selecting a
stack. A technology preference is a constraint, not evidence of a user need.

Consider the cheapest credible alternative: keep the current process, change it
manually, configure an existing product, extend the current project, or build.
State why the recommended route fits. If demand is speculative, propose a cheap
way to learn whether the problem exists before designing a large system.

Inspect repository facts such as manifests, relevant code, tests, and deployment
configuration. Record paths or sources for consequential findings. Keep observed
facts separate from assumptions; lack of access is an unknown, not an invitation
to invent what the repository contains.

## Ask small, useful rounds

Ask one to three questions at a time, starting with the choice that unlocks the
most work. Offer two or three realistic options with a recommendation and its
trade-off when that helps. Let the user propose a different answer.

For example, decide whether a booking tool serves one shop or independent shops
before asking about account isolation. Keep dependent choices pending until the
parent choice is resolved. Do not show a large decision tree unless it helps.

Update the working plan with each resolved choice, scope effect, and any domain
term whose meaning matters. A short terms section is sufficient; a separate
glossary is useful only when terminology is extensive or already maintained.

If the user says to use your judgment, choose reversible defaults and label them.
If a consequential unknown cannot be decided within that delegation, record the
blocker and continue independent work. Silence is not agreement.

## Stop when the next step is clear

Discovery is sufficient when the first-version outcome, scope, success checks,
constraints, and consequential decisions are clear enough for the next task.
Defer polish and distant features. Do not keep interviewing for completeness.

For a feasibility route, specify the hypothesis, smallest experiment, time or cost
limit, success/failure threshold, and what each result changes. Planning the
experiment does not mean it ran. Execute it only when included in the user's scope.

A conclusion of "do not build yet" should state why, what to do instead, and what
new evidence would justify reconsidering it. Do not manufacture a software plan
after recommending that no software is needed.

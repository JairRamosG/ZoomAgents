# How work is organized

## Source of truth

The task backlog lives in `_docs/outdated/tasks.md`. Each task becomes a GitHub
issue. Issues are the unit of work — not PRs, not branches, not mental notes.

## Issue lifecycle

```
tasks.md  →  GitHub issue  →  Groomed by PM  →  Labeled  →  Implemented  →  Merged
```

1. **Create**: Every task in `tasks.md` gets a GitHub issue with title,
   description, and dependencies.
2. **Groom**: The PM rewrites each issue using `_docs/task_template.md` — clear
   goal, checkable acceptance criteria, out-of-scope items with follow-up
   links, and constraints.
3. **Label**: Issues get `MVP` or `post-MVP` to define scope. All out-of-scope
   items from grooming become `post-MVP` follow-up issues.
4. **Implement**: An engineer picks a groomed issue, creates a branch, and
   implements it. Commits reference the issue number.
5. **Review & Merge**: PRs are reviewed and merged to `main`.

## Labels

| Label | Meaning |
|-------|---------|
| `enhancement` | Applied automatically on issue creation |
| `MVP` | Part of the MVP scope — must ship |
| `post-MVP` | Future work — not blocking the MVP |

## Dependency discipline

Every issue states its dependencies explicitly ("Depends on: Task #N"). An issue
with unmet dependencies is not ready for implementation. The dependency graph
lives in the issues themselves, not in a separate document.

## Rules

- Tasks are GitHub issues. Not Slack messages, not verbal agreements.
- Commit regularly. Small, focused commits tied to an issue.
- Every issue must be groomed before implementation starts.
- An engineer who has never spoken to the PM should be able to implement an
  issue from the issue body and the documents it links.

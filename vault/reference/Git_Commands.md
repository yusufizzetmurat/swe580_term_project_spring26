---
tags: [reference, git]
created: 2026-01-04T10:00:00
modified: 2026-01-10T12:00:00
---

# Git Commands

Quick reference for git operations I use regularly.

## Branching

- `git branch feature-x` — create branch
- `git checkout -b feature-x` — create and switch
- `git branch -d feature-x` — delete merged branch

## Merging

- `git merge feature-x` — merge into current branch
- `git rebase main` — rebase current branch onto main
- `git cherry-pick abc123` — apply specific commit

## Stashing

- `git stash` — save uncommitted changes
- `git stash pop` — restore and remove stash
- `git stash list` — show all stashes

## Common Workflows

Feature branch workflow: branch from main, develop, PR, merge, delete branch. Always pull before pushing.

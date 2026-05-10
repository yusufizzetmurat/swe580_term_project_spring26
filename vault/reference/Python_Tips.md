---
tags: [reference, python]
created: 2026-01-05T09:00:00
modified: 2026-01-20T08:00:00
---

# Python Tips

A collection of useful Python patterns and tricks I keep coming back to.

## List Comprehensions

Nested comprehensions for flattening: `[x for sublist in nested for x in sublist]`

## Decorators

Use `functools.wraps` to preserve function metadata. Common patterns: timing, caching, retry logic.

## Context Managers

The `with` statement for resource management. Write custom ones using `contextlib.contextmanager`.

## Virtual Environments

Always use venv or conda. Never install packages globally. `python -m venv .venv` is the standard approach.

## Debugging

- `breakpoint()` drops into pdb (Python 3.7+)
- `python -m pdb script.py` for post-mortem debugging
- `icecream` library for better print debugging

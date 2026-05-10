---
tags: [reference, linux]
created: 2026-01-02T08:00:00
modified: 2026-01-08T10:00:00
---

# Linux Commands

Essential command-line tools for daily work.

## File Navigation

- `ls -la` — list with details and hidden files
- `find . -name "*.py"` — find files by pattern
- `tree -L 2` — visualize directory structure

## Permissions

- `chmod 755 script.sh` — make executable
- `chown user:group file` — change ownership

## Process Management

- `ps aux | grep python` — find running processes
- `kill -9 PID` — force kill
- `htop` — interactive process viewer

## Text Processing

- `grep -r "pattern" .` — recursive search
- `awk '{print $1}' file` — extract columns
- `sed 's/old/new/g' file` — find and replace

## Shell Scripting

Use `#!/bin/bash` shebang. Variables: `$VAR`. Conditionals: `if [ condition ]; then`. Loops: `for f in *.py; do`.

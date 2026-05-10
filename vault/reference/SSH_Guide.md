---
tags: [reference, tools, devops]
created: 2026-01-28T10:00:00
modified: 2026-01-28T10:00:00
---

# SSH Guide

Reference for working efficiently with remote servers — GPU cluster, lab machines, cloud instances. The right SSH setup eliminates most of the friction of remote work.

## SSH Config File

Put this in `~/.ssh/config`:

```
Host gpu01
    HostName gpu01.cs.university.edu
    User myusername
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60

Host gpu-jump
    HostName bastion.cs.university.edu
    User myusername
    IdentityFile ~/.ssh/id_ed25519
```

After this, `ssh gpu01` works instead of typing the full command. `ServerAliveInterval` prevents idle connections from dropping during long training runs.

## Key-Based Authentication

```bash
ssh-keygen -t ed25519 -C "email@university.edu"   # generate key (ed25519 is better than RSA)
ssh-copy-id gpu01                                   # install public key on remote
```

Always use key-based auth. Password auth is both less secure and slower.

## Port Forwarding

```bash
# Forward remote port 8888 (Jupyter) to local port 8888
ssh -L 8888:localhost:8888 gpu01

# Forward remote TensorBoard
ssh -L 6006:localhost:6006 gpu01
```

Use this to access Jupyter notebooks and [[Docker_Setup]] services running on the GPU server from a local browser.

## tmux for Persistent Sessions

Long training runs must run in tmux — if SSH disconnects, the process dies without it.

```bash
tmux new -s training        # new session named "training"
# ... start your training job ...
Ctrl+B, D                   # detach (session keeps running)
tmux attach -t training     # reattach from any connection
tmux ls                     # list sessions
```

Never run a long training job outside tmux. See [[Bash_Scripting]] for job submission via SLURM (preferred for cluster jobs).

## SCP and rsync

```bash
scp local_file.py gpu01:/scratch/project/     # copy single file
rsync -avz --progress local_dir/ gpu01:/scratch/project/dir/  # sync directory
rsync -avz --exclude=".git" --exclude="__pycache__" project/ gpu01:/scratch/project/
```

`rsync` is better than `scp` for directories — it only transfers changed files, shows progress, and handles interruptions gracefully.

## Checking GPU Usage

```bash
ssh gpu01 "nvidia-smi"          # quick check
ssh gpu01 "watch -n 1 nvidia-smi"   # live monitoring
```

Before submitting a large job, check that the GPUs aren't already fully utilized by other users.

## See Also

[[Linux_Commands]] for command reference, [[Docker_Setup]] for containerized remote services, [[Bash_Scripting]] for automating remote workflows.

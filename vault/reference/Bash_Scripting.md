---
tags: [reference, linux, tools]
created: 2026-01-27T09:00:00
modified: 2026-01-27T09:00:00
---

# Bash Scripting

Reference for writing reliable shell scripts. Most of my scripting is for ML workflow automation — submitting GPU jobs, running experiments in sequence, processing files in bulk.

## Script Header

```bash
#!/bin/bash
set -euo pipefail
```

These three options should be on every script:
- `set -e`: exit immediately on error
- `set -u`: treat unset variables as errors
- `set -o pipefail`: propagate errors through pipes (without this, `cmd1 | cmd2` returns cmd2's exit code even if cmd1 failed)

## Variables

```bash
NAME="experiment_v1"
DATA_DIR="/scratch/data"
OUTPUT="${DATA_DIR}/${NAME}/results"

echo "Running ${NAME}"          # always quote variable expansions
mkdir -p "${OUTPUT}"
```

Always double-quote variable expansions — unquoted variables break on spaces in paths and filenames.

## Loops

```bash
# Over files
for f in data/*.json; do
    python process.py "$f" --output "${f%.json}_processed.json"
done

# Over values
for lr in 1e-5 2e-5 5e-5; do
    python train.py --learning-rate "$lr"
done
```

The `${f%.json}` pattern strips the `.json` suffix from the filename — very useful for generating output filenames from input filenames.

## Submitting GPU Jobs

```bash
sbatch --gres=gpu:1 --mem=32G --time=12:00:00 --wrap="python train.py --config config.yaml"
```

We use SLURM for cluster job submission. The `--wrap` flag lets you submit inline commands without a job script file.

## Parallel Execution

```bash
# Run multiple experiments in parallel (background)
python train.py --config config_a.yaml &
python train.py --config config_b.yaml &
wait   # wait for all background jobs to finish

echo "All experiments done"
```

For more sophisticated parallelism, use GNU Parallel:

```bash
parallel python train.py --lr {} ::: 1e-5 2e-5 5e-5
```

## Useful Patterns

```bash
# Check if file exists
if [ -f "checkpoint.pt" ]; then
    echo "Resuming from checkpoint"
fi

# Capture command output
RESULT=$(python evaluate.py --model checkpoint.pt)
echo "F1: ${RESULT}"

# Redirect output to log file
python train.py 2>&1 | tee train.log
```

## See Also

[[Linux_Commands]] for individual command reference, [[SSH_Guide]] for running scripts on remote servers.

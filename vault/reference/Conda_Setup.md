---
tags: [reference, tools, python]
created: 2026-01-23T09:00:00
modified: 2026-01-29T11:00:00
---

# Conda Setup

Reference for managing Python environments with Conda. I use Conda for GPU-dependent projects where pip + venv sometimes causes CUDA compatibility issues, and venv for everything else (see [[Python_Tips]]).

## Creating Environments

```bash
conda create -n myenv python=3.10
conda activate myenv
conda deactivate
```

Always specify a Python version. Never use the base environment for actual work.

## Installing Packages

```bash
conda install numpy pandas
conda install -c conda-forge whoosh     # use conda-forge for packages not in defaults
pip install transformers                # pip within conda env is fine
```

Mixing conda and pip is unavoidable for ML projects. Best practice: install conda packages first, then pip packages. Never run `conda install` after `pip install` in the same env — it can break pip-installed packages.

## Environment Files

```bash
conda env export > environment.yml      # full export (platform-specific)
conda env export --from-history > environment.yml  # only explicitly installed packages (portable)
conda env create -f environment.yml
```

Use `--from-history` for sharing across platforms (Linux GPU server vs Mac laptop).

## Useful Commands

```bash
conda env list                          # list all environments
conda env remove -n myenv               # delete an environment
conda clean --all                       # free up disk space from cached packages
conda update conda                      # update conda itself
```

## CUDA Compatibility

This is why I use Conda over venv for GPU projects. Conda manages CUDA and cuDNN versions alongside Python packages:

```bash
conda install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
```

This installs CUDA 11.8 without touching the system CUDA installation. Critical on shared GPU servers where the system CUDA version may differ from what PyTorch needs.

## Integration with [[Docker_Setup]]

When containerizing a Conda environment, use the `continuumio/miniconda3` base image. Alternatively, export to `environment.yml` and install inside the container at build time.

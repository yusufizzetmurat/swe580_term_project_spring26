---
tags: [reference, python, tools]
created: 2026-01-29T09:00:00
modified: 2026-02-01T10:00:00
---

# Jupyter Tips

Patterns for productive Jupyter notebook work. Useful for exploration and visualization; for production code, move logic to Python modules.

## Magic Commands

```python
%timeit some_function()          # benchmark execution time
%time some_function()            # single run timing
%matplotlib inline               # render plots in notebook
%load_ext autoreload             # enable autoreload
%autoreload 2                    # reload all modules before executing cells

%%bash                           # run cell as bash script
ls -la
```

`autoreload 2` is essential when working with custom modules — changes to imported code take effect without restarting the kernel.

## Remote Kernels

For GPU work, run the kernel on a remote server and connect the browser locally:

```bash
# On GPU server (inside tmux):
jupyter notebook --no-browser --port=8888

# On local machine:
ssh -L 8888:localhost:8888 gpu01
```

Then open `localhost:8888` in the local browser. See [[SSH_Guide]] for the port forwarding setup.

## Kernel Management

```bash
# List available kernels
jupyter kernelspec list

# Install a conda environment as a kernel
conda activate myenv
pip install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

Each project should have its own kernel corresponding to its [[Conda_Setup]] environment.

## Useful Extensions (JupyterLab)

- **Variable Inspector**: shows current variables and their shapes — useful for debugging tensor dimensions
- **Table of Contents**: navigation sidebar for long notebooks
- **Git integration**: shows diff of notebook changes

## Best Practices

- Keep notebooks for exploration only. Extract stable code to `.py` modules that can be imported, tested, and version-controlled properly.
- Clear all outputs before committing to Git (`Kernel > Restart & Clear Output`). Notebook outputs in Git diffs are unreadable.
- Number cells are misleading — execution order matters, not cell order. Restart and run all before treating results as final.

## Visualization

```python
from IPython.display import display, HTML
display(df.head(10))                    # renders as table
display(HTML(fig.to_html()))            # embed Plotly figure
```

See [[Matplotlib_Guide]] for static figure generation and [[Pandas_Tips]] for DataFrame display options.

---
tags: [project, visualization]
created: 2026-01-15T10:00:00
modified: 2026-01-22T11:00:00
---

# Model Dashboard

A Streamlit-based dashboard for visualizing model training metrics and experiment results.

## Features

- Real-time training loss and accuracy charts
- Hyperparameter comparison across runs
- Model performance breakdown by dataset split
- Confusion matrix and error analysis views

## Data Source

Reads experiment data from the [[Experiment_Tracker]] JSON output format.

## Status

First version working. Demonstrated at the lab standup and received good feedback. Plan to add more interactive filtering options.

## Tech Stack

Streamlit for the UI, Plotly for interactive charts, pandas for data manipulation.

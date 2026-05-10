---
tags: [project, python]
created: 2026-01-06T08:00:00
modified: 2026-01-18T17:00:00
---

# Experiment Tracker

A lightweight tool for logging ML experiment configurations, metrics, and results.

## Features

- Log hyperparameters, metrics, and artifacts for each run
- Compare runs side by side
- Export results to CSV for further analysis
- Integration with MLflow for visualization

## Design

Each experiment is stored as a JSON file with model versioning. The tracker supports tagging runs and filtering by metric thresholds.

## Current Users

Used by [[Paper_Recommender]] for tracking embedding model experiments and by [[Dataset_Cleaner]] for benchmarking different cleaning strategies.

## Planned Improvements

- Add a web dashboard using [[Model_Dashboard]]
- Support distributed experiment logging

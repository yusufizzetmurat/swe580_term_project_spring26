---
tags: [project, python, data]
created: 2026-01-31T14:00:00
modified: 2026-02-04T11:00:00
---

# Annotation Tool

A lightweight web interface for labeling data across multiple projects. Replaced a growing collection of shared Google Sheets that were becoming unmanageable as the annotation volume increased.

## Background

We had three concurrent annotation efforts:
- [[Sentiment_Analyzer]]: labeling review sentiment
- [[Chatbot_Prototype]]: rating chatbot response quality
- [[Dataset_Cleaner]]: flagging problematic papers for exclusion

Managing these through spreadsheets meant no version control, no inter-annotator agreement tracking, and no way to prioritize examples.

## Implementation

Flask backend, simple HTML/CSS/JS frontend. Deliberately minimal — the goal is low friction for annotators, not a feature-rich platform.

Each task has a configuration file specifying:
- Data source (CSV or database)
- Label schema (binary, multiclass, rating scale)
- Instructions for annotators (displayed on screen)
- Whether to enable inter-annotator overlap (for agreement tracking)

## Inter-Annotator Agreement

For each annotation task, 15% of examples are shown to multiple annotators. Cohen's kappa is computed automatically and displayed in the admin dashboard. Tasks with kappa < 0.6 trigger a guidelines review.

## Integration with [[Active_Learning_System]]

The active learning system feeds the annotation tool a prioritized queue: the most uncertain model predictions are annotated first. This reduced total annotation effort by roughly 30% on the sentiment task while maintaining the same final model quality.

## Deployment

Running on a lab server behind the university VPN. Accessible to all lab members. Data stored in SQLite for simplicity — no need for a heavier database at our scale.

## Data Export

Exports completed annotations as CSV or JSON, compatible with the [[Fine_Tuning_Pipeline]] data loading format and the [[Data_Pipeline]] preprocessing stage.

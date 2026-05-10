---
tags: [project, python]
created: 2026-01-07T09:00:00
modified: 2026-01-14T15:30:00
---

# Dataset Cleaner

A reusable Python pipeline for cleaning and preprocessing tabular and text datasets.

## Features

- Missing value detection and imputation strategies
- Outlier detection using IQR and z-score methods
- Text normalization: lowercasing, punctuation removal, unicode handling
- Duplicate row detection and removal

## Implementation

Built on top of pandas with a modular pipeline architecture. Each cleaning step is a separate function that can be composed.

## Usage

Currently used by the [[Experiment_Tracker]] to preprocess experiment logs and by the [[Web_Scraper]] output pipeline to clean raw scraped data.

## Known Issues

- Slow on datasets larger than 1GB due to in-memory processing
- Unicode handling still has edge cases with CJK characters

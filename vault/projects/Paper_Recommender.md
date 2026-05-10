---
tags: [project, python, machine-learning]
created: 2026-01-08T10:00:00
modified: 2026-01-19T13:00:00
---

# Paper Recommender

Building a system that recommends relevant academic papers based on reading history and interests.

## Approach

Using sentence embeddings to represent paper abstracts as dense vectors. The recommender computes cosine similarity between a query paper and candidates in the database.

## Dataset

Collected 5000 arxiv abstracts using the [[Web_Scraper]]. Cleaned and preprocessed with the [[Dataset_Cleaner]] pipeline.

## Model

Tried fine-tuning a small [[Transformers]] model on the abstract corpus. The fine-tuned embeddings capture domain-specific similarity better than general-purpose sentence transformers.

## Current Status

Prototype working. Recommendations are reasonable but need filtering by date and category.

## Next Steps

- Integrate with [[Experiment_Tracker]] for systematic evaluation
- Add user feedback loop

---
tags: [meeting, lab]
created: 2026-01-26T10:00:00
modified: 2026-01-26T10:30:00
---

# Lab Standup - January 26

Monday standup. Everyone back from the weekend with a clearer sense of the week ahead.

## Team Updates

- **Alice**: [[Data_Pipeline]] orchestration is running end-to-end for the first time. A few edge cases in the cleaner step still failing on papers with non-standard encoding.
- **Bob**: RL baseline is running but results are worse than expected — discussing whether to include or drop from the paper.
- **Me**: Finished [[RAG_System]] prototype. First end-to-end demo working. [[Sentiment_Analyzer]] training running on V100.
- **Sarah**: Reading papers on sparse attention for her own project. Will present one at next reading group.

## Infrastructure

GPU queue is getting congested. We have 4 A100 slots and 3 projects competing for them. Agreed to coordinate via a shared Slack channel before submitting large jobs.

## Demo Planning

Professor Chen wants a lab demo in two weeks. Will need [[Visualization_Tool]] and [[Model_Dashboard]] ready for that. Divided responsibilities: I handle the demo script, Alice handles data freshness, Bob handles the RL visualization.

## Blockers

- Need access to the Semantic Scholar API for [[Knowledge_Graph_Builder]] — Bob is the key holder, will share credentials.
- [[Fine_Tuning_Pipeline]] mixed precision crashes on the older V100 nodes — need to investigate.

## Next Week Focus

Paper writing week. Coding should slow down, writing should accelerate.

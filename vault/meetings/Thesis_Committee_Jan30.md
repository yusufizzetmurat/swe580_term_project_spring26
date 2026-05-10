---
tags: [meeting, advisor, thesis]
created: 2026-01-30T10:00:00
modified: 2026-01-30T11:30:00
---

# Thesis Committee Meeting - January 30

First thesis committee meeting of the spring semester. Committee: Professor Chen (advisor), Professor Williams (NLP), Professor Rodriguez (ML systems).

## Progress Overview

Presented a 20-minute overview of the semester's research direction:

1. Attention mechanism analysis — the main paper contribution
2. [[Paper_Recommender]] as the applied motivation
3. [[Transformers]] experimentation and ablation results so far
4. Infrastructure built: [[Experiment_Tracker]], [[Fine_Tuning_Pipeline]], [[Data_Pipeline]]

## Committee Feedback

**Professor Williams**: Happy with the research direction. Suggested connecting to interpretability literature more explicitly — there's a large body of work on attention as explanation that we should engage with (even if we disagree with some of it).

**Professor Rodriguez**: Interested in the systems work. Suggested that the [[Fine_Tuning_Pipeline]] and [[Benchmark_Suite]] infrastructure could be a separate contribution — "engineering papers are undervalued but important." Worth thinking about for the thesis even if not for this paper.

**Professor Chen**: Largely positive. Emphasized staying focused — the paper needs to make one clear contribution, not four partial ones.

## Timeline Discussion

Discussed the overall PhD timeline. Two more papers needed before dissertation. This semester's paper is on track. Next semester focus should be on the longer-term research question that ties everything together.

## Action Items

- [ ] Add interpretability literature to related work section
- [ ] Send committee a written progress report by February 28
- [ ] Schedule next committee meeting for late April

## Notes on [[Reinforcement_Learning]]

Professor Rodriguez asked whether there's a connection between attention mechanisms and RL — specifically around attention over state representations. Bob's RL work might be more relevant to my thesis than I thought. Worth a conversation.

---
tags: [meeting, advisor]
created: 2026-01-24T14:00:00
modified: 2026-01-24T15:00:00
---

# Advisor Meeting - January 24

Check-in with Professor Chen, focused on ablation study results and related work.

## Agenda

- Review ablation study output from [[Experiment_Tracker]]
- Discuss related work coverage
- Timeline check before February 15 deadline

## Discussion

Showed Professor Chen the ablation results — removing individual attention heads hurts performance unevenly across tasks. Some heads are critical; others seem redundant. She found this interesting and suggested framing it as a finding about attention head specialization, not just an ablation.

She also recommended adding [[BERT]] and [[Transfer_Learning]] baseline comparisons to contextualize our approach. Currently we only compare against vanilla transformer configurations.

## Feedback on Writing

Reviewed the related work draft. Main comment: too much description, not enough positioning. Need to explain not just what each paper does, but why our work is different or builds on it in a specific way.

## Action Items

- [ ] Add BERT fine-tuning baseline to experiment grid
- [ ] Rewrite related work to foreground our contribution
- [ ] Check GPU quota — large ablation grid will need more resources
- [ ] Send draft introduction to Professor Chen by January 31

## Notes

Professor Chen asked about the [[Paper_Recommender]] integration — is it going in the paper or staying as a separate project? Decision: it's motivating context, not a paper contribution. Keep it in the introduction as application context only.

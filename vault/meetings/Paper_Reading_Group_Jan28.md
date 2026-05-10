---
tags: [meeting, reading-group]
created: 2026-01-28T16:00:00
modified: 2026-01-28T17:00:00
---

# Paper Reading Group - January 28

This week: contrastive learning for sentence embeddings. Sarah suggested the topic after the Jan 14 session on efficient attention.

## Papers Discussed

1. **SimCSE: Simple Contrastive Learning of Sentence Embeddings** (Gao et al., 2021)
2. **DeCLUTR: Deep Contrastive Learning for Unsupervised Textual Representations**

## Key Takeaways from SimCSE

The dropout-as-augmentation idea is elegant: pass the same sentence through the encoder twice with different dropout masks, treat the two representations as a positive pair. No complicated augmentations needed.

Hard negatives (contradictory sentence pairs from NLI data) substantially improve performance over random negatives. The model needs to discriminate between sentences that are superficially similar but semantically opposite.

See [[Contrastive_Learning]] for my notes on the broader methodology.

## Connection to Our Work

Sarah pointed out that SimCSE embeddings might outperform our current SciBERT embeddings for the [[Paper_Recommender]]. The contrastive training objective directly optimizes for similarity discrimination — which is exactly what a recommender needs.

Decision: I'll run a quick A/B test comparing our current SciBERT embeddings vs. SimCSE embeddings on a held-out set of paper similarity judgments. Will report at next session.

## Discussion Points

- How do we construct good hard negatives for scientific text? Citation pairs might be positive; non-citing unrelated papers might be negatives. But two non-citing papers can still be closely related in topic.
- The paper uses NLI contradiction pairs as hard negatives — we don't have NLI-style data for scientific text.

## Next Session

Sarah is presenting on Longformer and other long-context attention mechanisms. Back to [[Self_Attention]] variants.

---
tags: [project, nlp, python]
created: 2026-01-23T14:00:00
modified: 2026-02-05T10:30:00
---

# Sentiment Analyzer

A fine-tuned [[BERT]] classifier for detecting sentiment in academic peer review text. The immediate use case is filtering low-quality or extremely negative reviews from the [[Paper_Recommender]] training data.

## Motivation

Peer reviews are noisy. Some papers get recommended because they were heavily discussed (even negatively). Adding a sentiment signal helps distinguish papers that attracted genuine positive attention from those that were controversial or criticized.

## Dataset

Annotated 2,400 review excerpts from PeerRead and ICLR OpenReview as positive, neutral, or negative. Label distribution is roughly 45/35/20 — real reviews skew toward neutral hedging language.

## Model

Fine-tuned SciBERT (not base BERT) on the annotation data. SciBERT's scientific pre-training vocabulary handles domain-specific phrases better. Training details in [[Experiment_Tracker]] run `sentiment_v2`.

3 epochs, batch size 32, LR=2e-5 with linear warmup. Validation F1: 0.81 on the held-out test set.

## Integration

The [[Fine_Tuning_Pipeline]] handles the training loop. Output probabilities feed into the [[Paper_Recommender]] ranking function as a soft signal — papers with high positive sentiment get a small score boost.

## Active Learning Extension

[[Active_Learning_System]] selects the most uncertain review excerpts for human annotation, reducing the total annotation cost. After one round of active learning, we improved F1 by 0.03 with only 200 additional examples.

## Next Steps

- Evaluate on out-of-domain reviews (NeurIPS, ACL)
- Experiment with [[Knowledge_Distillation]] to speed up inference
- Possibly extend to aspect-level sentiment (methodology, clarity, novelty)

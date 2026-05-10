---
tags: [transformer, attention, deep-learning]
created: 2026-01-10T09:30:00
modified: 2026-01-18T14:22:00
---

# Transformers

The Transformer architecture was introduced in the "Attention Is All You Need" paper by Vaswani et al. in 2017. It replaced recurrence with [[Self_Attention]] mechanisms entirely.

## Key Components

- **Multi-Head Attention**: Allows the model to attend to different representation subspaces. See [[Attention_Mechanisms]] for a detailed breakdown.
- **Positional Encoding**: Since there is no recurrence, position information is injected via sinusoidal functions or learned embeddings.
- **Feed-Forward Networks**: Applied independently to each position after attention layers.

## Why It Matters

Transformers are the foundation of modern large language models like GPT and BERT. They scale better than RNNs on long sequences because attention is O(n²) but fully parallelizable, unlike sequential recurrence.

## My Experiments

Tried fine-tuning a small transformer on our [[Paper_Recommender]] dataset. Results were promising — see experiment logs for numbers.

## Open Questions

- How does rotary position encoding compare to learned embeddings?
- Can we reduce the quadratic cost with sparse attention patterns?

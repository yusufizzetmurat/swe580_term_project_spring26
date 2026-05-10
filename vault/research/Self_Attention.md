---
tags: [attention, transformer]
created: 2026-01-14T08:15:00
modified: 2026-01-14T08:15:00
---

# Self-Attention

Self-attention computes relationships between all positions within a single sequence. Unlike cross-attention, the queries, keys, and values are all derived from the same input.

## How It Works

Each token in the input sequence attends to every other token, producing a weighted representation that captures contextual dependencies. This is the core mechanism inside [[Transformers]].

## Computational Cost

The main drawback is quadratic complexity: for a sequence of length n, self-attention requires O(n²) time and memory. This limits the practical context window length.

## Variants

Several approaches aim to reduce this cost:
- Linear attention approximations
- Sparse attention patterns (local windows, strided)
- Flash attention (hardware-aware optimization)

See [[Attention_Mechanisms]] for the broader family of attention approaches.

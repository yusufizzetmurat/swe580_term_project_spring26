---
tags: [attention, deep-learning]
created: 2026-01-12T11:00:00
modified: 2026-01-20T16:45:00
---

# Attention Mechanisms

Attention mechanisms allow neural networks to focus on relevant parts of the input when producing output. Originally introduced for machine translation, they are now fundamental to most deep learning architectures.

## Types of Attention

- **Scaled Dot-Product Attention**: Computes compatibility between query and key vectors using dot products, scaled by the square root of the dimension. Core building block of [[Transformers]].
- **Additive Attention**: Uses a learned feed-forward network to compute alignment scores. Historically important but largely superseded.
- **Cross-Attention**: Attends between two different sequences, such as encoder and decoder in seq2seq models.

## Relation to Self-Attention

[[Self_Attention]] is a special case where queries, keys, and values all come from the same sequence. This enables the model to capture dependencies within a single input.

## Mathematical Formulation

Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

The softmax ensures the weights sum to one, creating a weighted combination of value vectors.

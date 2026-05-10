---
tags: [deep-learning, nlp]
created: 2026-01-24T09:30:00
modified: 2026-01-24T09:30:00
---

# Recurrent Networks

Recurrent Neural Networks (RNNs) process sequences by maintaining a hidden state that is updated at each timestep. Before [[Transformers]], they were the dominant architecture for NLP.

## Vanilla RNN

At each step t, the hidden state h_t = tanh(W_h * h_{t-1} + W_x * x_t + b). The same weights are applied at every timestep — this is what makes it recurrent.

The fundamental problem is the **vanishing gradient**: gradients shrink exponentially as they propagate back through many timesteps. Long-range dependencies are practically unlearnable.

## LSTM

Long Short-Term Memory networks address vanishing gradients with a gating mechanism — input, forget, and output gates control what information flows through a separate cell state. The cell state acts as a "memory highway" with only additive updates, preserving gradients over long distances.

LSTMs were the workhorse of NLP from roughly 2015 to 2018.

## GRU

A simpler variant with reset and update gates, fewer parameters than LSTM. Often performs comparably in practice.

## Why Transformers Replaced Them

- RNNs are inherently sequential — you cannot parallelize across timesteps during training.
- [[Attention_Mechanisms]] in Transformers can directly connect any two positions in O(1) steps regardless of distance.
- [[Self_Attention]] is fully parallelizable across the sequence dimension.

In practice, once hardware-efficient attention implementations arrived, RNNs became mostly obsolete for language modeling.

## Where RNNs Still Appear

Streaming inference where you need online, step-by-step processing. Some time-series tasks. Certain edge deployment scenarios where quadratic attention is too expensive.

## Connection to [[Word_Embeddings]]

Early NLP pipelines used pre-trained word embeddings as inputs to LSTMs. The move to Transformers replaced both: contextualized token representations make static embeddings largely redundant.

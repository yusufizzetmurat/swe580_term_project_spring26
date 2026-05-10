---
tags: [deep-learning, optimization]
created: 2026-02-04T10:30:00
modified: 2026-02-04T10:30:00
---

# Mixture of Experts

Mixture of Experts (MoE) is an architecture where a large number of "expert" sub-networks exist, but only a small subset is activated for each input. This allows scaling model capacity without proportionally scaling compute.

## Core Mechanism

Each transformer feed-forward layer is replaced by N expert networks. A learned routing function selects the top-K experts for each token and routes the token's representation through them. Only K/N of the parameters are used per forward pass.

## Switch Transformer

Google's Switch Transformer (2021) demonstrated that routing to just one expert (K=1) works well and simplifies training. With 1.6 trillion parameters but only activating a fraction per token, it matched much smaller dense models at equal compute.

We read this paper at [[Paper_Reading_Group_Feb04]].

## Routing

The router is a simple linear layer followed by softmax. Tokens are assigned to experts based on highest router probability. The challenge: if the router isn't balanced, some experts become overloaded while others are never used.

**Load balancing loss**: An auxiliary loss penalizes uneven expert utilization. Without it, training collapses to using just a few experts.

## Connection to [[Transformers]]

MoE replaces the FFN sublayer in standard transformer blocks. Attention layers remain dense and shared. This is important: the attention mechanism handles the cross-token reasoning, while experts handle the per-token processing.

## Connection to [[GPT]]

GPT-4 is rumored to use MoE. This would explain the reported 8-expert, 2-active configuration that leaked. MoE is likely central to how frontier labs scale efficiently.

## Trade-offs

- **Pros**: Much larger effective capacity, better performance at equal FLOPs
- **Cons**: More complex training, communication overhead (experts may be on different devices), load balancing is non-trivial

## Connection to [[Optimization_Methods]]

Standard Adam doesn't handle MoE perfectly — experts receive very different gradient magnitudes. Some work suggests per-expert optimizers or modified momentum estimates improve stability.

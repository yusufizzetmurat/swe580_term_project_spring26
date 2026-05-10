---
tags: [deep-learning, graph-ml]
created: 2026-02-02T09:30:00
modified: 2026-02-05T10:00:00
---

# Graph Neural Networks

Graph Neural Networks (GNNs) extend deep learning to graph-structured data. They learn node and edge representations by aggregating information from local neighborhoods — a process called message passing.

## Message Passing Framework

At each layer, each node aggregates messages from its neighbors, combines them with its own representation, and produces an updated embedding. After K layers, a node's representation reflects its K-hop neighborhood.

Formally: h_v^(k) = UPDATE(h_v^(k-1), AGGREGATE({h_u^(k-1) : u ∈ N(v)}))

The choice of AGGREGATE (sum, mean, max, attention) and UPDATE (MLP, GRU) defines the specific GNN variant.

## Graph Attention Networks (GAT)

Apply [[Attention_Mechanisms]] during aggregation — instead of treating all neighbors equally, learn attention coefficients that weight neighbor contributions. This is the natural bridge between GNNs and the transformer world.

Interestingly, the full [[Transformers]] self-attention mechanism is equivalent to a GNN on a complete graph (every node attends to every other node).

## Applications Relevant to Our Work

- **Citation graphs**: Papers as nodes, citations as edges. GNNs can learn paper representations that incorporate citation context — potentially useful for [[Knowledge_Graph_Builder]].
- **Semantic similarity**: Modeling relationships between concepts in a knowledge base.

## Expressive Power

GNNs are limited by the Weisfeiler-Leman graph isomorphism test — standard message passing cannot distinguish certain graph structures. Higher-order GNNs or positional encodings are needed for full expressiveness.

## Connection to [[Transformers]]

There's a growing view that transformers are a special case of GNNs. Both use attention to aggregate information. The main difference is that GNNs operate on sparse graphs (local neighborhoods) while transformers use dense attention (all pairs). Sparse attention variants of transformers (Longformer, BigBird) are essentially making transformers more GNN-like.

## Open Questions

- Can we use GNNs to improve the [[Paper_Recommender]] by incorporating citation structure?
- How do we handle dynamic graphs where nodes and edges change over time?

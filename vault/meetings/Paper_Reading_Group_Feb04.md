---
tags: [meeting, reading-group]
created: 2026-02-04T16:00:00
modified: 2026-02-04T17:00:00
---

# Paper Reading Group - February 4

Two papers on Mixture of Experts scaling. Suggested by Bob after seeing the Switch Transformer results mentioned in a paper we cited.

## Papers Discussed

1. **Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** (Fedus et al., 2022)
2. **GLaM: Efficient Scaling of Language Models with Mixture-of-Experts** (Du et al., 2022)

## Key Takeaways

Switch Transformer's main insight: routing to just one expert (top-1) is stable and often matches or beats top-2 routing with half the communication cost. The load balancing loss is critical — without it, training collapses to a few experts.

GLaM uses top-2 MoE and trains on much more data. The paper's claim: for a given inference compute budget, MoE architectures outperform dense models. Dense models are compute-efficient during training but have worse quality-per-FLOP at inference.

See [[Mixture_of_Experts]] for my notes on the technical details.

## Discussion

Bob raised the connection to [[Optimization_Methods]] — the Adam optimizer behaves differently when only a fraction of parameters receive gradients each step. Some experts may have stale momentum estimates if they're rarely selected. This is a real issue that the GLaM paper mentions briefly.

Sarah connected this to [[Self_Attention]] efficiency: MoE makes the FFN sublayer sparse, but attention is still dense. True efficiency gains need both sparse attention AND sparse FFN.

## Relevance

Not directly relevant to the paper deadline in two weeks. But very relevant for thinking about what a next project might look like — applying MoE principles to the attention mechanism itself.

## Next Session (February 10)

Alice is presenting DistilBERT and TinyBERT. Relevant to [[Knowledge_Distillation]] and our ongoing discussion about deploying lighter models.

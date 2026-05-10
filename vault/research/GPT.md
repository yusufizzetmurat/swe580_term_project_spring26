---
tags: [nlp, deep-learning, transformer]
created: 2026-01-25T11:00:00
modified: 2026-02-01T09:45:00
---

# GPT

GPT (Generative Pre-trained Transformer) is a family of autoregressive language models. Unlike [[BERT]], GPT uses only the decoder side of the [[Transformers]] architecture — each token can only attend to previous tokens (causal attention).

## Architecture

Stacked decoder blocks with masked [[Self_Attention]]. The causal mask ensures no information leakage from future tokens. This makes GPT naturally suited for text generation.

Pre-training objective: predict the next token given all previous tokens. Simple but remarkably powerful at scale.

## Scaling Laws

One of the most important insights from the GPT line of work: model performance improves predictably with compute, data, and parameters. Scaling is more reliable than architectural innovation for raw language modeling.

## In-Context Learning

GPT-3 demonstrated that large models can perform tasks from a few examples in the prompt alone, without gradient updates. This was surprising — the model has to somehow "learn" the task from context during inference.

See [[Prompt_Engineering]] for practical techniques that build on this capability.

## Comparison with BERT

| | GPT | BERT |
|---|---|---|
| Direction | Left-to-right only | Bidirectional |
| Primary use | Generation | Understanding/classification |
| Pre-training | Next token prediction | Masked LM + NSP |
| Fine-tuning | Optional (few-shot works) | Usually required |

## Relevance to Our Work

The [[Chatbot_Prototype]] generation component is essentially a lightweight GPT-style model. We use the retrieval results from the [[Paper_Recommender]] as context and prompt a GPT model to synthesize a response.

The [[RAG_System]] project formalizes this retrieve-then-generate pipeline.

## Open Questions

- At what scale does in-context learning become reliable enough to replace fine-tuning?
- How do [[Mixture_of_Experts]] architectures change the scaling picture?

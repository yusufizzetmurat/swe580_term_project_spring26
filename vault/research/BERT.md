---
tags: [nlp, deep-learning, transformer]
created: 2026-01-23T10:00:00
modified: 2026-01-29T15:30:00
---

# BERT

BERT (Bidirectional Encoder Representations from Transformers) was introduced by Devlin et al. at Google in 2018. It changed NLP by showing that a single pre-trained model could be fine-tuned to outperform task-specific architectures across almost every benchmark.

## Architecture

BERT is a stack of [[Transformers]] encoder layers — it uses only the encoder side, unlike seq2seq models. The bidirectional attention (via [[Self_Attention]]) means each token attends to all other tokens simultaneously, both left and right. This is what GPT cannot do — GPT is causal (left-to-right only).

## Pre-training Tasks

- **Masked Language Modeling (MLM)**: 15% of tokens are randomly masked. The model learns to predict them using both left and right context. This forces genuine bidirectional understanding.
- **Next Sentence Prediction (NSP)**: Given two sentences, predict if the second follows the first. Controversial — later work (RoBERTa) showed NSP may not help.

## Tokenization

Uses WordPiece tokenization. Unknown words are split into subword units, so vocabulary coverage is near-complete. See [[Tokenization]] for details on subword methods and their trade-offs.

## Why It Matters for Our Work

We use BERT embeddings in the [[Paper_Recommender]] to represent paper abstracts. Domain-adapted BERT (SciBERT, specifically) gives much better similarity estimates for scientific text than general-purpose sentence transformers.

The [[Sentiment_Analyzer]] project also fine-tunes BERT for classifying review sentiment — useful for filtering low-quality papers from the recommender pipeline.

## Fine-Tuning

Add a task-specific head on top of the [CLS] token representation and fine-tune end-to-end. Works well even with small labeled datasets (a few thousand examples). See [[Transfer_Learning]] for the conceptual framing.

## Open Questions

- How much does the pre-training data domain matter? SciBERT helps, but is there a better starting point for our specific domain?
- BERT is slow at inference. Is [[Knowledge_Distillation]] the right path for deployment?

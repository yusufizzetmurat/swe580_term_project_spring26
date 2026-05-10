---
tags: []
created: 2026-01-09T16:00:00
modified: 2026-01-16T10:30:00
---

# Word Embeddings

Word embeddings map discrete words to dense vector representations where semantically similar words are close in vector space.

## Classic Methods

- **Word2Vec**: Uses skip-gram or CBOW architectures to learn embeddings from local context windows. Efficient to train on large corpora.
- **GloVe**: Combines global co-occurrence statistics with local context. Produces embeddings that capture both syntactic and semantic relationships.

## Properties

Embeddings capture analogies: king - man + woman ≈ queen. They also encode relationships like country-capital, verb tenses, and comparative forms.

## Connection to Modern NLP

While static embeddings assign one vector per word, [[Transformers]] produce contextual embeddings where the same word gets different representations depending on surrounding context. This was a major leap forward.

See also [[Attention_Mechanisms]] for how modern models weight different parts of the input dynamically.

## Evaluation

Intrinsic evaluation uses analogy tasks and similarity benchmarks. Extrinsic evaluation measures downstream task performance like classification or named entity recognition.

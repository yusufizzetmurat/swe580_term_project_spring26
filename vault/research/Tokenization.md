---
tags: [nlp, deep-learning]
created: 2026-01-28T10:30:00
modified: 2026-01-28T10:30:00
---

# Tokenization

Tokenization converts raw text into discrete units (tokens) that a model can process. The choice of tokenization scheme has significant downstream effects on model behavior, vocabulary coverage, and efficiency.

## Character, Word, and Subword

- **Character-level**: Smallest units, no unknown tokens, but sequences are very long and characters carry little meaning individually.
- **Word-level**: Natural units, short sequences, but vocabulary explodes and rare/unseen words become unknowns.
- **Subword**: The current standard. Splits rare words into smaller units while keeping common words intact. Best of both worlds.

## Subword Methods

**Byte Pair Encoding (BPE)**: Start with characters, iteratively merge the most frequent adjacent pair. Used by GPT-2, GPT-3, and many others. Greedy, deterministic, fast.

**WordPiece**: Similar to BPE but merges maximize language model likelihood rather than raw frequency. Used by [[BERT]]. Produces a slightly different vocabulary that tends to keep morphemes together.

**SentencePiece**: Language-agnostic tokenization that works directly on raw text (no whitespace pre-tokenization). Good for multilingual models. Used by T5 and multilingual BERT variants.

**Unigram LM**: Probabilistic approach — start with a large vocabulary and prune tokens that don't improve model likelihood. Produces tokenizations with uncertainty.

## Vocabulary Size Trade-offs

Larger vocabulary → shorter sequences, but more parameters in the embedding layer and output head. Typical sizes: 30k–50k for monolingual, 100k–250k for multilingual.

## Connection to [[Word_Embeddings]]

Static word embeddings require fixed vocabularies. Subword tokenization sidesteps this entirely — the model learns representations for subword units rather than whole words.

## Tokenization Artifacts

Tokenization boundaries affect model behavior in subtle ways. "GPU" might be split as "G", "##PU" in BERT's WordPiece scheme. Leading spaces matter in BPE (the token "dog" and " dog" are different). These quirks need to be understood when working with model outputs.

## Practical Note

When fine-tuning a pre-trained model, always use its original tokenizer. Changing the tokenizer invalidates the pre-trained embeddings.

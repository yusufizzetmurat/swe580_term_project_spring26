---
tags: [deep-learning, self-supervised]
created: 2026-01-30T11:00:00
modified: 2026-02-02T14:15:00
---

# Contrastive Learning

Contrastive learning trains a model to map similar inputs close together in embedding space and dissimilar inputs far apart — without requiring labels. It has become the dominant paradigm for self-supervised representation learning.

## Core Idea

Given an anchor example, create a positive pair (augmented version of the same example) and negative pairs (other examples). The model learns to minimize distance to positives and maximize distance to negatives.

## SimCLR

A landmark framework for vision. Two augmented views of the same image form a positive pair. All other images in the batch are negatives. The NT-Xent loss pushes positives together in the normalized embedding space.

Key insight: large batch sizes are critical — more negatives means the model has to be more discriminative.

## In NLP: SimCSE

Applies contrastive learning to sentence embeddings. Positive pairs are created by passing the same sentence through the encoder twice with different dropout masks — the stochasticity creates different representations of the same meaning.

Negative pairs can be "hard negatives" — sentences that are grammatically similar but semantically opposite (e.g. entailment vs contradiction pairs from NLI datasets).

We discussed this at [[Paper_Reading_Group_Jan28]]. The technique is relevant to our [[Paper_Recommender]] — better sentence embeddings mean better similarity estimates between paper abstracts.

## Connection to [[Word_Embeddings]]

Word2Vec's skip-gram objective is a form of contrastive learning — predicting context words (positives) vs. random noise words (negatives). Contrastive learning generalizes and formalizes this idea.

## Connection to [[Transfer_Learning]]

Contrastive pre-training produces general representations that transfer well to downstream tasks — often rivaling supervised pre-training while requiring no labels. It's an increasingly attractive alternative when labeled data is scarce.

## Why It Works

The model learns to encode semantic content rather than surface features. Augmentations that preserve meaning (synonym replacement, dropout, back-translation) guide the model toward meaning-preserving representations.

## Open Questions

- How do we choose good augmentations for scientific text?
- Can we construct better hard negatives from our paper database?

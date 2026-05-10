---
tags: [deep-learning, machine-learning]
created: 2026-01-27T14:00:00
modified: 2026-02-03T11:20:00
---

# Transfer Learning

Transfer learning reuses knowledge gained from one task or domain to improve performance on another. In deep learning, this typically means pre-training a model on a large dataset and then fine-tuning on a smaller, task-specific one.

## Why It Works

Deep networks learn hierarchical representations. Early layers capture general features (edges, syntax, basic patterns); later layers capture task-specific features. Pre-trained early layers transfer well across tasks — only the later layers need adaptation.

## Two Paradigms

**Feature extraction**: Freeze the pre-trained model entirely. Use its outputs as fixed features for a downstream classifier. Fast and cheap, but limited — the representation cannot adapt to the target domain.

**Fine-tuning**: Continue training the pre-trained model on the target task. All or most weights update. Typically better performance, especially when the target domain differs from the pre-training domain.

## In NLP

The pre-train then fine-tune approach became standard after [[BERT]]. A model pre-trained on massive text corpora can be fine-tuned on a few thousand labeled examples and reach state-of-the-art on many tasks. This democratized NLP — you no longer need enormous labeled datasets for each new task.

See [[Fine_Tuning_Pipeline]] for our implementation.

## In Computer Vision

[[CNN_Architecture]] models pre-trained on ImageNet transfer well to medical imaging, satellite imagery, and other domains with limited data. The lower convolutional layers are nearly always frozen.

## Domain Adaptation

When the source and target domains differ significantly, full fine-tuning may be needed — or intermediate domain-adaptive pre-training (e.g. continued pre-training on domain text before task fine-tuning). We do this with SciBERT for the [[Paper_Recommender]].

## Negative Transfer

Not all transfer is positive. If source and target tasks are too different, pre-trained features can hurt. Monitor validation performance carefully during fine-tuning, especially in the early epochs.

## Connection to [[Contrastive_Learning]]

Self-supervised contrastive methods are a form of transfer learning — learning general representations without labels, then transferring to labeled tasks. Growing alternative to supervised pre-training.

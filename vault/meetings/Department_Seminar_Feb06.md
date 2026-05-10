---
tags: [meeting, workshop]
created: 2026-02-06T14:00:00
modified: 2026-02-06T16:00:00
---

# Department Seminar - February 6

Monthly department seminar. Two back-to-back talks on efficient machine learning. Well-attended — about 40 people including faculty and students from multiple groups.

## Talk 1: Model Compression for On-Device Inference

Speaker: Professor Liu (visiting from Carnegie Mellon)

Focus on deploying large models on edge devices with strict memory and latency constraints. Covered [[Knowledge_Distillation]], pruning, and quantization as complementary compression strategies.

Key point: distillation, pruning, and quantization are often applied in sequence — distill first to get a smaller model, then prune sparse weights, then quantize to INT8. Stacking all three can achieve 10-20x compression with <5% accuracy loss on many NLP tasks.

The DistilBERT example was directly relevant to our work — we're evaluating exactly this for the [[Chatbot_Prototype]] deployment path.

## Talk 2: Privacy-Preserving Machine Learning

Speaker: Dr. Kim (our department, security lab)

Covered [[Federated_Learning]] and differential privacy. Emphasized the tension between privacy guarantees and model utility — adding enough noise for differential privacy often degrades accuracy substantially for small datasets.

Dr. Kim mentioned that federated learning works much better when participants have similar data distributions. This aligns with the challenges Dr. Park's group would face with multilingual review data — Korean and English reviews have very different length distributions and vocabulary.

## Q&A Highlights

Professor Rodriguez asked about quantization compatibility with custom attention implementations — the answer is nuanced (quantization-aware training helps but requires architectural support).

Someone from the systems group asked about [[Optimization_Methods]] for quantized training — turns out Adam works poorly with INT8 weights. Straight-through estimators are needed for backpropagation through discrete quantization.

## Personal Notes

Both talks directly relevant to deployment plans for our lab's projects. Need to read Professor Liu's distillation survey paper that he mentioned.

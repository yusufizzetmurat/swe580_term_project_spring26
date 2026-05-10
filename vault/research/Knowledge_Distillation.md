---
tags: [deep-learning, optimization, machine-learning]
created: 2026-02-05T09:00:00
modified: 2026-02-09T16:30:00
---

# Knowledge Distillation

Knowledge distillation trains a smaller "student" model to mimic a larger "teacher" model. The goal is to compress a high-capacity model into one that is faster and smaller without losing too much accuracy.

## Core Idea

Instead of training the student on hard labels (one-hot), train it on the teacher's soft probability distributions over classes. These soft targets carry more information — a "6" that looks slightly like "0" and "8" encodes similarity information that a hard label discards.

Temperature T controls the softness:

softmax(z_i / T)

Higher temperature → softer, more informative distributions. Typical T values: 2–5 for standard distillation.

## DistilBERT

Distilled version of [[BERT]] — 40% fewer parameters, 60% faster, retaining 97% of BERT's performance on GLUE. The student is initialized from every other layer of the teacher, then trained with a combination of:
- Soft cross-entropy on teacher logits
- MLM loss on raw text  
- Cosine similarity between teacher and student hidden states (intermediate layer matching)

We read this paper at [[Paper_Reading_Group_Feb10]].

## Relevance to Our Work

[[BERT]] inference is too slow for real-time use in the [[Chatbot_Prototype]]. We're evaluating DistilBERT and TinyBERT as drop-in replacements. Preliminary results suggest DistilBERT retains 95% of our classification accuracy with 2x speedup.

This was discussed with Professor Chen at [[Advisor_Meeting_Feb07]] — she's supportive of including efficiency results in the paper.

## Task-Specific vs. General Distillation

- **General distillation**: Distill the pre-trained model (e.g. BERT → DistilBERT). Student is then fine-tuned normally.
- **Task-specific distillation**: Distill the fine-tuned teacher directly on the target task. Better task performance but less generalizable.

We're exploring task-specific distillation for the [[Sentiment_Analyzer]] where we have sufficient labeled data.

## Connection to [[Transfer_Learning]]

Distillation is another form of knowledge transfer — from teacher to student rather than from pre-training to fine-tuning. The two can be combined: distill a fine-tuned teacher onto a small student.

## Limitations

Student capacity is a hard ceiling — you cannot distill a 340M parameter BERT into a 5M parameter model without significant loss. There is a minimum viable size for a given task.

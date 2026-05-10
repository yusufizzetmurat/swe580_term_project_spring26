---
tags: [meeting, reading-group]
created: 2026-02-10T16:00:00
modified: 2026-02-10T17:00:00
---

# Paper Reading Group - February 10

Alice presenting. Topic: model compression via [[Knowledge_Distillation]], specifically DistilBERT and TinyBERT.

## Papers Discussed

1. **DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter** (Sanh et al., 2019)
2. **TinyBERT: Distilling BERT for Natural Language Understanding** (Jiao et al., 2020)

## DistilBERT

Alice gave an excellent presentation. Key design choices:

- Student initialized from every other layer of the teacher (layers 0, 2, 4, 6, 8, 10)
- Three training objectives: soft cross-entropy on teacher logits, masked language modeling on raw text, cosine distance between teacher and student hidden states
- 40% parameter reduction, 60% speed increase, 97% of BERT performance on GLUE

The hidden state matching loss is what makes DistilBERT work — without it, the student struggles to match the teacher's internal representations even if final outputs look similar.

## TinyBERT

More aggressive compression approach. Matches teacher at every transformer layer (attention matrices, hidden states) not just the final output. Also does task-specific distillation after general distillation — two-stage process.

Result: 7.5x smaller, 9.4x faster than BERT, 96.8% performance on GLUE.

## Discussion

I mentioned that we're evaluating DistilBERT for the [[Chatbot_Prototype]] — good timing, as this gives me sharper intuition about what makes the distillation work. The hidden state matching is probably the key; our preliminary results match the paper's claims.

Bob asked about distillation for [[Reinforcement_Learning]] policies — this is called policy distillation and it's used in multi-task RL. Different challenges because the teacher policy is non-stationary during training.

## Connection to [[Optimization_Methods]]

Alice raised a subtle point: DistilBERT uses the same AdamW optimizer as BERT fine-tuning. The temperature parameter in the soft cross-entropy loss needs to be treated like a hyperparameter — the paper found T=8 works well but this isn't universal.

## See Also

[[Knowledge_Distillation]] for full notes on the general technique.

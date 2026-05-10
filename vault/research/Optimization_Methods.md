---
tags: [deep-learning, optimization, math]
created: 2026-01-29T09:00:00
modified: 2026-02-04T16:00:00
---

# Optimization Methods

Training neural networks is a high-dimensional non-convex optimization problem. The choice of optimizer, learning rate, and schedule can make or break a training run.

## Stochastic Gradient Descent (SGD)

The baseline. Update parameters in the direction of the negative gradient computed on a mini-batch. Simple, well-understood, and still competitive when tuned well — particularly for computer vision tasks.

Momentum helps by accumulating a velocity vector in directions of persistent gradient, dampening oscillations. Nesterov momentum looks ahead before computing the gradient.

## Adam

The default for most NLP and transformer training. Combines momentum (first moment) with adaptive learning rates per parameter (second moment). Much less sensitive to learning rate choice than SGD.

Adam parameters:
- β₁ = 0.9 (momentum decay)
- β₂ = 0.999 (second moment decay)
- ε = 1e-8 (numerical stability)

**AdamW**: Adam with decoupled weight decay. Weight decay in Adam is not equivalent to L2 regularization — AdamW fixes this. Now standard for [[Transformers]] and [[BERT]] fine-tuning.

## Learning Rate Scheduling

A constant learning rate rarely works best. Common schedules:

- **Warmup**: Gradually increase LR from near-zero for the first N steps. Critical for transformer training — without warmup, early large gradient updates can destabilize the model.
- **Cosine decay**: LR follows a cosine curve after warmup. Smooth, effective.
- **Linear decay**: Simpler, often sufficient.

## Gradient Clipping

Clip gradient norm to a threshold (e.g. 1.0) before applying updates. Prevents explosive gradients, especially important in RNNs and early transformer training. We use this in the [[Fine_Tuning_Pipeline]].

## Practical Notes from Our Experiments

From running [[Experiment_Tracker]] logs:
- Warmup of 6% of training steps works well for BERT fine-tuning
- AdamW with LR=2e-5 and linear decay is a safe default for most NLP tasks
- Batch size interacts strongly with LR — larger batches need proportionally higher LR (linear scaling rule)
- Gradient accumulation is useful when GPU memory limits batch size

## Connection to [[Reinforcement_Learning]]

RL algorithms use gradient-based optimization too, but the objective is non-stationary (the policy changes the data distribution). This makes RL optimization fundamentally harder than supervised learning.

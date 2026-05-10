---
tags: [project, machine-learning, python]
created: 2026-02-05T10:00:00
modified: 2026-02-09T09:00:00
---

# Active Learning System

Selects the most informative examples from unlabeled data for human annotation. Reduces labeling cost by prioritizing uncertain or diverse examples over random sampling.

## Motivation

We have large unlabeled paper collections but limited annotation budget. For [[Sentiment_Analyzer]], annotating everything would cost ~400 hours. Active learning reduces this by 30-50% while maintaining the same final model quality.

## Query Strategies

**Uncertainty sampling**: Select examples where the current model is least confident. For classification, this means examples where the predicted class probability is closest to 1/K (K classes). Simple and effective.

**Margin sampling**: Select examples with the smallest margin between the top-two class probabilities. More discriminative than uncertainty sampling.

**Entropy sampling**: Use prediction entropy as the uncertainty measure. Equivalent to uncertainty sampling for binary classification, but generalizes better to multi-class.

**Core-set**: Selects a geometrically diverse subset of the unlabeled pool, maximizing coverage of the feature space. Useful when the initial labeled set is small and biased.

We use entropy sampling by default — it consistently outperforms random selection by 20-30% in our experiments.

## Integration

Reads model checkpoint from [[Fine_Tuning_Pipeline]], runs inference on the unlabeled pool, ranks examples by entropy, and pushes the top N to the [[Annotation_Tool]] queue.

After annotation, the pipeline automatically retrains the model with the new labels and reruns selection. This loop continues until the annotation budget is exhausted or a performance threshold is reached.

## Results

On [[Sentiment_Analyzer]]: 30% fewer annotations needed to reach F1=0.80 compared to random sampling. On [[Multilingual_Classifier]]: 40% reduction, likely because the multilingual label space has larger regions of uncertainty.

## Tracked in

[[Experiment_Tracker]] runs `al_sentiment_v1` through `al_sentiment_v3`.

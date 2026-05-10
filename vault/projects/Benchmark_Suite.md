---
tags: [project, python, benchmark]
created: 2026-02-01T09:00:00
modified: 2026-02-07T10:00:00
---

# Benchmark Suite

Standardized benchmarking scripts for NLP classification and retrieval tasks. Built to make evaluation consistent across projects — before this, each project had its own evaluation code with slightly different metric implementations.

## Problem It Solves

Found three different implementations of F1 score across [[Sentiment_Analyzer]], [[Paper_Recommender]], and [[Chatbot_Prototype]]. They gave slightly different numbers for the same predictions. This is embarrassing in a research context and makes comparison across experiments meaningless.

## What It Provides

**Classification metrics**: accuracy, precision, recall, F1 (macro/micro/weighted), confusion matrix, ROC-AUC.

**Retrieval metrics**: precision@K, recall@K, NDCG@K, mean reciprocal rank (MRR). Essential for evaluating [[Paper_Recommender]] and [[RAG_System]].

**Significance testing**: paired bootstrap resampling for comparing two systems. Reports p-values and confidence intervals — Professor Chen insisted on this after seeing results without statistical testing at [[Advisor_Meeting_Jan17]].

**Report generation**: automatically produces a markdown report with all metrics, a confusion matrix figure (via [[Matplotlib_Guide]]), and a comparison table if multiple systems are evaluated.

## Integration

Wraps the HuggingFace `evaluate` library for standard metrics. Custom implementations for retrieval metrics and significance testing.

All projects now import from `benchmark_suite` instead of implementing their own metrics. Results are automatically logged to [[Experiment_Tracker]].

## Usage

```python
from benchmark_suite import ClassificationEvaluator, RetrievalEvaluator

eval = ClassificationEvaluator(labels, predictions)
report = eval.full_report()
```

## Next Steps

- Add ROUGE and BERTScore for [[Text_Summarizer]] evaluation
- Generate LaTeX tables directly (for paper figures)
- Integrate with [[Evaluation_Framework]] for higher-level comparisons

---
tags: [project, python, benchmark]
created: 2026-02-03T13:00:00
modified: 2026-02-09T11:00:00
---

# Evaluation Framework

A higher-level evaluation harness that wraps [[Benchmark_Suite]] and adds experiment management, cross-system comparison, and paper-ready reporting. Where Benchmark_Suite handles single-model evaluation, Evaluation Framework handles multi-system comparisons with statistical rigor.

## Why a Separate Layer

[[Benchmark_Suite]] answers "how good is this model?" Evaluation Framework answers "is system A significantly better than system B, and by how much?"

For the paper, we need both: absolute numbers for each configuration, and significance-tested comparisons across configurations.

## Core Features

**System registry**: Register multiple systems (e.g. Config A vs Config B, BERT vs DistilBERT) and run them all on the same test set.

**Paired evaluation**: Automatically runs paired bootstrap significance tests across all registered system pairs using [[Benchmark_Suite]]'s testing module.

**Ablation support**: Define an ablation by specifying which components to remove. The framework systematically runs all ablation conditions and reports delta performance.

**Report generation**: Produces a LaTeX table directly from results — format matches ACL/EMNLP style. Saves hours of manual table formatting.

## Usage in Our Paper

This is what generates Table 1 and Table 2 in the paper draft. Professor Chen saw the output at [[Advisor_Meeting_Feb07]] and was satisfied with the format.

The [[Chatbot_Prototype]] evaluation section runs through this framework — comparing retrieval-only, generation-only, and full RAG conditions.

## Integration

Reads model predictions from [[Experiment_Tracker]] runs. Writes final reports to a `reports/` directory. Visualizations delegated to [[Model_Dashboard]] and [[Visualization_Tool]].

## Limitations

Currently only supports offline evaluation (pre-computed predictions). Online evaluation (calling model APIs at test time) is not yet supported — relevant for [[Prompt_Optimizer]] experiments.

## Next Steps

- Add support for human evaluation result integration (from [[Annotation_Tool]])
- Generate comparison plots automatically (currently done manually in [[Matplotlib_Guide]])

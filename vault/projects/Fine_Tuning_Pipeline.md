---
tags: [project, python, machine-learning]
created: 2026-01-27T09:00:00
modified: 2026-02-06T16:00:00
---

# Fine-Tuning Pipeline

A reusable fine-tuning framework for transformer models. Born out of frustration with rewriting the same training loop for every new project — [[Sentiment_Analyzer]], [[Multilingual_Classifier]], and the [[Paper_Recommender]] embedding model all now use it.

## Design Goals

- Config-driven: all hyperparameters in a YAML file, no hardcoded values
- Reproducible: automatically logs configs and seeds to [[Experiment_Tracker]]
- Memory-efficient: gradient accumulation, mixed precision training (fp16/bf16)
- Flexible: works with any HuggingFace model and tokenizer

## Pipeline Stages

1. **Data loading**: reads from CSV or JSON, applies [[Dataset_Cleaner]] preprocessing
2. **Tokenization**: uses the model's native tokenizer, handles truncation and padding
3. **Training loop**: AdamW with warmup + linear decay (see [[Optimization_Methods]])
4. **Evaluation**: runs on validation set every N steps, early stopping on F1 or loss
5. **Checkpointing**: saves best model and last model; compatible with HuggingFace Hub

## Gradient Accumulation

When GPU memory limits effective batch size, accumulate gradients over N micro-batches before updating. The pipeline handles this transparently — set `batch_size: 64` and `accumulation_steps: 4` to effectively train with batch size 256.

## Mixed Precision

BF16 training is enabled by default on A100 GPUs. On older hardware, FP16 with loss scaling is used. Roughly 40% memory reduction with negligible accuracy loss for most tasks.

## Usage

```bash
python train.py --config configs/sentiment.yaml
```

The config file specifies model name, dataset path, learning rate, epochs, and evaluation metrics. Output: trained model + full experiment log in [[Experiment_Tracker]].

## Current Limitations

- No support for distributed multi-GPU training yet — relies on single-GPU training with gradient accumulation as a workaround
- Parameter-efficient fine-tuning (LoRA, prefix tuning) not yet implemented

## Next Steps

- Add LoRA support to enable fine-tuning much larger models with limited GPU memory
- Integrate [[Knowledge_Distillation]] as a post-training step

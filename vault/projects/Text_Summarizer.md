---
tags: [project, nlp, python]
created: 2026-01-29T11:00:00
modified: 2026-02-05T14:00:00
---

# Text Summarizer

Abstractive summarization model for academic paper abstracts. The use case: many papers have long, dense abstracts. Generating a 2-3 sentence summary helps users quickly triage recommendations from the [[Paper_Recommender]] without reading the full abstract.

## Models Tested

**T5-small**: Fast, decent quality. Fine-tuned on scientific abstract pairs (original + human-written structured abstract). Good enough for a first pass.

**BART-base**: Better quality, slower. The encoder-decoder architecture is well-suited for summarization. [[Transformers]] at both encoder and decoder. Results tracked in [[Experiment_Tracker]] under `summarizer_v1` and `summarizer_v2`.

**GPT-style prompting**: Zero-shot summarization with [[GPT]]-class models via the [[RAG_System]] generation component. Surprisingly competitive — no fine-tuning needed, but inconsistent formatting.

## Evaluation

Used ROUGE-1, ROUGE-2, and ROUGE-L against human-written reference summaries. BART-base scores:
- ROUGE-1: 0.42
- ROUGE-2: 0.19
- ROUGE-L: 0.39

These numbers look low but are typical for abstractive summarization — ROUGE heavily penalizes paraphrasing.

Human evaluation (n=30 judges) rates BART-base summaries as "helpful" 76% of the time.

## Integration

Summaries are generated at indexing time and stored alongside the paper metadata. The [[RAG_System]] can optionally include the generated summary in retrieved passages.

## Challenges

- Some papers have highly structured abstracts (Motivation/Methods/Results/Conclusions). The model struggles when fine-tuned on mixed formats.
- Very long papers (>20 pages) whose abstracts are insufficient summaries — needs full-text access.

## Next Steps

- Try hierarchical summarization: summarize each section, then summarize the summaries
- Evaluate [[Knowledge_Distillation]] to compress BART-base for faster inference

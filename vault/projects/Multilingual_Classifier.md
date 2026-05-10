---
tags: [project, nlp, python]
created: 2026-02-06T11:00:00
modified: 2026-02-09T14:00:00
---

# Multilingual Classifier

Extends the [[Sentiment_Analyzer]] to handle non-English academic text. Dr. Park's lab works with Korean and Chinese NLP papers — our English-only classifier was useless for their review data.

## Background

The collaboration with Dr. Park (see [[Collaboration_Meeting_Jan27]]) surfaced a real need: their evaluation dataset includes reviews in Korean, Chinese, and English. A multilingual classifier would make the joint workshop paper significantly stronger.

## Model

Using mBERT (multilingual BERT) and XLM-RoBERTa as base models. XLM-RoBERTa is generally superior — trained on more data across more languages with a better tokenizer.

See [[Tokenization]] for notes on how multilingual [[BERT]] handles subword units across different scripts (crucial for CJK languages where tokenization is fundamentally different from English).

## Dataset

Combined:
- Our existing English review annotations (2,400 examples from [[Sentiment_Analyzer]])
- Dr. Park's Korean review annotations (800 examples, provided after data sharing agreement)
- Automatically translated Chinese reviews with human spot-checking (600 examples)

Total: 3,800 training examples across 3 languages. Evaluation done on held-out sets for each language separately.

## Results (preliminary)

| Language | F1 |
|---|---|
| English | 0.79 |
| Korean | 0.71 |
| Chinese | 0.68 |

English performance is slightly lower than the English-only [[Sentiment_Analyzer]] (0.81 vs 0.79) — some capacity used for multilingual generalization.

## Training

Used [[Fine_Tuning_Pipeline]] with a multilingual-specific config. [[Active_Learning_System]] helped prioritize the most uncertain Korean examples for human review — important given our limited Korean annotation budget.

## Next Steps

- Collect more Korean and Chinese training data
- Evaluate zero-shot transfer to Japanese (not in training data)
- Cross-lingual consistency: same paper in different languages should get the same sentiment score

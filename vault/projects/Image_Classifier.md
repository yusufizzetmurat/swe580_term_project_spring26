---
tags: [project, computer-vision, python]
created: 2026-01-28T13:00:00
modified: 2026-02-02T09:00:00
---

# Image Classifier

A ResNet-based classifier for categorizing figures extracted from academic papers. The goal is to enrich the [[Paper_Recommender]] index with visual content signals — a paper with many architecture diagrams is probably more relevant to someone studying model design than one with only bar charts.

## Problem

Papers contain different types of figures: architecture diagrams, training curves, qualitative results (images), tables, and equations-as-images. Currently the [[Paper_Recommender]] only indexes text. Visual content is ignored entirely.

## Approach

Extract all figures from PDFs using pdfminer. Classify each figure into one of five categories:
- Architecture diagram
- Training/evaluation plot
- Qualitative results (generated images, visualizations)
- Table
- Other

## Model

Fine-tuned ResNet-50 on a manually labeled set of 1,800 figures. See [[CNN_Architecture]] for the underlying architecture.

Training details in [[Experiment_Tracker]] run `imgcls_v1`. Validation accuracy: 83% — hardest cases are the boundary between architecture diagrams and "other" figures.

## Dataset Construction

Used [[Dataset_Cleaner]] to remove corrupt or duplicate images after PDF extraction. About 8% of extracted figures were unusable (rendering artifacts, extremely small images).

## Integration Plan

Once stable, will pass figure type distribution as additional features to the [[Paper_Recommender]] ranking model. Papers with architecture diagrams get a slight boost for method-focused queries; papers with training plots get a boost for empirical queries.

## Limitations

- PDF figure extraction is imperfect — captions and figures sometimes merge
- 83% accuracy is not good enough for hard decisions — using it as a soft signal only
- No handling of multi-panel figures yet

## Next Steps

- Collect more labeled examples, particularly for architecture diagrams
- Try a vision transformer backbone (ViT) as an alternative to ResNet

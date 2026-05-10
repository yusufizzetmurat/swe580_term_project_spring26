---
tags: [project, python, visualization]
created: 2026-02-07T10:00:00
modified: 2026-02-09T17:00:00
---

# Visualization Tool

Interactive visualizations for attention weights, embedding spaces, and model behavior. Built primarily for generating paper figures and for demos — the static [[Matplotlib_Guide]] recipes aren't interactive enough for live demos.

## Components

**Attention Heatmap Viewer**: Given a sentence and a BERT-style model, renders the attention weight matrix for any layer and head. Useful for qualitative analysis — which tokens does the model attend to when processing "attention"?

Built with Plotly for interactivity. Can export to static PNG for paper figures.

**Embedding Space Explorer**: Projects high-dimensional embeddings (from SciBERT, sentence transformers) into 2D using UMAP. Color-codes by category (paper topic, sentiment, etc.). Interactive zoom and hover shows paper title on mouseover.

Used to visualize the [[Paper_Recommender]] embedding space — you can clearly see topic clusters forming. This figure will go in the paper.

**Training Curve Dashboard**: Pulls run data from [[Experiment_Tracker]] via its API and renders live training curves with smoothing. Nicer than TensorBoard for our specific use case because it combines multiple runs in one view.

## Integration with [[Model_Dashboard]]

The Model Dashboard handles operational monitoring (live inference stats, latency, error rates). Visualization Tool handles research analysis (embedding spaces, attention patterns, training dynamics). They share the [[Experiment_Tracker]] as a data source.

## Paper Figures Generated So Far

- Figure 2: Attention heatmap on a sample paper abstract
- Figure 3: UMAP embedding space with topic clusters
- Figure 4: Training curves for ablation study conditions

Professor Chen approved all three at [[Advisor_Meeting_Feb07]].

## Technical Stack

Plotly Dash for interactive components, Matplotlib for static export, UMAP-learn for dimensionality reduction, HuggingFace transformers for model inference.

## Next Steps

- Add citation graph visualization using NetworkX + Pyvis
- Export figures at publication-quality DPI with proper font embedding

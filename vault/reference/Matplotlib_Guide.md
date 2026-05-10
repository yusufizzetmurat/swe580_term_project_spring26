---
tags: [reference, python, visualization]
created: 2026-01-26T10:00:00
modified: 2026-02-08T15:00:00
---

# Matplotlib Guide

Reference for producing publication-quality figures. Matplotlib's default settings are fine for exploration but need significant customization for papers and presentations.

## Figure and Axes

```python
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
fig, axes = plt.subplots(1, 3, figsize=(14, 4))   # 1 row, 3 columns
```

Always use the object-oriented interface (`ax.plot()` not `plt.plot()`). The functional interface is confusing for subplots and doesn't compose well.

## Publication-Quality Settings

```python
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})
```

Setting these globally at the top of a plotting script saves a lot of per-figure fiddling.

## Saving for Papers

```python
fig.savefig("figure.pdf", bbox_inches="tight")    # PDF for LaTeX (vector)
fig.savefig("figure.png", dpi=300, bbox_inches="tight")  # PNG fallback
```

Always use PDF for LaTeX. Vector graphics scale perfectly and stay crisp at any zoom level. The [[LaTeX_Formatting]] notes cover how to include them correctly.

## Attention Heatmaps

We generate these for the [[Visualization_Tool]]:

```python
im = ax.imshow(attention_matrix, cmap="Blues", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(len(tokens)))
ax.set_xticklabels(tokens, rotation=45, ha="right", fontsize=8)
ax.set_yticks(range(len(tokens)))
ax.set_yticklabels(tokens, fontsize=8)
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
```

## Training Curves

```python
ax.plot(steps, train_loss, label="Train", color="#1f77b4")
ax.plot(steps, val_loss, label="Val", color="#ff7f0e", linestyle="--")
ax.fill_between(steps, lower, upper, alpha=0.2)  # confidence band
ax.set_xlabel("Training Steps")
ax.set_ylabel("Loss")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)  # cleaner look
```

Removing top and right spines makes the plot cleaner — a convention I picked up from reading well-designed ML papers.

## Color Palettes

Use colorblind-friendly palettes. The Tableau 10 palette (Matplotlib default since 3.x) is reasonably accessible. For sequential data, use viridis or Blues. Never use jet.

## See Also

[[Pandas_Tips]] for preparing data before plotting, [[Numpy_Guide]] for array manipulation.

---
tags: [reference, writing]
created: 2026-01-06T14:00:00
modified: 2026-01-14T09:00:00
---

# LaTeX Formatting

Reference for writing academic papers in LaTeX.

## Document Structure

Use `\documentclass{article}` for papers. Common packages: amsmath, graphicx, hyperref, natbib.

## Equations

Inline: `$E = mc^2$`. Display: `\begin{equation}`. Multi-line: `\begin{align}`.

## Figures and Tables

Always use `\begin{figure}[htbp]` for float placement. Tables with `booktabs` package look much cleaner.

## Bibliography

BibTeX with natbib for author-year citations. Keep a master .bib file and use JabRef or Zotero for management.

## Overleaf Tips

- Use track changes for co-author review
- Compile with pdflatex for speed, lualatex for complex fonts
- Rich text mode is useful for non-LaTeX co-authors

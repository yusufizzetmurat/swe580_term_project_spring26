---
tags: [project, python]
created: 2026-01-05T11:00:00
modified: 2026-01-12T16:00:00
---

# Web Scraper

A Python tool for scraping academic paper metadata from arxiv and other sources.

## Implementation

Built with BeautifulSoup and the requests library. Uses rate limiting to respect server policies.

## Data Collected

- Paper titles, authors, abstracts, and categories
- Publication dates and citation counts where available
- Currently holds about 5000 papers focused on NLP and machine learning

## Pipeline

Raw HTML is parsed, cleaned by the [[Dataset_Cleaner]], and stored as structured JSON files for downstream use.

## Issues

- Some arxiv pages have inconsistent HTML structure
- Need to add support for Semantic Scholar API as a backup source

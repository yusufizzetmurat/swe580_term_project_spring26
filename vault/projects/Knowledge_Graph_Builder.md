---
tags: [project, python, graph-ml]
created: 2026-01-30T10:00:00
modified: 2026-02-06T15:00:00
---

# Knowledge Graph Builder

Constructs a citation graph from our arxiv paper collection. Nodes are papers; directed edges represent citations. The graph enables structural retrieval — finding papers not just by content similarity but by their position in the citation network.

## Motivation

Two papers can discuss very similar ideas without sharing vocabulary — making content search miss them. But they'll appear in each other's citation neighborhood. The citation graph captures this structural relatedness.

See [[Graph_Neural_Networks]] for the modeling techniques we plan to apply on top of this graph.

## Data Sources

- ArXiv metadata API: paper IDs, titles, abstracts, authors, dates
- Semantic Scholar API: citation relationships between papers
- [[Web_Scraper]]: supplementary data collection where APIs are incomplete

Raw data cleaned with [[Dataset_Cleaner]] — deduplication, handling retracted papers, normalizing author names.

## Graph Statistics (current snapshot)

- 18,400 paper nodes
- 142,000 citation edges
- Average in-degree: 7.7
- Highly skewed — top 1% of papers receive 40% of citations

## Graph Construction Pipeline

1. Collect paper metadata from APIs
2. Resolve citation links (many citations reference paper titles, not IDs — fuzzy matching required)
3. Build adjacency list and store as compressed sparse matrix
4. Generate node embeddings using SciBERT for cold-start papers with no citation history

## Integration with [[Paper_Recommender]]

Current plan: hybrid scoring that combines:
- Content similarity (SciBERT cosine similarity)
- Citation proximity (graph distance or GNN-based embedding similarity)
- Recency signal (newer papers scored higher)

## Next Steps

- Train a Graph Attention Network on the citation graph (see [[Graph_Neural_Networks]])
- Evaluate hybrid recommendations against pure content-based baseline
- Connect to [[RAG_System]] for structured retrieval queries ("find papers that cite X and are related to Y")

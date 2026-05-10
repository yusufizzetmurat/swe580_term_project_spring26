---
tags: [project, python, data]
created: 2026-02-02T10:30:00
modified: 2026-02-08T09:00:00
---

# Data Pipeline

End-to-end orchestration of data collection, cleaning, annotation, and delivery to downstream models. Ties together [[Web_Scraper]], [[Dataset_Cleaner]], [[Annotation_Tool]], and the [[Paper_Recommender]] indexing step into a single reproducible workflow.

## Motivation

Early in the project, these steps were run manually in sequence. This caused reproducibility issues — nobody could remember exactly which version of the scraper was used, whether the cleaner had been re-run after fixing a bug, or which annotation batch was included. A pipeline solves this.

## Orchestration

Using Apache Airflow for scheduling and dependency management. Each stage is a DAG node:

```
Scrape (daily) → Clean → Annotate (manual step, human in loop) → Index → Notify
```

The annotation step is semi-automated: [[Active_Learning_System]] selects examples, [[Annotation_Tool]] collects labels, the pipeline resumes after a minimum number of annotations are complete.

## Stage Details

**Scrape**: [[Web_Scraper]] fetches new arxiv papers matching our category filters. Runs nightly. New papers land in a staging area.

**Clean**: [[Dataset_Cleaner]] runs deduplication, language detection, and quality filters. Rejects papers with parsing errors or below a minimum content length.

**Annotate**: Optional stage for papers that the [[Sentiment_Analyzer]] is uncertain about. Uncertainty threshold is configurable.

**Index**: Embeds cleaned abstracts with SciBERT and adds to the FAISS index. Also updates the [[Knowledge_Graph_Builder]] citation graph.

**Notify**: Sends a summary email with pipeline stats — papers added, rejected, annotated, and any failures.

## Monitoring

Pipeline run logs stored in [[Experiment_Tracker]]. The [[Model_Dashboard]] has a dedicated "Data Health" tab showing ingestion rate, rejection rate, and index freshness.

## Failure Handling

Each stage retries up to 3 times on transient errors. Failures alert via email. Human intervention required for repeated failures — typically API rate limits or schema changes on the source website.

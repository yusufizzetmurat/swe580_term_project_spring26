---
tags: [meeting, workshop]
created: 2026-01-29T15:00:00
modified: 2026-01-29T16:30:00
---

# Industry Talk - January 29

Guest lecture by Dr. Aisha Sharma from Google DeepMind. Title: "Building Production NLP Systems: What Academia Doesn't Teach You."

## Overview

Excellent talk. Very different perspective from the papers we read — focused on the gap between benchmark performance and production reliability.

## Key Points

**Reliability over accuracy**: A system that is 85% accurate and fails gracefully is more valuable in production than one that is 90% accurate and fails silently. Error handling, confidence calibration, and fallback behavior matter enormously.

**Prompting in production**: Dr. Sharma's team manages hundreds of [[Prompt_Engineering]] templates with version control, A/B testing, and automatic regression detection. Individual prompt sensitivity is a major operational challenge — a model update can silently break a prompt that worked before.

**RAG is not retrieval + generation**: She was emphatic that the [[RAG_System]] architecture requires careful attention to retrieval quality, not just generation quality. Bad retrieval produces confident wrong answers. Their internal metric: "hallucination rate on grounded queries" — how often does the model say something not in the retrieved context?

**Evaluation gap**: The most important metric in production is user satisfaction, which is poorly correlated with automated metrics. They run continuous human evaluation at small scale throughout deployment.

## Connections to Our Work

The retrieval quality point is directly relevant — our [[Evaluation_Framework]] should include a "faithfulness" metric that checks whether the generated answer is supported by retrieved passages.

The prompt sensitivity point motivates [[Prompt_Optimizer]] — automating prompt evaluation is better than relying on manual inspection.

## Follow-Up

Dr. Sharma offered to give feedback on a draft of our paper. Professor Chen will reach out to her directly.

## Resources

Mentioned a Google technical report on LLM evaluation frameworks — need to find the reference.

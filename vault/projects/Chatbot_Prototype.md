---
tags: [project, nlp]
created: 2026-01-13T14:00:00
modified: 2026-01-21T10:30:00
---

# Chatbot Prototype

A conversational AI prototype for answering questions about our research lab's publications.

## Architecture

- **Intent Recognition**: Classifies user queries into categories (paper lookup, author search, topic exploration).
- **Response Generation**: Uses a retrieval-augmented approach — finds relevant paper chunks then generates a response.

## Technology

The retrieval component uses [[Transformers]] embeddings. The generation step is powered by a pre-trained language model with [[Attention_Mechanisms]] at its core.

## Evaluation

Testing with 50 sample questions from lab members. Current accuracy is around 72% for factual questions.

## Demo

Presented at the collaboration meeting. Feedback was positive but users want better handling of follow-up questions.

---
tags: [project, nlp, python]
created: 2026-01-26T10:00:00
modified: 2026-02-07T14:00:00
---

# RAG System

Retrieval-Augmented Generation (RAG) system for answering questions about our lab's research. It retrieves relevant paper chunks from a vector database, then conditions a language model to generate a grounded answer.

## Architecture

```
User query
    → Query encoder (SciBERT)
    → Vector similarity search (FAISS index)
    → Top-K retrieved passages
    → Prompt construction (context + question)
    → LLM generation ([[GPT]]-style model)
    → Grounded answer
```

## Why RAG over Pure LLM

A language model alone will hallucinate paper titles, authors, and results. By anchoring the generation to retrieved text, we constrain the output to factually supported content. This is the core architecture behind the [[Chatbot_Prototype]].

## Retrieval Component

The FAISS index stores SciBERT embeddings of 500-token paper chunks with 50-token overlap. Chunking with overlap ensures that relevant sentences near chunk boundaries are captured.

Retrieved K=5 passages by default, passed to the generator as numbered context items.

## Generation Component

Using a fine-tuned model with a [[Prompt_Engineering]] template that instructs it to answer from the provided context only. The "grounding instruction" reduces hallucination significantly — early versions without it would confidently invent results.

## Evaluation

Evaluated on 120 annotated question-answer pairs from lab members. Metrics: answer accuracy (human-judged), faithfulness (does the answer follow from retrieved passages), and coverage (did retrieval find the relevant chunk).

Results tracked in [[Experiment_Tracker]], visualized in [[Model_Dashboard]].

## Current Limitations

- Retrieval fails on very specific numerical questions ("What was the F1 score in Table 2?") — the relevant chunk often isn't the abstract but a table in the paper body
- Multi-hop questions requiring reasoning across multiple papers are hard

## Next Steps

- Connect [[Knowledge_Graph_Builder]] output for structured retrieval
- Evaluate with [[Evaluation_Framework]] for systematic comparison

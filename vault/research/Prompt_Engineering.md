---
tags: [nlp, llm]
created: 2026-02-03T14:00:00
modified: 2026-02-08T11:30:00
---

# Prompt Engineering

Prompt engineering is the practice of designing input text to elicit desired behavior from large language models. As models have grown more capable, prompting has become a skill as important as fine-tuning.

## Zero-Shot and Few-Shot

**Zero-shot**: Describe the task in the prompt and expect the model to follow. Works well for capable models on natural instructions.

**Few-shot**: Provide examples of input-output pairs in the prompt before the actual query. The model infers the pattern and applies it. [[GPT]]-3 demonstrated this surprisingly well.

## Chain-of-Thought

Ask the model to reason step-by-step before giving a final answer. "Let's think step by step" — this simple phrase dramatically improves performance on reasoning tasks. The model externalizes its intermediate computation in the text, which helps it stay on track.

## Prompt Templates

Consistent templates reduce variance. For our [[Chatbot_Prototype]], we use:

```
You are a helpful assistant for a research lab.
Context: {retrieved_passages}
Question: {user_question}
Answer concisely based only on the context above.
```

The instruction to use only the provided context is important — it reduces hallucination and keeps responses grounded.

## System Prompts

Many chat models support a system prompt that sets the model's role and constraints. This is more reliable than putting instructions in the user turn. We use this extensively in the [[RAG_System]].

## Prompt Sensitivity

A frustrating reality: small wording changes can significantly affect output. "List the key points" vs "Summarize the key points" can produce qualitatively different responses. This is one motivation for the [[Prompt_Optimizer]] project.

## Limitations

Prompt engineering is fragile. It works differently across model families and versions. Fine-tuning is more reliable when you have labeled data, but prompting is faster to iterate on. We use prompting for exploration and fine-tuning for production.

## Connection to [[Industry_Talk_Jan29]]

The DeepMind speaker emphasized that production systems almost always combine prompting with other signals — retrieval, tool use, structured outputs. Pure prompting rarely suffices.

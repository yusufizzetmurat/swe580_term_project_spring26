---
tags: [meeting, collaboration]
created: 2026-01-27T11:00:00
modified: 2026-01-27T12:00:00
---

# Collaboration Meeting - January 27

Second meeting with Dr. Park's NLP group. More concrete this time — moved from exploration to planning.

## Participants

Our side: me, Professor Chen (first 20 minutes). Dr. Park's side: Dr. Park and two PhD students (Jiwon and Marcus).

## Data Sharing

Dr. Park's team shared 800 labeled Korean review excerpts via a secure university file transfer. These are now integrated into the [[Multilingual_Classifier]] training set.

Jiwon raised a concern about sharing raw review text — reviewers have an expectation of anonymity. We agreed to strip all identifying metadata before use. Alice will handle the anonymization step in [[Dataset_Cleaner]].

## Joint Chatbot Evaluation

Agreed on a concrete plan: Dr. Park's team will test the [[Chatbot_Prototype]] on 50 of their standard evaluation questions (originally designed for their dialogue system). This gives us an external, independent evaluation.

Their evaluation questions cover a wider range of query types than our internal test set, which will stress-test the [[RAG_System]] retrieval.

## Multilingual Extension

Marcus is interested in the [[Multilingual_Classifier]] work. He's worked with XLM-RoBERTa before and offered to review our fine-tuning approach. Scheduled a separate technical sync next week.

## Timeline

- By February 3: Share [[Chatbot_Prototype]] API access with Dr. Park's team
- By February 10: Collect their evaluation results
- By February 12: Merge into paper if results are positive

## Potential Issues

If their chatbot questions are significantly out-of-distribution from our training data, the results might look bad. Need to characterize the question distribution before presenting externally.

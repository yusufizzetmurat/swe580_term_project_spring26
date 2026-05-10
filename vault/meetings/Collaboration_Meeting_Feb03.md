---
tags: [meeting, collaboration]
created: 2026-02-03T14:00:00
modified: 2026-02-03T15:00:00
---

# Collaboration Meeting - February 3

Third meeting with Dr. Park's group. First time seeing their evaluation numbers on our system.

## Chatbot Evaluation Results

Dr. Park's team ran the [[Chatbot_Prototype]] on 50 of their standard dialogue evaluation questions. Results:

- Answer accuracy (human-judged): 68%
- Faithfulness (answer grounded in retrieved text): 84%
- Coverage (retrieval found relevant passage): 79%

68% accuracy is lower than our internal 72% — expected, since their questions are out-of-distribution. The faithfulness score (84%) is encouraging — when retrieval works, the generation is mostly grounded.

## Discussion

The 21% retrieval failure rate is the main bottleneck. Marcus analyzed the failure cases: most are questions about very recent papers (post-2024) not yet in our index, and questions requiring cross-paper reasoning.

The [[RAG_System]] retrieval uses a fixed index snapshot — Dr. Park's evaluation queries include papers published this month. Need to increase update frequency in the [[Data_Pipeline]].

## [[Multilingual_Classifier]] Sync

Separate 30-minute discussion with Jiwon about the multilingual extension. She reviewed the [[Fine_Tuning_Pipeline]] configuration and suggested adding a language identification step before classification — the classifier currently assumes language is known.

## Next Steps

- Increase [[Data_Pipeline]] index update frequency from weekly to daily
- Add recent paper coverage to [[Evaluation_Framework]] metrics
- Jiwon will send XLM-RoBERTa fine-tuning tips for Korean text

## Timeline Concern

February 10 is the deadline for incorporating their results into the paper. That's tight — Dr. Park's team will send a final evaluation report by February 8.

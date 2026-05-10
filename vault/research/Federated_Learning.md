---
tags: [machine-learning, privacy]
created: 2026-02-06T11:00:00
modified: 2026-02-06T11:00:00
---

# Federated Learning

Federated learning trains machine learning models across multiple decentralized devices or institutions without exchanging the raw data. Each participant trains locally; only model updates (gradients or weights) are shared with a central server.

## Motivation

Privacy regulations (GDPR, HIPAA) restrict sharing sensitive data across institutional boundaries. In our context: Dr. Park's lab has valuable dialogue evaluation data, but sharing it directly raises data governance issues. This came up at [[Collaboration_Meeting_Jan27]] as a potential concern.

## FedAvg Algorithm

The standard approach:
1. Server sends global model to participants
2. Each participant trains for E local epochs on their data
3. Participants send updated weights to server
4. Server averages the weights (weighted by dataset size)
5. Repeat

Surprisingly effective — despite the simplicity, FedAvg converges to good models on many tasks.

## Challenges

**Statistical heterogeneity**: Participants' data distributions differ. The lab with mostly ML papers and the lab with mostly NLP papers will produce conflicting gradient directions. This "non-IID" problem is a core research challenge.

**Communication efficiency**: Sending full model gradients every round is expensive. Gradient compression, quantization, and partial model updates reduce communication cost.

**Byzantine robustness**: If some participants are malicious or faulty, their updates can corrupt the global model. Robust aggregation methods (e.g., coordinate-wise median) provide some protection.

## Differential Privacy

Often combined with federated learning for stronger guarantees — add calibrated noise to local updates so the server cannot infer individual training examples. This comes at a privacy-utility trade-off.

## Connection to [[Optimization_Methods]]

FedAvg is essentially distributed SGD with infrequent synchronization. The local update steps before aggregation cause "client drift" — local models diverge from the global optimum. Methods like FedProx add a proximal term to constrain local updates.

## Connection to [[Reinforcement_Learning]]

Federated RL is an emerging area — training RL agents across multiple environments without sharing environment data. More complex due to the non-stationarity of RL.

## Practical Relevance

Worth keeping in mind if the collaboration with Dr. Park's group expands. For now, we agreed on a simpler data transfer protocol, but federated learning is the principled long-term solution.

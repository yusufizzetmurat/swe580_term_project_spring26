---
tags: [reinforcement-learning, machine-learning]
created: 2026-01-11T14:00:00
modified: 2026-01-19T09:15:00
---

# Reinforcement Learning

Reinforcement learning trains agents to make sequential decisions by maximizing cumulative reward signals from an environment.

## Core Concepts

- **Markov Decision Process**: The formal framework — states, actions, transitions, and rewards.
- **Policy**: A mapping from states to actions. Can be deterministic or stochastic.
- **Value Function**: Estimates the expected cumulative reward from a given state.

## Key Algorithms

- **Q-Learning**: Off-policy algorithm that learns action-value functions. Deep Q-Networks (DQN) scale this with neural networks.
- **Policy Gradient**: Directly optimizes the policy using gradient ascent on expected reward. REINFORCE is the simplest example.
- **Actor-Critic**: Combines policy gradient with a value function baseline to reduce variance.

## Exploration vs Exploitation

A fundamental tradeoff: the agent must explore new actions to discover better strategies while exploiting known good actions to maximize reward.

## Applications

Game playing (Atari, Go), robotics, and recommendation systems. Sometimes paired with [[CNN_Architecture]] for visual input processing.

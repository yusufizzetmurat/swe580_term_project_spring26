---
tags: [deep-learning, generative-ai]
created: 2026-01-31T15:00:00
modified: 2026-01-31T15:00:00
---

# Diffusion Models

Diffusion models are a class of generative models that learn to reverse a gradual noising process. They have become the dominant approach for image synthesis and are expanding into audio, video, and structured data.

## Forward Process

Starting from a clean sample x₀, iteratively add small amounts of Gaussian noise over T steps. At step T, the sample is pure noise. The forward process is fixed and requires no learning.

## Reverse Process

A neural network (typically a U-Net for images) learns to predict the noise added at each step, effectively denoising the sample. At inference, start from pure noise and repeatedly apply the denoising network to recover a clean sample.

## Why They Work Better Than GANs

[[GAN_Architecture]] training is notoriously unstable — the generator and discriminator can enter failure modes like mode collapse. Diffusion models are trained with a stable MSE objective (predict the added noise) and tend to produce more diverse samples.

The trade-off: inference is slow — hundreds to thousands of forward passes through the denoising network, versus a single forward pass for a GAN.

## Connections to [[Attention_Mechanisms]]

Modern diffusion models incorporate transformer-based architectures (DiT — Diffusion Transformers). Cross-attention is used to condition generation on text prompts — this is what makes Stable Diffusion and DALL-E 3 work.

## Text-to-Image

The conditioning mechanism: a text encoder (usually a CLIP or T5 model) encodes the prompt into a sequence of embeddings. The denoising U-Net uses cross-attention to attend to these embeddings at each step.

## Relevance to Our Work

Mostly tangential for now — our focus is language understanding, not generation. But diffusion for discrete text is an active research area worth watching. Bob mentioned this at lab meeting as a potential future direction.

## Key Papers

- DDPM (Ho et al., 2020): foundational formulation
- Score matching (Song et al.): alternative theoretical framing
- Latent diffusion (Rombach et al.): operate in a compressed latent space for efficiency

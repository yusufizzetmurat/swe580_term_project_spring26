---
tags: [deep-learning, generative-ai, computer-vision]
created: 2026-02-01T10:00:00
modified: 2026-02-01T10:00:00
---

# GAN Architecture

Generative Adversarial Networks (GANs) frame image generation as a two-player game. A generator tries to produce realistic-looking samples; a discriminator tries to distinguish generated samples from real ones.

## Training Objective

The generator G and discriminator D play a minimax game:

min_G max_D E[log D(x)] + E[log(1 - D(G(z)))]

In practice this is often non-saturating: maximize log D(G(z)) for the generator, which provides stronger gradients early in training.

## Architecture

Early GANs used fully connected layers. DCGANs introduced convolutional architectures that work much better for images — the generator uses transposed convolutions to upsample from a latent vector z; the discriminator uses strided convolutions to downsample.

See [[CNN_Architecture]] for the convolutional building blocks.

## Training Challenges

GAN training is notoriously difficult:

- **Mode collapse**: The generator finds a small number of outputs that fool the discriminator and stops producing diversity.
- **Non-convergence**: The minimax objective has no guaranteed Nash equilibrium in the function approximation regime.
- **Evaluation**: There is no clean loss metric — FID (Fréchet Inception Distance) is standard but imperfect.

## Wasserstein GAN

WGAN replaces the JS divergence with the Wasserstein distance, which provides a more stable gradient signal. Requires gradient penalty or weight clipping on the discriminator (now called "critic"). Much more stable training in practice.

## Where GANs Still Win

Despite [[Diffusion_Models]] largely overtaking GANs for image quality, GANs remain faster at inference (single forward pass). StyleGAN3 still produces state-of-the-art face synthesis.

## Connection to [[Optimization_Methods]]

GAN optimization is a min-max problem, not a standard minimization. Standard Adam works but requires careful balancing of generator and discriminator update frequencies and learning rates.

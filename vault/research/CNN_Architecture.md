---
tags: [deep-learning, computer-vision]
created: 2026-01-08T10:00:00
modified: 2026-01-15T11:30:00
---

# CNN Architecture

Convolutional Neural Networks are the backbone of modern computer vision. They learn hierarchical features through stacked layers of convolutions.

## Core Layers

- **Convolutional Layers**: Apply learned filters across the input to detect local patterns like edges, textures, and shapes.
- **Pooling Layers**: Downsample feature maps to reduce spatial dimensions and provide translation invariance.
- **Fully Connected Layers**: Map extracted features to output classes.

## Training

CNNs are trained using backpropagation and gradient descent. The loss gradients flow backward through the network, updating filter weights at each layer. Batch normalization and dropout help with regularization.

## Relation to Other Architectures

While CNNs dominate vision tasks, [[Reinforcement_Learning]] agents sometimes use CNN encoders to process visual observations from environments.

## Key Architectures

AlexNet, VGG, ResNet, and EfficientNet represent major milestones. ResNet introduced skip connections that enabled training of very deep networks.

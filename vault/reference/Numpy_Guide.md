---
tags: [reference, python, math]
created: 2026-01-25T09:00:00
modified: 2026-01-25T09:00:00
---

# NumPy Guide

Core reference for numerical computing with NumPy. Mostly matrix operations and broadcasting patterns I use frequently in ML work.

## Array Creation

```python
np.zeros((3, 4))           # 3x4 array of zeros
np.ones((3, 4))
np.eye(4)                  # 4x4 identity matrix
np.random.randn(3, 4)      # standard normal
np.arange(0, 10, 0.5)      # like range() but returns array
np.linspace(0, 1, 100)     # 100 evenly spaced values from 0 to 1
```

## Indexing and Slicing

```python
a[1, :]          # second row, all columns
a[:, 1]          # all rows, second column
a[1:3, 2:4]      # submatrix
a[[0, 2], :]     # rows 0 and 2 (fancy indexing — returns copy, not view)
```

Slicing returns a view. Fancy indexing returns a copy. This matters for memory: modifying a slice modifies the original; modifying a fancy-indexed result does not.

## Broadcasting

Rules: dimensions are aligned from the right. Size 1 dimensions are stretched to match. 

```python
a = np.ones((3, 4))
b = np.ones((4,))       # broadcast to (3, 4)
c = np.ones((3, 1))     # broadcast to (3, 4)
```

Broadcasting eliminates most explicit loops. The attention score computation QK^T / sqrt(d_k) is a pure broadcasting + matrix multiplication operation — no loops needed.

## Matrix Operations

```python
np.dot(A, B)     # matrix multiplication (also A @ B)
A.T              # transpose
np.linalg.norm(v)           # L2 norm
np.linalg.norm(v, axis=1)   # per-row L2 norms
np.linalg.svd(M)            # singular value decomposition
```

For batched matrix multiplication (e.g. multiple attention heads), use `np.einsum`:

```python
# Batch matrix multiply: (batch, heads, seq, dim) x (batch, heads, dim, seq)
scores = np.einsum('bhid,bhjd->bhij', Q, K)
```

## Useful Functions

```python
np.argmax(a, axis=1)        # index of max per row
np.argsort(a, axis=1)       # indices that would sort each row
np.clip(a, 0, 1)            # clamp values to [0, 1]
np.concatenate([a, b], axis=0)
np.stack([a, b], axis=0)    # creates a new axis
```

## Softmax (manually)

```python
def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)  # numerical stability
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)
```

Subtracting the max before exponentiation prevents overflow. This is what every deep learning framework does internally.

## Connection to [[Statistics_Basics]]

NumPy provides most of the statistical primitives: `np.mean`, `np.std`, `np.var`, `np.corrcoef`, `np.histogram`. For hypothesis testing, use `scipy.stats`.

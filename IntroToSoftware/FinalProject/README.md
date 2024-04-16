# Pong From Pixels - Final Project

## Problem Statement

How can we get from raw pixel data (RGB values) of a game of pong to an AI agent that can play the game?
![alt text](image.png)

## Methodology

```python
self.model = {
    'W1': np.random.randn(self.hidden_size, self.input_dim) / np.sqrt(self.input_dim),
    'W2': np.random.randn(self.hidden_size) / np.sqrt(self.hidden_size),
}
```

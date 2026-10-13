"""Estimate an event probability by simulation and compare with theory."""
import numpy as np

rng = np.random.default_rng(42)
trials = 100_000
# Roll two fair six-sided dice. The event is that their sum is seven.
rolls = rng.integers(1, 7, size=(trials, 2))
estimated_probability = np.mean(rolls.sum(axis=1) == 7)
theoretical_probability = 6 / 36

print(f"Estimated probability: {estimated_probability:.4f}")
print(f"Theoretical probability: {theoretical_probability:.4f}")
# Try increasing trials: the estimate usually gets closer to the theoretical value.

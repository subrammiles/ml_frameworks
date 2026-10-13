"""Interview: find the indices of the three largest values efficiently."""
import numpy as np

values = np.array([12, 5, 31, 18, 24, 9, 31])
k = 3

# argpartition selects the top-k region without fully sorting every value.
top_indices = np.argpartition(values, -k)[-k:]
top_indices = top_indices[np.argsort(values[top_indices])[::-1]]

print("Top values:", values[top_indices])
print("Their original indices:", top_indices)
# Ties can appear in either order. Follow-up: compare this with argsort for small arrays.

"""Select, slice, and update values in a NumPy array."""
import numpy as np

scores = np.array([72, 88, 91, 65, 78])

print("First score:", scores[0])
print("Middle scores:", scores[1:4])

# A slice is a view, so updating it also updates the original array.
scores[0:2] += 5
print("After adding 5 to the first two:", scores)

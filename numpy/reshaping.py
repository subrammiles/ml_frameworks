"""Reshape and combine arrays while keeping the same number of values."""
import numpy as np

measurements = np.arange(1, 13)
matrix = measurements.reshape(3, 4)

print("3 rows by 4 columns:\n", matrix)
print("Transpose:\n", matrix.T)
print("First two columns:\n", matrix[:, :2])

left, right = np.split(measurements, 2)
print("Two halves:", left, right)

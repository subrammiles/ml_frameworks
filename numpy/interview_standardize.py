"""Interview: standardize each column (z-score) without Python loops."""
import numpy as np

data = np.array([[10.0, 100.0], [12.0, 130.0], [14.0, 160.0]])

# axis=0 computes a separate mean and standard deviation for each column.
column_means = data.mean(axis=0)
column_stds = data.std(axis=0)
standardized = (data - column_means) / column_stds

print("Column means:", column_means)
print("Standardized values:\n", standardized)
# Interview follow-up: what if a column has zero standard deviation?

"""Compute summaries by axis and handle missing numeric values."""
import numpy as np

# Rows are students; columns are assignments. NaN represents a missing score.
scores = np.array([[80, 90, 85], [70, np.nan, 75], [95, 88, 92]])

print("Average per assignment:", np.nanmean(scores, axis=0))
print("Average per student:", np.nanmean(scores, axis=1))
print("Assignment maxima:", np.nanmax(scores, axis=0))

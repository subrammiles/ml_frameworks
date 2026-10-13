"""Calculate and interpret a correlation matrix."""
import numpy as np

hours_studied = np.array([1, 2, 2, 3, 4, 5, 6], dtype=float)
practice_tests = np.array([1, 1, 2, 2, 3, 4, 5], dtype=float)
exam_scores = np.array([52, 57, 61, 64, 72, 80, 86], dtype=float)

features = np.column_stack([hours_studied, practice_tests, exam_scores])
correlations = np.corrcoef(features, rowvar=False)
print("Rows and columns: study hours, practice tests, exam score")
print(np.round(correlations, 2))

# Correlation measures linear association. It does not establish causation and
# can miss nonlinear relationships or be distorted by outliers.

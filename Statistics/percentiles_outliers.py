"""Find quartiles and flag possible outliers with the 1.5*IQR rule."""
import numpy as np

wait_minutes = np.array([4, 5, 6, 7, 7, 8, 9, 10, 11, 35], dtype=float)
q1, median, q3 = np.percentile(wait_minutes, [25, 50, 75])
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers = wait_minutes[(wait_minutes < lower_fence) | (wait_minutes > upper_fence)]

print(f"Q1={q1:.1f}, median={median:.1f}, Q3={q3:.1f}")
print(f"IQR={iqr:.1f}; fences=({lower_fence:.1f}, {upper_fence:.1f})")
print("Possible outliers:", outliers)
# A statistical flag is a prompt to investigate, not proof of bad data.

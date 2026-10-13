"""Inspect, select, and sort a DataFrame."""
import pandas as pd

students = pd.DataFrame(
    {
        "name": ["Asha", "Ben", "Chen", "Diya"],
        "class": ["A", "B", "A", "B"],
        "marks": [82, 67, 91, 76],
    }
)

print("Shape:", students.shape)
print("Columns:", students.columns.tolist())
print("Students scoring at least 80:\n", students.loc[students["marks"] >= 80])
print("Sorted by marks:\n", students.sort_values("marks", ascending=False))

"""Find and handle missing and duplicate records."""
import pandas as pd

students = pd.DataFrame(
    {
        "name": ["Asha", "Ben", "Chen", "Chen"],
        "marks": [82, None, 91, 91],
        "city": ["Delhi", "Pune", None, None],
    }
)

print("Missing values per column:\n", students.isna().sum())

# Keep one copy of duplicate records, then fill missing values explicitly.
students = students.drop_duplicates()
students["marks"] = students["marks"].fillna(students["marks"].mean())
students["city"] = students["city"].fillna("Unknown")
print("Cleaned data:\n", students)

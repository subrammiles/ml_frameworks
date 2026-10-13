"""Summarize records by category and reshape a summary."""
import pandas as pd

sales = pd.DataFrame(
    {
        "store": ["North", "South", "North", "South", "North"],
        "item": ["Tea", "Tea", "Coffee", "Coffee", "Tea"],
        "units": [12, 9, 7, 11, 5],
        "revenue": [36, 27, 35, 55, 15],
    }
)

summary = sales.groupby("store").agg(
    total_units=("units", "sum"), average_revenue=("revenue", "mean")
)
print("Summary by store:\n", summary)

pivot = sales.pivot_table(index="store", columns="item", values="units", aggfunc="sum", fill_value=0)
print("Units by store and item:\n", pivot)

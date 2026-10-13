"""Interview: calculate a seven-day rolling total per store."""
import pandas as pd

sales = pd.DataFrame(
    {
        "store": ["A", "A", "A", "A", "B", "B", "B"],
        "date": pd.to_datetime(
            ["2025-01-01", "2025-01-03", "2025-01-07", "2025-01-09", "2025-01-01", "2025-01-04", "2025-01-08"]
        ),
        "amount": [10, 15, 8, 12, 7, 11, 5],
    }
).sort_values(["store", "date"])

sales = sales.set_index("date")
sales["rolling_7_day_sales"] = sales.groupby("store")["amount"].transform(
    lambda amounts: amounts.rolling("7D").sum()
)
print(sales.reset_index().to_string(index=False))
# A time-based window includes rows within the previous seven calendar days.

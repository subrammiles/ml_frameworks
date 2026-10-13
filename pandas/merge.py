"""Join related tables and work with dates."""
import pandas as pd

orders = pd.DataFrame(
    {"order_id": [101, 102, 103], "customer_id": [1, 2, 1], "date": ["2025-01-05", "2025-01-08", "2025-02-02"], "amount": [40, 65, 30]}
)
customers = pd.DataFrame({"customer_id": [1, 2], "customer": ["Asha", "Ben"]})

orders["date"] = pd.to_datetime(orders["date"])
orders = orders.merge(customers, on="customer_id", how="left")
orders["month"] = orders["date"].dt.to_period("M")

print("Orders with customer names:\n", orders)
print("Monthly revenue:\n", orders.groupby("month")["amount"].sum())

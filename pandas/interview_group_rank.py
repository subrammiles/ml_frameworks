"""Interview: find each department's two highest-paid employees."""
import pandas as pd

employees = pd.DataFrame(
    {
        "name": ["Asha", "Ben", "Chen", "Diya", "Eli", "Farah"],
        "department": ["Data", "Data", "Data", "Sales", "Sales", "Sales"],
        "salary": [120, 110, 110, 95, 105, 90],
    }
)

# dense rank includes ties at the cutoff; filter to rank <= 2.
employees["salary_rank"] = employees.groupby("department")["salary"].rank(
    method="dense", ascending=False
)
top_paid = employees.loc[employees["salary_rank"] <= 2].sort_values(
    ["department", "salary", "name"], ascending=[True, False, True]
)
print(top_paid.to_string(index=False))
# Follow-up: use method="first" if exactly two rows per department are required.

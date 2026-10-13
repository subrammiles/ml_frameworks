"""Build a readable chart with labels, a legend, and a clean layout."""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [120, 150, 135, 180, 210]
costs = [80, 95, 90, 110, 125]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(months, revenue, marker="o", label="Revenue")
ax.plot(months, costs, marker="s", label="Costs")
ax.set(title="Monthly revenue and costs", xlabel="Month", ylabel="Amount ($)")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()

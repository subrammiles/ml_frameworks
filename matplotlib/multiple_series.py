"""Compare group averages and show the spread of observations."""
import matplotlib.pyplot as plt
import numpy as np

groups = ["Group A", "Group B", "Group C"]
observations = [
    [68, 72, 70, 74, 69],
    [75, 78, 73, 80, 77],
    [82, 79, 85, 83, 81],
]
averages = [np.mean(group) for group in observations]
spread = [np.std(group, ddof=1) for group in observations]

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(groups, averages, yerr=spread, capsize=5, color=["#4C78A8", "#F58518", "#54A24B"])
ax.set(title="Average score by group", ylabel="Score")
ax.set_ylim(0, 100)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
plt.show()

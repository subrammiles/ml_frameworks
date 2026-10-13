"""Filter and update array values with boolean masks."""
import numpy as np

temperatures = np.array([18.5, 22.0, 25.5, 30.0, 27.5])
hot_days = temperatures >= 25

print("Hot-day mask:", hot_days)
print("Hot temperatures:", temperatures[hot_days])

# Replace readings above 28 with 28.
temperatures[temperatures > 28] = 28
print("Capped temperatures:", temperatures)

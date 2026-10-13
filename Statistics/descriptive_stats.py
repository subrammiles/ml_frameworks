"""Compare measures of center and spread for two score groups."""
import numpy as np

class_a = np.array([68, 72, 75, 77, 78, 80, 82, 88])
class_b = np.array([60, 72, 74, 78, 78, 82, 90, 106])

for name, scores in [("Class A", class_a), ("Class B", class_b)]:
    print(f"{name}: mean={scores.mean():.1f}, median={np.median(scores):.1f}")
    print(
        f"  range={np.ptp(scores)}, population std={scores.std(ddof=0):.2f}, "
        f"sample std={scores.std(ddof=1):.2f}"
    )

# ddof=0 treats these values as the whole population; ddof=1 estimates spread
# from a sample and applies Bessel's correction.

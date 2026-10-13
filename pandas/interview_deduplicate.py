"""Interview: keep each user's most recent event, with a tie-breaker."""
import pandas as pd

events = pd.DataFrame(
    {
        "user": ["A", "A", "B", "A", "B"],
        "event_time": pd.to_datetime(
            ["2025-02-01 10:00", "2025-02-03 09:00", "2025-02-02 12:00", "2025-02-03 09:00", "2025-02-04 08:00"]
        ),
        "event_id": [1, 2, 3, 4, 5],
        "event": ["login", "view", "login", "purchase", "view"],
    }
)

# Sorting makes keep="last" deterministic when timestamps tie.
latest = events.sort_values(["event_time", "event_id"]).drop_duplicates("user", keep="last")
print(latest.sort_values("user").to_string(index=False))
# Follow-up: how would you retain all events tied for the latest timestamp?

#merging logic with pd.merge()

import pandas as pd

users = pd.DataFrame({
    "user_id": [101, 102, 103, 104],
    "country": ["US", "UK", "Canada", "Germany"],
    "subscription": ["Free", "Pro", "Pro", "Free"]
})

print("User dataset: \n", users)

logs = pd.DataFrame({
    "user_id": [101, 102, 102, 103],
    "latency_ms": [120, 95, 105, 85],
    "tokens_generated": [150, 300, 250, 400]
})

print("\nLogs dataset: \n", logs)

#Merge the data

merged = pd.merge(
        logs,
        users,
        on = "user_id",
        how = "left"
        )
print("After left merging on key user_id \n", merged)


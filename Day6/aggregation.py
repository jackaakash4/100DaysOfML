#Aggregation with groupby()

import pandas as pd

#dataset
logs = pd.DataFrame({
    "hardware": [
        "CPU",
        "CPU",
        "GPU",
        "GPU",
        "GPU",
        "CPU"
    ],
    "latency_ms": [
        120,
        110,
        70,
        80,
        75,
        130
    ]
})

#mean
print("Mean latency: \n", logs.groupby("hardware")["latency_ms"].mean())

#standard deviation
print("Standard deviation: \n", logs.groupby("hardware")["latency_ms"].std())

#multiple statistics
print("Multiple statistics: \n", logs.groupby("hardware")["latency_ms"].agg(
    ["mean", "std", "min", "max"]))

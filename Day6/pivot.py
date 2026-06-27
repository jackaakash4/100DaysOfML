#Using pivot_table()
#more flexible aggregation tool

import pandas as pd

#dataset
logs = pd.DataFrame({
    "hardware": ["CPU", "CPU", "GPU", "GPU"],
    "region": ["US", "EU", "US", "EU"],
    "latency_ms": [120, 130, 75, 80]
})

#mean by hardware and region

pivot_mean = pd.pivot_table(
        logs, 
        values = "latency_ms",
        index = "hardware",
        columns = "region",
        aggfunc = "mean"
        )

print("Mean by hardware and region using pivot_table(): \n", pivot_mean)

#Ai_flavored challenge
import pandas as pd
import numpy as np

users = pd.DataFrame({
    "user_id": [1,2,3,4],
    "hardware": ["CPU","GPU","GPU","CPU"]
})

logs = pd.DataFrame({
    "user_id": [1,2,2,3,4],
    "latency_ms": [120,80,np.nan,70,140],
    "loss": [0.9,0.4,0.2,0.1,np.nan]
})

#task1
#Merge the datasets

merged = pd.merge(
        users,
        logs,
        on = "user_id",
        how = "left"
        )
print("After merged: \n", merged)

#task2
#fill missing latency values using mean imputation

merged['latency_ms'] = merged['latency_ms'].fillna(
        merged['latency_ms'].mean()
        )
print("\nAfter mean imputation: \n", merged)

#task3
#handle missing loss values first
merged['loss'] = merged['loss'].fillna(
        merged['loss'].mean()
        )

merged['loss_bucket'] = merged['loss'].apply(
        lambda x:
            "High" if x > 0.8
            else "Medium" if x > 0.3
            else "Low"
            )

print("\nAfter applying lambda function: \n", merged)

#task 4
#mean latency
#std latency


merged_statistic = merged.groupby("hardware")["latency_ms"].agg(
        ["mean", "std"])
print("\nMean and standard deviation of latency: \n", merged_statistic)

#task 5
#create a pivot table

merged_pivot = pd.pivot_table(
        merged,
        index = "hardware",
        values = "latency_ms",
        aggfunc = "mean"
        )
print("\nPivot table: \n", merged_pivot)

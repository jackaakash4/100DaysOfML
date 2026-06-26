import pandas as pd

df = pd.DataFrame({
    "accuracy": [0.82, 0.91, 0.95],
    "status": ["bad", "good", "good"]
    })

print("Dataframe: \n", df)

#cleaning using iloc 
#updating the status which accuracy is greater than 0.9

df.loc[df["accuracy"] > 0.9, "status"] = "excellent"

print("\nAfter update \n", df)

import pandas as pd
import numpy as np

#Feature engineering with apply()

df = pd.DataFrame({
    "loss": [
        0.95,
        0.60,
        0.32,
        0.12,
        0.80
    ]
})

#using .apply()

df['loss_bucket'] = df['loss'].apply(
        lambda x:
            "High" if x > 0.8
            else "Medium" if x > 0.3
            else "Low"
        )

print("After feature engineering: \n", df)

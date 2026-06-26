#iloc and loc for selection

import pandas as pd

df = pd.DataFrame({
    "Model": ["CNN", "Transformer", "LSTM"],
    "Accuracy": [0.82, 0.91, 0.95]
})

print("Dataset: \n", df)
print("Selection by position using iloc: \n", df.iloc[0])

print("Selection all except first row using iloc: \n", df.iloc[1:])

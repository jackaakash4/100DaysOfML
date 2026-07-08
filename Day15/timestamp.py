#Time series signal
#extracting the cyclic patterns of timestamp

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Timestamp': pd.to_datetime([
        '2026-07-08 09:15:00', '2026-07-08 14:30:00',
        '2026-07-09 22:45:00', '2026-07-11 03:10:00',
        '2026-12-24 18:00:00'
    ])
})

print("Dataset: \n", df)

#1. Hour of day

df['Hour_of_Day'] = df['Timestamp'].dt.hour

#2. Day of week

df['Day_of_Week'] = df['Timestamp'].dt.dayofweek

#3. is it weekend? - a boolean a liner model can weight directly

df['is_weekend'] = df['Timestamp'].isin([5, 6]).astype(int)

#4. Month
df['Month'] = df['Timestamp'].dt.month

#5. Cyclical encoding of hour
df['Hour_sin'] = np.sin(2 * np.pi * df['Hour_of_Day'] / 24)
df['Hour_cos'] = np.cos(2 * np.pi * df['Hour_of_Day'] / 24)

print("\n", df.to_string())

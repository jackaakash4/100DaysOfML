#cleaning pipeline
#real datasets always contain missing values
#use when missing values are relatively rare and we don't want to lose rows

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "loss": [0.35, np.nan, 0.22, np.nan, 0.15]
})

print("Dataframe: \n", df)

#strategy 1: Mean imputation
df['loss_mean'] = df['loss'].fillna(
        df['loss'].mean()
        )

print("Dataframe after mean imputation: \n", df)

#Strategy 2: Constant fill
#replace with a fixed value

df['loss_constant'] = df['loss'].fillna(0)
print("Dataframe after constant fill: \n", df)


#Strategy 3: Drop missing rows
df_drop = df.dropna()
print("Dropping the missing rows: \n", df_drop)


"""
    Binning: converts the continuous number into category

"""

import pandas as pd
import numpy as np

np.random.seed(42)

#skewed income data

income = np.concatenate([
    np.random.normal(50000, 15000, 90),
    np.random.normal(400000, 100000, 10)    #high earners, rare
    ])

income = np.clip(income, 15000, None)   #min = 15000 max=None

df = pd.DataFrame(
        {
            'income': income
        })

#Equal-WIDTH: cuts the Range into equal-sized chunks
df['bin_width'] = pd.cut(df['income'], bins = 4)

#Equal-Frequency: cuts so each bin has the same count of people
df['bin_freq'] = pd.qcut(df['income'], q = 4)

print("Equal width: ", df['bin_width'].value_counts().sort_index())
print("\nEqual frequency: ", df['bin_freq'].value_counts().sort_index())


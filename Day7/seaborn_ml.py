import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

#dataset
df = pd.DataFrame({
    "Feature_A": np.random.randn(100),
    "Feature_B": np.random.randn(100),
    "Feature_C": np.random.randn(100),
    "Feature_D": np.random.randn(100)
})
print("\nDataset: \n", df)

#compute correlation
corr = df.corr()
print("\nCorrelation of dataset: \n", corr)

#visualization

plt.figure(figsize = (6, 5))

sns.heatmap(
        corr,
        annot = True,
        cmap=sns.color_palette("rocket", as_cmap=True),
        linewidths = 0.5
        )
plt.title("Feature correlation matrix ")
plt.show()

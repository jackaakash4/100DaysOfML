#1. heatmap
#generate random dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

df = pd.DataFrame(
        np.random.randn(200, 10),
        columns = [f"Feature_{i}" for i in range(10)]
        )

print("Random dataset: \n", df)

#correlation

corr = df.corr()
print("Correlation: \n", corr)

#visualize
sns.heatmap(
        corr,
        annot = True,
        cmap = "coolwarm",
        )
plt.show()

fig, axes = plt.subplots(1, 2, figsize = (12, 5))

axes[0].hist(df["Feature_0"], bins = 20)
axes[0].set_title("Histogram")


#create a category
df['Category'] = np.random.choice(
        ["A", "B"],
        size = len(df)
        )

sns.violinplot(
        data = df,
        x = "Category",
        y = "Feature_0",
        ax = axes[1]
        )

axes[1].set_title("violin plot")
plt.tight_layout()
plt.show()


#Task3: INteractive 3D scatter plot

import plotly.express as px

fig = px.scatter_3d(
        df,
        x = "Feature_0",
        y = "Feature_1",
        z = "Feature_2",
        color = "Category",
        title = "#D feature space"
        )
fig.show()

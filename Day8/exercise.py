"""
AI-Flavored Coding Exercise

Imagine a dataset of 1,000 model training runs.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

runs = pd.DataFrame({
    "Loss": np.random.gamma(2, 0.3, 1000),
    "Inference_Latency": np.random.normal(100, 20, 1000),
    "Learning_Rate": np.random.uniform(0.0001, 0.01, 1000),
    "Accuracy": np.random.uniform(0.6, 0.99, 1000)
})

# Add a few extreme latency outliers
runs.loc[[25, 300, 700], "Inference_Latency"] *= 6

"""
Task 1 — Univariate Check
"""
sns.histplot(
        runs['Loss'],
        kde = True
        )
plt.show()
"""
Questions:

Is the loss approximately normal?
No
Is it positively skewed?
Yes

"""


"""Task 2"""
#outlier hunt

sns.boxplot(
        x = runs["Inference_Latency"]
        )
plt.show()

#dentify runs where latency is at least 5× the median:

median_latency = runs["Inference_Latency"].median()

slow_runs = runs[
        runs["Inference_Latency"] >= 5 * median_latency
        ]

print("Slow run: ", slow_runs)

#TAsk 3: bivariate relationship

sns.scatterplot(
        data = runs,
        x = "Learning_Rate",
        y = "Accuracy"
        )
plt.show()

"""
Is there a trend?
No

Does a higher learning rate consistently improve accuracy?
Nope
Or is the relationship weak?
Yes, the relationship is weak.


"""


corr = runs.corr(numeric_only = True)

sns.heatmap(
        corr,
        annot = True,
        cmap = "coolwarm"
        )
plt.show()

"""
Which feature has the strongest positive correlation with Accuracy?


"""
corr["Accuracy"].sort_values(ascending=False)
print("After sorting \n", corr)

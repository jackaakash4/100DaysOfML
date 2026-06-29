"""Coding Challenge

Choose either the Titanic or Iris dataset.

Task 1

Load the dataset. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")
print("Iris dataset: \n", df)



"""Task 2

Identify the target variable.

"""

#quick inspection
print("Iris dataset's info: \n", df.info())

print("Iris dataset's describe: \n", df.describe())

print("Iris dataset's shape: \n", df.shape)

#target variable is species 
sns.countplot(data = df, x = "species")
plt.show()

"""Task 3

Keep only numerical columns:

numeric = df.select_dtypes(include="number")

"""
numeric = df.select_dtypes(include = "number")

print("Numberic dataset only :\n", numeric.head())

"""Task 4

Compute the correlation matrix:

corr = numeric.corr()

"""
corr = numeric.corr()
"""Task 5

Find the three features most correlated with the target.

"""

sns.heatmap(
        data = corr,
        annot = True,
        cmap = 'coolwarm'
        )
plt.show()





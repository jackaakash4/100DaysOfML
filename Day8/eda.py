#EDA
#Exploratory Data Analysis

#step 1 load and inspect the dataset

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore

df = sns.load_dataset("titanic")
print("Dataset: \n", df.head())

#quick inspection
print("\nDataset info: \n", df.info())

print("\nDataset describe: \n", df.describe())

print("\nDataset shape: \n: ", df.shape)


#checking the datatypes
print("\nDatatypes: \n", df.dtypes)

#step 3: Study the target variable
#target = "survived"

sns.countplot(data = df, x = "survived")
plt.show()

#Step 4: Analyze individual feature

sns.histplot(
        data = df,
        x = "age",
        bins = 20,
        kde = True
        )

plt.show()


#step 5: outlier detection
#outlier distort training 
#to solve it. There are two approach.

#method 1 - IQR(Interquartile range)
#iqr = Q3 - Q1
#lower = Q1 - 1.5 * IQR
#upper = Q3 + 1.5 * IQR

Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
        (df["fare"] < lower) |
        (df["fare"] > upper)
        ]

print("Outlier in fare: ", outliers.head())

#Method 2 - Z-score

df["fare_z"] = zscore(
        df["fare"].fillna(
            df["fare"].mean()
            ))

outliers_from_z = df[
        abs(df["fare_z"]) > 3
        ]
print("Outliers from z-score: \n", outliers_from_z.head())

#visualizing outliers

sns.boxplot(
        data = df,
        x = "fare"
        )
plt.show()

#beyond the whiskers are potential outliers
#removing them blindly can hurt our model

#step 6: handling skewness
#measure skewness

print("Measuring skewness: \n", df['fare'].skew())

#it is positive skewed
#so it dominate optimization and slow convergence

#let's fix it with 
#log transformation
#log1p = log(1 + x)
#why log1p bcoz it handle zeros safely

df["fare_log"] = np.log1p(df['fare'])
print("AFter log(1 + x) transformation : ", df["fare_log"])


#let's compare before and after

fig, axex = plt.subplots(1, 2, figsize  = (10, 4))

sns.histplot(df["fare"], ax = axex[0], kde = True)
axex[0].set_title("Orginal")

sns.histplot(df["fare_log"], ax = axex[1], kde = True)
axex[1].set_title("Log transformation")

plt.show()
#it becomes much symmetric than original after log transformation


#step 7: Relationship with the target
#does fare affect survival

sns.boxplot(
        data = df,
        x = "survived",
        y = "fare"
        )
plt.show()

sns.violinplot(
        data = df,
        x = "survived",
        y = "fare"
        )
plt.show()

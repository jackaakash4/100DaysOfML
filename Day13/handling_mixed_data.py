#Handling mixed data with ColumnTransformer

#sample data
import pandas as pd

df = pd.DataFrame({
    "learning_rate": [0.001, 0.01, 0.005],
    "optimizer": ["Adam", "SGD", "Adam"],
    "accuracy": [1, 0, 1]
})

#separate features
X = df.drop("accuracy", axis=1)

y = df['accuracy']

#Define column
numerical_features = df["learning_rate"]

categorical_features = df["optimizer"]

#building the transformer
from sklearn.compose import ColumnTransformer
form sklearn.preprocessing import (
        StandardScaler,
        OneHotEncoder
        )

preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                numerical_features
            ),
            (
                "cat",
                OneHotEncoder(),
                categorical_features
            )
        ]
    )

"""
Numerical columns -> standardized
Categorical columns -> One-hot Encoded
"""
#Combine with mode

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier)
    ])
#Training
pipeline.fit(X,y)

#Prediction
pipeline.predict(X)




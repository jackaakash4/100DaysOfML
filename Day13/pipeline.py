#Building the first pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#creating a pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression)
    ])

#training

pipeline.fit(X_train, y_train)
#it automatically train logistic regression

#predict
predictions = pipeline.predict(X_test)




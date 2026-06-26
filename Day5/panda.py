
#Day 5
#pandas library

import pandas as pd

#series
#a single feature(column)
accuracy = pd.Series([0.82, 0.91, 0.95])
print("Accuracy as series: ", accuracy)

#Dataframe = complete dataset
#multiple series combined into a table

models = pd.DataFrame({
    "Model_name": ["CNN", "Transformer", "LSTM"],
    "Accuracy": accuracy,
    "Epochs": [10, 20, 15]
    })
print("Model as dataframe: \n", models)

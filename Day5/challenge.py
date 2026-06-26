import pandas as pd

runs = {
    "Run_ID": [101, 102, 103, 104, 105],
    "Model_Type": [
        "CNN",
        "Transformer",
        "Transformer",
        "LSTM",
        "Transformer"
    ],
    "Accuracy": [0.84, 0.91, 0.97, 0.88, 0.93],
    "Learning_Rate": [0.01, 0.001, 0.0005, 0.01, 0.001],
    "Epochs": [10, 20, 25, 15, 30]
}

#Task 1
#Convert the dictionary into a DataFrame.

df = pd.DataFrame(runs)
print("Dataset: \n", df)

#Task2
#Observe the dataset

#first 10 sample of datasets
print("Sample of dataset: \n", df.head())

#Information about datasets
print("\nINformation of dataset: \n", df.info())

#Describing the dataset
print("\nDescription of dataset: \n", df.describe())

#Task3
#Extract only
#Model_Type
print("\nExtracting the Model_type only \n", df["Model_Type"])

#Accuracy
print("\nExtracting the Accuracy only \n", df["Accuracy"])

#Task 4
#find all sucessful runs i.e accuracy > 0.90

print("\nAll sucessful run: \n", df[df["Accuracy"] > 0.90])

#Task 5
#find all sucessful transformer runs

print("\nAll sucessful transforemer runs: \n",
      df[
          (df["Model_Type"] == "Transformer")
          &
          (df["Accuracy"] > 0.90)
          ])

#Task6
#create a new column high performer and add true if accuracy is greater or equal to 0.95 else false

df["High_performer"] = df["Accuracy"] >= 0.95 
print("\nNew dataset after update: \n", df.head())


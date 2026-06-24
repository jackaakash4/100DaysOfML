import numpy as np

#real preprocessing step used in ML

#dataset
data = np.array([
    [10, 100, 5],
    [20, 200, 10],
    [30, 300, 15],
    [40, 400, 20],
    [50, 500, 25]
    ])

#step1: Mean per feature

mean = data.mean(axis = 0)  #axix = 0 means calculate down each column

#displaying the mean of each feature
print("Mean of each features: \n", mean)

#Step2: Standard Deviation
#standard deviation of each feature
std = data.std(axis = 0)
print("\nStandard deviation of each features: \n", std)

#Step3: Normalize

normalized = (data - mean)/std

print("\nNormalized data: \n", normalized)

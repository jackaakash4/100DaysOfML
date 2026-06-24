import numpy as np

#dataset
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
    ])

#printing dataset
print("Dataset: ", data)
#shape
print("Shape of the dataset is \n", data.shape)

#select row

print("Selecting row: ", data[2])

#selecting column

print("Selecting column ", data[:, 0])

#selecting subb-matrix

print("Sub matrix: ", data[1:3, -1])




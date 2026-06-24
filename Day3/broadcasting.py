#Broadcasting
#Broadcasting lets arrays with different shapes interact

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

print("Matrix: \n", matrix)

#shape of matrix
print("\nShape of matrix is: \n", matrix.shape)


#creating the vector
vector = np.array([
    [10],
    [20],
    [30]
    ])

print("\n Vector: \n", vector)

#shape of vector
print("\nShape of vector: ", vector.shape)


#Adding them
print("\nAddition of matrix and vector is: \n", matrix + vector)

#what happen?
#vector stretched into shape of respective matrix


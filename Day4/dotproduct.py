import numpy as np

#vector
v1 = np.array([1, 2])
v2 = np.array([3, 4])

#compute
print(f"Dot product of {v1} and {v2} is {np.dot(v1, v2)}")


#vector matrix multiplication
matrix = np.array([
    [3, 4],
    [5, 6]
    ])

result = np.dot(v1, matrix)
print(f"Vector matrix multiplication of{v1} and {matrix} is {result}")

#Eigen vector and eigen value

import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
    ])

values, vectors = np.linalg.eig(A)

print(f"Eigen vector is {vectors} and eigen value is {values}")



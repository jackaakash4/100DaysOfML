import numpy as np

#creation of matrix

A = np.array([
    [2, 1],
    [1, 1]
    ])

print("A matrix: ", A)
#inverse of A matrix

A_inv = np.linalg.inv(A)
print("\nInverse of A matrix: ", A_inv)

#verification
print(A @ A_inv, " Must gives indentity matrix")

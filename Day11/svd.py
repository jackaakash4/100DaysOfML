#Singular value decomposition(svd)
#svd implementation using numpy

import numpy as np

image = np.random.rand(100, 100)

U, S, Vt = np.linalg.svd(image)

#keep only
k = 20

#largest singular values

compressed = (
        U[:, :k]
        @ np.diag(S[:k])
        @ Vt[:k, :]
        )

#compressed 100 * 100 into rank 20 approximationo(much smaller representation)

print("U: ", U)
print("\nS: ", S)
print("\nVt: ", Vt)

print("After compression: \n", compressed)

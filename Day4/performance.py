#performance challenge
#traditional vs numpy matrix multiplication

import numpy as np

rng = np.random.default_rng(42)

A = rng.random((300, 300))
B = rng.random((300, 300))

#manual matrix multiplication
def manual_matmul(A, B):
    rows = A.shape[0]
    cols = B.shape[1]
    inner = A.shape[1]
    result = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i, j] += A[i, k] * B[k, j]

    return result

#mesure time
import time

start = time.time()

manual_result = manual_matmul(A, B)
manual_time = time.time() - start

print("Manual time: ", manual_time)


#numpy
start = time.time()
numpy_result = np.matmul(A, B)
numpy_time = time.time() - start
print("NUmpy time: ", numpy_time)


print(f"Manual: {manual_time:.4f}s")
print(f"Numpy time: {numpy_time: .4f}s")

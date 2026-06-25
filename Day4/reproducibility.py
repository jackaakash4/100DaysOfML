#Traditional seed

import numpy as np

np.random.seed(42)
data = np.random.rand(5)

print("Traditional approach random data generator: ",data)

#Modern generator api

rng = np.random.default_rng(42)
modern_data = rng.random(5)
print("Modern Numpy approach: ",modern_data)

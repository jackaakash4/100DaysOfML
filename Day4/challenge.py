import numpy as np

#X - Feature
#w - weight

rng = np.random.default_rng(42)

X = rng.random((1000, 50))
w = rng. random((50, 10))

#prediction is Xtimew

prediction = np.matmul(X, w)
print("Prediction: ", prediction)

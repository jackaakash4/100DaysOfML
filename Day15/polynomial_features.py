#Polynomial features

from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.array([
    [2, 3],
    [4, 1],
    [5, 5]
    ])

poly = PolynomialFeatures(degree = 2, interaction_only = False, include_bias = False)

X_poly = poly.fit_transform(X)

print(X_poly)



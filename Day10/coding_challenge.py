"""
Coding Challenge — A/B Testing

Imagine your recommendation system has a new ranking algorithm.

Current System:
"""
import numpy as np
from scipy.stats import ttest_ind

np.random.seed(42)

A = np.random.normal(
    0.18,
    0.04,
    100
)

#New System:

B = np.random.normal(
    0.20,
    0.04,
    100
)

"""Think of these values as click-through rates.

Task 1

Calculate:
mean

"""
print("Mean of model A: ", A.mean())
print("Mean of model B: ", B.mean())

"""
Task 2

Perform:
t-test

"""
t_stats, p_test = ttest_ind(
        A,
        B
        )
print("T-test statistics is : ", t_stats, " p value is ", p_test)


"""
Task 3

Decision

If:

p < 0.05

Deploy?

Otherwise:

Keep the current system.
"""
if p_test < 0.05:
    print("Its a signal so deploy the model. It has improved")
else:
    print("Keey the current system. It is a noise")


"""
Also consider whether the improvement is practically meaningful, not just statistically significant. For example, a tiny improvement may not justify deployment costs.
"""

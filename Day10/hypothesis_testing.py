"""Hypothesis testing

Define Hypotheses
Null Hypothesis(Ho)

Model A and Model B perform equally


Alternative hypothesis(H1)
Model B performs better than Model A

"""

#Simulate Results
import numpy as np

np.random.seed(42)

model_A = np.random.normal(
        loc = 0.92,
        scale = 0.02,
        size = 30
        )

model_B = np.random.normal(
        loc = 0.94,
        scale = 0.02,
        size = 30
        )

#perform T-test
from scipy.stats import ttest_ind

t_stat, p_stat = ttest_ind(
        model_A,
        model_B
        )

print("T-statistics: ", t_stat, " and P-statistic: ", p_stat)

#Decision rule

if p_stat < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

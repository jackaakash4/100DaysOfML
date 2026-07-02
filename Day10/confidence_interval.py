#Confidence intervals

import numpy as np
from scipy.stats import sem, t
latency = np.array([
    95,102,100,98,97,
    101,99,103,100,96
])

#calculate mean
mean = np.mean(latency)
print("The mean is ", mean)

#calculate standard error


standard_err = sem(latency)
print("Standard error: ", standard_err)

#compute 95% confidence interval
confidence = 0.95

ci = t.interval(
        confidence,
        df = len(latency) - 1,
        loc = mean,
        scale = standard_err
        )

print("The confidence interval: ", ci)

"""
Interpretation:
    Based on this sample and method, we are 95% confident that the procedure used to construct the interval captures the true average inference latency



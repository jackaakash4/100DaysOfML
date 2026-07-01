#Central Limit Theorem(CLT)
"""
Statement:
    Even if the original population is highly skewed,
    the distribution of sample means becomes approximately normal as the sample size grows

"""

#simulation
#skewed population
import numpy as np
import matplotlib.pyplot as plt

population = np.random.exponential(
        scale = 2,
        size = 100000
        )

plt.hist(population, bins = 50)
plt.title("Original Population")
plt.show()

#sample from it
sample_mean = []

for _ in range(1000):
    sample = np.random.choice(
            population,
            size = 30
            )
    sample_mean.append(sample.mean())

#visualize
plt.hist(sample_mean, bins = 40)
plt.title("Distribution of sample mean")
plt.show()

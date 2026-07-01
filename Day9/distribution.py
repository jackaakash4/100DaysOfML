#Distribution recognization
#normal distribution
#mean = 0
#sd = 1

import numpy as np
import matplotlib.pyplot as plt

normal = np.random.normal(
        loc = 0,
        scale = 1,
        size = 10000
        )

plt.hist(normal, bins = 40)
plt.title("Normal distribution ")
plt.show()

#Poisson Distribution
#models counts

poisson = np.random.poisson(
        lam = 5,
        size = 1000
        )

plt.hist(poisson, bins = 20)
plt.title("Poisson Distribution")
plt.show()

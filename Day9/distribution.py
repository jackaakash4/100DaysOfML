#Distribution recognization
#normal distribution

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


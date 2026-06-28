#common ml workflow
#load data -> visualize -> detect outliers -> check feature relationship -> train model

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x ** 2

fig, ax = plt.subplots(figsize = (6, 4))

#creating a simple sub plot
ax.plot(x, y)
ax.set_title("Quadratic function")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()


#creating a 2*2 grid of subplots
xx = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize = (10, 8))

axes[0, 0].plot(xx, np.sin(xx))
axes[0, 0].set_title("Sine")

axes[0, 1].plot(xx, np.cos(xx))
axes[0, 1].set_title("Cosine")

axes[1, 0].plot(xx, np.exp(xx/5))
axes[1, 0].set_title("Exponential")

axes[1, 1].plot(xx, np.sqrt(xx))
axes[1, 1].set_title("Square root")

plt.tight_layout()
plt.show()

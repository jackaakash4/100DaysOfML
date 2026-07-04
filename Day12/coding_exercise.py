#Coding eercise
#f(x) = x^2

import numpy as np
import matplotlib.pyplot as plt

#define f(x)
def f(x):
    return x**2

#define gradient descent
def grad(x):
    return 2*x

#for visualization adding history of x
history = []
#initialize

learning_rate = 0.1

x = 10

#run gradient descent

print("i\tx\tf(x)\n")
for i in range(20):

    gradient = grad(x)
    history.append(x)
    x = x - learning_rate * gradient

    
    print(f"{i+1}\t{x}\t{f(x)}\n")

#visualizing optimization

xs = np.linspace(-1, 10, 200)
ys = xs ** 2

plt.plot(xs, ys, label="f(x)=x^2")
plt.scatter(history, [h**2 for h in history], color = "red", label="Gradient Descent Step")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent toward the minimun")
plt.legend()
plt.show()

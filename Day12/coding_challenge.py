#Gradient Descent with numpy

#import package
import numpy as np

#define the function
def f(x):
    return (x**2) - (4 * x) + 4

#define the gradient
def grad(x):
    return 2*x -4

#initialize 
x = 10

learning_rate = 0.1

iteration = 30

#optimization loop

for i in range(iteration):
    gradient = grad(x)
    x = x - learning_rate * gradient
    print(
            f"Iteration {i+1}: x = {x:.4f}, loss = {f(x):.4f}"
            )

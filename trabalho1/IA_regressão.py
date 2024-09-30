import numpy as np
from matplotlib.pyplot import subplot, plot, show, clf, vlines

import matplotlib.pyplot as plt

# conjunto de dados {(x,y)}
mean0, std0 = -0.4, 0.5
mean1, std1 = 0.9, 0.3
m = 200

x1s = np.random.randn(m // 2) * std1 + mean1
x0s = np.random.randn(m // 2) * std0 + mean0
xs = np.hstack((x1s, x0s))

ys = np.hstack((np.ones(m // 2), np.zeros(m // 2)))

plot(xs[:m // 2], ys[:m // 2], '.')
plot(xs[m // 2:], ys[m // 2:], '.')
show()

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def h(x, theta):
    return sigmoid(theta[0] + theta[1] * x)

def cost(h, y):
    return -y * np.log(h) - (1 - y) * np.log(1 - h)

def J(theta, xs, ys):
    m = len(ys)
    total_cost = 0
    for i in range(m):
        total_cost += cost(h(xs[i], theta), ys[i])
    return total_cost / m

def gradient(i, theta, xs, ys):
    m = len(ys)
    grad = 0
    for j in range(m):
        grad += (h(xs[j], theta) - ys[j]) * (xs[j] if i == 1 else 1)
    return grad / m

def plot_fronteira(theta):
    vlines()

def print_modelo(theta, xs, ys):
    clf()
    plot(xs[:m // 2], ys[:m // 2], '.')
    plot(xs[m // 2:], ys[m // 2:], '.')
    plot_fronteira(theta)
    show()

def accuracy(ys, predictions):
    num = sum(ys == predictions)
    return num / len(ys)

alpha = 0.1
epochs = 600
theta = np.zeros(2)

for k in range(epochs):
    theta[0] -= alpha * gradient(0, theta, xs, ys)
    theta[1] -= alpha * gradient(1, theta, xs, ys)

predictions = h(xs, theta) >= 0.5
print('Acuracia:', accuracy(ys, predictions))
print_modelo(theta, xs, ys)
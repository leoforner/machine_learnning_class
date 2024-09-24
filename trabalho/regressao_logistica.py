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
    sig = 1 / (1 + np.exp(-z))
    return sig

''' hipotese
sigmoid(theta[0] + theta[1] * x)
'''
def h(x, theta):
    hip = sigmoid(theta[0] + theta[1] * x)
    return hip

''' funcao de custo para um exemplo ; entropia cruzada
'''
def cost(h, y):
    cost = -y * np.log(h) - (1 - y) * np.log(1 - h)
    return cost
    

''' funcao de custo total
'''
def J(theta, xs, ys):
    j = sum([cost(h(xs[i], theta), ys[i]) for i in range(len(ys))])
    return j


''' derivada parcial com respeito a theta[i]
'''
def gradient(i, theta, xs, ys):
    return theta[i] - (alpha / len(ys)) * sum([(h(xs[j], theta) - ys[j]) * xs[j]**i for j in range(len(ys))])

def plot_fronteira(theta):
    plt.vlines(-theta[0] / theta[1], ymin=-0.1, ymax=1.1, colors='r')
    

''' plota em subplots: - os dados, com a fronteira de decisao
- e os dados classificados
'''
def print_modelo(theta, xs, ys):
    clf()
    plot(xs[:m // 2], ys[:m // 2], '.')
    plot(xs[m // 2:], ys[m // 2:], '.')
    plot_fronteira(theta)
    show()


def accuracy(ys, predictions):
    num = sum(ys == predictions)
    return num / len(ys)


alpha = 0.1 # completar
epochs = 600
theta = [1,2] # completar

for k in range(epochs): # 10000
    # apply gradient decent
    theta[0] = gradient(0, theta, xs, ys)
    theta[1] = gradient(1, theta, xs, ys)


# show classication performance

predictions = h(xs, theta) >= 0.5
print('Acuracia:', accuracy(ys, predictions))
print_modelo(theta, xs, ys)
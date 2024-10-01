import numpy as np
import numpy.random
import matplotlib.pyplot as plt


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


def make_cost(x, y):
    return np.array(numpy.random.uniform(-1, 1, (x, y + 1)))


def make_network(layer_size: list):
    layers = {}
    Delta = {}
    for i in range(len(layer_size) - 1):
        layers[i] = make_cost(layer_size[i + 1], layer_size[i])
        Delta[i] = np.zeros((layer_size[i + 1], layer_size[i]))
    return layers, Delta


def next_layer(val: list, cost, bias: int):
    next_layer = []
    for i in range(len(cost)):
        z = bias * cost[i][0]
        for j in range(len(cost[i]) - 1):
            z += val[j] * cost[i][j + 1]
        z = sigmoid(z)
        next_layer.append(z)
    return next_layer


def final_delta(xs: list,ys: list, web):
    forward = xs
    for i in range(len(web)):
        forward = next_layer(forward, web[i], 1)
    alpha = forward
    deltas = np.zeros(len(ys))
    for i in range(len(ys)):
        deltas[i] = alpha[i] - ys[i]
    return deltas

def previous_layer(web, deltas: list):
    d = 0
    temp_list = []
    row = len(web)
    column = len(web[0])
    for i in range(column):
        for j in range(row):
            d += web[j][i] * deltas[j]
        temp_list.append(d)
    return temp_list




data = np.loadtxt("classification2.txt", delimiter=',')
x1 = data[:,0]
x2 = data[:,1]
y = data[:,2]

#print(data)
'''class_0 = data[data['y'] == 0]
class_1 = data[data['y'] == 1]
plt.figure(figsize=(10,6))
plt.scatter(class_1['x1'],class_1['x2'], color='purple', label='class 1')
plt.scatter(class_0['x1'],class_0['x2'], color='orange', label='class 0')
plt.show()
'''
rede, Deltas = make_network([2,2,2,1])



delta_end = final_delta([0.63265,-0.030612],[0],rede)
print(delta_end)
print(previous_layer(rede[2], delta_end))
print(previous_layer(rede[1],previous_layer(rede[2],delta_end)))
print(previous_layer(rede[0],previous_layer(rede[1],previous_layer(rede[2],delta_end))))
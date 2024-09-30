import numpy as np
import numpy.random
import scipy.io

mat = scipy.io.loadmat('classification3.mat')
def make_cost(x,y):
    return np.array(numpy.random.uniform(-1, 1, (x,y)))

# obs: ultima camada sempre com apenas 1 item
def make_network(layer_size: list):
    layers = {}
    for i in range (len(layer_size)-1):
        layers[i] = make_cost(layer_size[i+1],layer_size[i])
    return layers

def next_layer(val: list, cost, bias: int):
    next_layer = []
    for i in range(len(cost)):
        x = bias
        for j in range(len(cost[i])):
            x += val[j]*cost[i][j]
        next_layer.append(x)
    return  next_layer

def back_prop(val:int, layers, network):
    for i in range(len(layers)-1):
        j = len(layers) - 1 - i
        for k in range(len(layers[j])):
            delta = layers[j][k] - val
            network[j][k] += delta

'''rede = make_network([3,3,3,3])
cost = np.array([(8,1),(3,2),(9,3)])
entrada = [1,1,1]
for i in range(len(rede)):
    print(entrada)
    entrada = next_layer(entrada, rede[i])
print(entrada)'''

temp = np.array(mat)
print(temp[0])
#By: Otacilio Netto
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

mt.use('TkAgg')
def f_true(x):
	return 2 + 0.8 * x



'''
hipotese
'''

def h(x, theta):
	return theta[0] + theta[1] * x

'''
funcao de custo
'''

def J(theta, xs, ys):
    sum = 0
    for i in range(len(ys)):
        sum += (h(xs[i], theta) - ys[i])**2
    return sum/ (2*len(ys))

'''
derivada parcial com respeito a theta [ i ]
'''

def gradient(i, theta, xs, ys):
    sum = 0
    m = len(ys)
    if i == 0:	
        for j in range(m):
            sum += h(xs[j], theta) - ys[j]
    elif i == 1:
        for j in range(m):
            sum += (h(xs[j], theta) - ys[j]) * xs[j]
    return (lr * sum / m)

'''
plota no mesmo grafico : - o modelo / hipotese ( reta )
- a reta original ( true function )
- e os dados com ruido ( xs , ys )
'''

def print_modelo(theta, xs, ys):
	# Plotar a função de fitness
    ax1.cla()
    ax1.plot(xs, ys, 'o', label='Dados com ruído')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    #plotar a reta real
    ax1.plot(xs, f_true(xs), label='Função real')
    #plotar a reta do modelo
    ax1.plot(xs, h(xs, theta), label='Modelo')
   
    #plotar a reta gerada pelo modelo linear (least squares)
    #ax1.plot(xs, predicted_ys, label='Least Squares', color='yellow')
    ax1.legend()
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, 7)
    #plotar a função custo
    ax2.plot(range(len(cost)), cost, label="learning rate: {}".format(lr), color="blue")
    ax2.legend()
    ax2.set_xlim(0, epocas)
    ax2.set_ylim(0, 3)
    ax2.set_xlabel('Iterações')
    ax2.set_ylabel('Custo')
    plt.show()
    #canvas.draw()
def step():
    tempTheta = list(theta)
    for j in range(len(theta)):
        theta[j] = theta[j] - gradient(j, tempTheta, xs, ys)
    cost.append(J(theta, xs, ys))
    
def update(frame):
     step()
     print_modelo(theta, xs, ys, frame)
# conjunto de dados {( x , y ) }
xs = np.linspace(-3, 3, 100)
ys = np.array([f_true(x) + np.random.randn() * 0.5 for x in xs])
theta = [0.3, 1]
cost = []
#lr: learning rate
lr = 0.5

#numero de iteracoes
epocas=5000
tempTheta = list(theta)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax2.legend()
fig.tight_layout(pad=3.0)
linearModel = LinearRegression().fit(xs.reshape(-1,1), ys)
predicted_ys = linearModel.predict(xs.reshape(-1, 1))
print("By: Otacilio Netto")
for i in range(epocas):
    step()
print_modelo(theta, xs, ys)

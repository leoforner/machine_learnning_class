import struct
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import argparse

# Analisar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Parâmetros do Algoritmo Genético')
parser.add_argument('--Pc', type=float, default=0.9, help='Probabilidade de crossover')
parser.add_argument('--Pm', type=float, default=0.01, help='Probabilidade de mutação')
parser.add_argument('--N', type=int, default=10, help='Tamanho da população')
parser.add_argument('--nF', type=int, default=100, help='Número de quadros')
args = parser.parse_args()

# Atribuir argumentos analisados a variáveis
Pc = args.Pc
Pm = args.Pm
N = args.N
nFrames = args.nF

L = 4 * 8  # tamanho do cromossomo em bits

def on_key_press(event):
    if event.keysym == 'q':
        print("A tecla 'q' foi pressionada")
        step()
        # Limpar o gráfico
        ax1.cla()
        # Redesenhar o gráfico
        ax1.plot(x, y_fitfunction)
        ax1.scatter(populacao, item_fitness_list, color='green')
        ax1.set_xlim(0, math.pi)
        ax1.set_ylim(0, 4.5)
        ax1.set_xlabel('x')
        ax1.set_ylabel('item_fitness')
        ax1.set_title('Fitness vs. x')
        canvas.draw()

def floatToBits(f):
    s = struct.pack('>f', f)
    return struct.unpack('>L', s)[0]

def bitsToFloat(b):
    s = struct.pack('>L', b)
    return struct.unpack('>f', s)[0]

def get_bits(x):
    x = floatToBits(x)
    N = 4 * 8
    bits = ''
    for bit in range(N):
        b = x & (2**bit)
        bits += '1' if b > 0 else '0'
    return bits

def get_float(bits):
    x = 0
    assert (len(bits) == L)
    for i, bit in enumerate(bits):
        bit = int(bit)
        x += bit * (2**i)
    return bitsToFloat(x)

def is_valid_chromosome(chromosome):
    fchromosome = get_float(chromosome)
    if math.isnan(fchromosome) or fchromosome < 0 or fchromosome > math.pi:
        return False
    return True

def roleta_russa(populacao, fitness):
    soma_fitness = sum(fitness)
    if soma_fitness == 0:
        return None
    valor_roleta = random.uniform(0, soma_fitness)
    acumulado = 0
    for i, individuo in enumerate(populacao):
        acumulado += fitness[i]
        if acumulado >= valor_roleta:
            return individuo
    return None

def crossover(cromossomo1, cromossomo2, Pc):
    r = random.uniform(0, 1)
    if r < Pc:
        ponto_corte = random.randint(1, L-1)
        filho1 = cromossomo1[:ponto_corte] + cromossomo2[ponto_corte:]
        filho2 = cromossomo2[:ponto_corte] + cromossomo1[ponto_corte:]
        if is_valid_chromosome(filho1) and is_valid_chromosome(filho2):
            return filho1, filho2
    return cromossomo1, cromossomo2

def mutacao(cromosso_):
    r = random.uniform(0, 1)
    if r < Pm:
        ponto_mutacao = random.randint(0, L-1)
        cromosso_list = list(cromosso_)
        cromosso_list[ponto_mutacao] = '1' if cromosso_list[ponto_mutacao] == '0' else '0'
        cromosso = ''.join(cromosso_list)
        if is_valid_chromosome(cromosso):
            return cromosso
    return cromosso_

def step():
    global populacao
    global item_fitness_list
    item_fitness_list = [item + abs(math.sin(32*item)) for item in populacao]
    novaPopulacao = []
    while len(novaPopulacao) < N:
        cromossomo1 = roleta_russa(populacao, item_fitness_list)
        cromossomo2 = roleta_russa(populacao, item_fitness_list)
        if cromossomo1 == cromossomo2:
            continue
        cromossomo1_bin = get_bits(cromossomo1)
        cromossomo2_bin = get_bits(cromossomo2)
        filho1, filho2 = crossover(cromossomo1_bin, cromossomo2_bin, Pc)
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)
        novaPopulacao.append(get_float(filho1))
        novaPopulacao.append(get_float(filho2))
    populacao = novaPopulacao
    item_fitness_list = [item + abs(math.sin(32*item)) for item in populacao]

def update(frame):
    step()
    ax1.cla()
    ax1.plot(x, y_fitfunction, label=f'Pc={Pc}, Pm={Pm}, N={N}')
    ax1.set_xlim(0, math.pi)
    ax1.set_ylim(0, 4.2)
    ax1.scatter(populacao, item_fitness_list, color='green')
    ax1.set_xlabel('x')
    ax1.set_ylabel('item_fitness')
    ax1.set_title('Fitness vs. x')
    ax1.legend()

    average_fitness.append(np.mean(item_fitness_list))
    ax2.cla()
    ax2.plot(average_fitness, label='Média de Fitness')
    ax2.set_xlim(0, nFrames)
    ax2.set_ylim(0, 4.2)
    ax2.set_xlabel('Frame')
    ax2.set_ylabel('Média de Fitness')
    ax2.set_title(f'Média de Fitness no tempo (Pc={Pc}, Pm={Pm}, N={N})')
    ax2.legend()

    canvas.draw()

# Inicializar população
populacao = [random.uniform(0, math.pi) for _ in range(N)]

y_fitfunction = [i + abs(math.sin(32*i)) for i in np.arange(0, math.pi, 0.001)]
x = np.arange(0, math.pi, 0.001)
item_fitness_list = [item + abs(math.sin(32*item)) for item in populacao]

# Criar uma janela tkinter para capturar eventos de teclado
root = tk.Tk()
root.title("Animação do Algoritmo Genético")

# Criar uma figura Matplotlib e plotar
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
fig.tight_layout(pad=3.0)

# Plotar a função de fitness
ax1.plot(x, y_fitfunction, label=f'Pc={Pc}, Pm={Pm}, N={N}')
ax1.set_xlim(0, math.pi)
ax1.set_ylim(0, 4.2)
ax1.scatter(populacao, item_fitness_list, color='green')
ax1.set_xlabel('x')
ax1.set_ylabel('item_fitness')
ax1.set_title('Fitness vs. x')
ax1.legend()

# Inicializar o subplot para fitness médio
average_fitness = [np.mean(item_fitness_list)]
ax2.plot(average_fitness, label='Média de Fitness')
ax2.set_xlim(0, nFrames)
ax2.set_ylim(0, 4.2)
ax2.set_xlabel('Execuções')
ax2.set_ylabel('Média de Fitness')
ax2.set_title(f'Média de Fitness no tempo (Pc={Pc}, Pm={Pm}, N={N})')
ax2.legend()

# Incorporar o gráfico na janela tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Criar animação
ani = FuncAnimation(fig, update, frames=nFrames, interval=5, repeat=False)

# Executar o loop de eventos do tkinter
root.mainloop()
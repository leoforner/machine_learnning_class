# Autor: Leonardo Augusto de Aguiar Forner

L = 4 * 8 # size of chromossome in bits

import struct
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def floatToBits(f):
	s = struct.pack('>f', f)
	return struct.unpack('>L', s)[0]

def bitsToFloat(b):
	s = struct.pack('>L', b)
	return struct.unpack('>f', s)[0]

# Exemplo : 1.23 -> '00010111100 '
def get_bits(x):
	x = floatToBits(x)
	N = 4 * 8
	bits = ''
	for bit in range(N):
		b = x & (2**bit)
		bits += '1' if b > 0 else '0'
	return bits

# Exemplo : '00010111100 ' -> 1.23
def get_float(bits):
	x = 0
	assert(len(bits) == L)
	for i, bit in enumerate(bits):
		bit = int(bit) # 0 or 1
		x += bit * (2**i)
	return bitsToFloat(x)


def criacao(n):
    individuos = []

    for i in range(n):
        individuos.append(random.uniform(0, math.pi))
        
    return individuos

def fitness(y):
	return y + abs(math.sin(32*y))



def torneio(população):
    vencedores = []
    ganhador = 0

    for i in range(0, int(len(população)/2)):
        competidores = população[random.randint(0,len(população)-1)], população[random.randint(0, len(população)-1)]
        vencedor = competidores[0] if fitness(competidores[0]) > fitness(competidores[1]) else competidores[1]

        vencedores.append(vencedor)
    return vencedores



def crossover(população,n):    
    filhos = []
    for i in range(0, int(n/2)):
        if random.random() < Pc: 
            pai1 = get_bits(população[i])
            pai2 = get_bits(população[i+1]) if i == n/2 else get_bits(população[0])
            ponto_de_corte = random.randint(0, L/2)
            ponto_de_corte_2 = random.randint(L/2, L)
            filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:ponto_de_corte_2] + pai1[ponto_de_corte_2:]
            filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:ponto_de_corte_2] + pai2[ponto_de_corte_2:]
            if (isinstance(get_float(filho1), float) and not math.isnan(get_float(filho1)) and
                isinstance(get_float(filho2), float) and not math.isnan(get_float(filho2))):
                if get_float(filho1) > math.pi or get_float(filho2) > math.pi or get_float(filho1) < 0 or get_float(filho2) < 0:
                    filho1 = pai1
                    filho2 = pai2            
            else:
                filho1 = pai1
                filho2 = pai2

            filhos.append(get_float(filho1))
            filhos.append(get_float(filho2))
        else:
            filho1 = população[i]
            filho2 = população[i+1] if i == n/2 else população[0]
            filhos.append(filho1)
            filhos.append(filho2)

    

    return filhos

def mutação(população):

    for i in range(len(população)):
        if random.random() < Pm:
            ponto_de_mutação = random.randint(0, L-1)
            individuo = get_bits(população[i])                
            if ponto_de_mutação == 0:
                individuo =  str(int(not int(individuo[ponto_de_mutação]))) + individuo[ponto_de_mutação+1:]
            elif ponto_de_mutação == L-1:
                individuo = individuo[:ponto_de_mutação] + str(int(not int(individuo[ponto_de_mutação])))
            else:
                individuo = individuo[:ponto_de_mutação] + str(int(not int(individuo[ponto_de_mutação]))) + individuo[ponto_de_mutação+1:]
            


            while get_float(individuo) > math.pi or get_float(individuo) < 0 or not isinstance(get_float(individuo), float) or math.isnan(get_float(individuo)):
                ponto_de_mutação = random.randint(0, L-1)
                individuo = get_bits(população[i])   
                if ponto_de_mutação == 0:
                  individuo =  str(int(not int(individuo[ponto_de_mutação]))) + individuo[ponto_de_mutação+1:]
                elif ponto_de_mutação == L-1:
                    individuo = individuo[:ponto_de_mutação] + str(int(not int(individuo[ponto_de_mutação])))
                else:
                    individuo = individuo[:ponto_de_mutação] + str(int(not int(individuo[ponto_de_mutação]))) + individuo[ponto_de_mutação+1:]


            população[i] = get_float(individuo)

    return população

    
def garfico_1(população, ax):
    x = np.linspace(0, math.pi, 10000)
    y = [fitness(val) for val in x]
    fitness_values = [fitness(individual) for individual in população]
    ax.plot(x, y)
    ax.plot(população, fitness_values, 'bo')
    ax.set_xlabel('Individual')
    ax.set_ylabel('Fitness')
    ax.set_title('Population Fitness')
    ax.set_xlim(0, math.pi)
    ax.set_ylim(0, 4.5)
    ax.grid(True)  
    

def garfico_2(media, geracao, geracoes, ax):
    #print(media[-1:])
    x = geracao
    y = media
    ax.plot(x, y, 'b-')
    ax.set_xlabel('Gerações')
    ax.set_ylabel('Fitness')
    ax.set_title('Média de Fitness por Geração')
    ax.set_xlim(-1, geracoes + 5)
    ax.set_ylim(0, 4.5)
    ax.grid(True)
    




def evolução(quantidade, geracoes):
    população = criacao(quantidade)
    
    # Criação das figuras e eixos
    fig, (ax1, ax2) = plt.subplots(2, 1)
    media = []
    geracao = []

    # Ajuste do espaçamento entre os gráficos
    plt.subplots_adjust(hspace=0.5)  # Ajuste o valor conforme necessário
    
    
    def update(frame):
        nonlocal população
        ax1.clear()
        ax2.clear()
        media.append(sum([fitness(individual) for individual in população])/len(população))
        garfico_1(população, ax1)
        geracao.append(frame)
        garfico_2(media, geracao, geracoes, ax2) 
        vencedores = torneio(população)
        população = crossover(vencedores, quantidade)
        população = mutação(população)
      
    
    ani = FuncAnimation(fig, update, frames=geracoes-1, repeat=False, interval=1)
    plt.show()



'''

def evolução(quantidade, geracoes):
    população = criacao(quantidade)
    for i in range(geracoes):
        vencedores = torneio(população)
        população = crossover(vencedores, quantidade)
        população = mutação(população)
        
'''

# quanto maior maior a chance de reprodução e mutação
Pm = 0.01
Pc = 0.1

evolução(2000, 100)
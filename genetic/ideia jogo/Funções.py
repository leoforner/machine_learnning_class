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
    for i in range(len(população)):
        competidores = população[random.randint(0,len(população)-1)], população[random.randint(0, len(população)-1)]
        vencedor = competidores[0] if fitness(competidores[0]) > fitness(competidores[1]) else competidores[1]

        vencedores.append(vencedor)
    return vencedores



def crossover(população,n):
    filhos = []
    for i in range(0, n-1):
        if random.random() > Pc: 
            pai1 = get_bits(população[i])
            pai2 = get_bits(população[i+1])
            ponto_de_corte = random.randint(0, L/2)
            ponto_de_corte_2 = random.randint(L/2, L)
            filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:ponto_de_corte_2] + pai1[ponto_de_corte_2:]
            filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:ponto_de_corte_2] + pai2[ponto_de_corte_2:]
            if get_float(filho1) > math.pi or get_float(filho2) > math.pi:
                filho1 = pai1
                filho2 = pai2
            filhos.append(get_float(filho1))
            filhos.append(get_float(filho2)) 
            
        else:
            filhos.append(população[i])
            filhos.append(população[i+1])
        
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
            


            while get_float(individuo) > math.pi:
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

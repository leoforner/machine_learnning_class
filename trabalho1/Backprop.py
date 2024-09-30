import numpy as np 
import pandas as pd
import scipy.io

# Carrega o arquivo .mat
db = scipy.io.loadmat('trabalho/classification3.mat')

# Exibe o conteúdo do arquivo
print(db)


db = pd.read_mat('trabalho\classification3.mat')
'''
layers = 5
neurons = 5

# Inicializa os pesos da rede
pesos = np.random.uniform(-1, 1, (2,2))
print(pesos)
'''

print(db)
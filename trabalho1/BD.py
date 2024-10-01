import numpy as np
import matplotlib.pyplot as plt

# Carrega os dados do arquivo classification2.txt com delimitador de vírgula
data = np.loadtxt("trabalho1/classification2.txt", delimiter=',')

print(data)

# Separa as colunas em variáveis
x1 = data[:, 0]
x2 = data[:, 1]
labels = data[:, 2]

# Separa os dados em duas classes
class_1 = data[labels == 1]
class_0 = data[labels == 0]

# Plota os dados
plt.figure(figsize=(10, 6))
plt.scatter(class_1[:, 0], class_1[:, 1], color="blue", label="Classe 1")
plt.scatter(class_0[:, 0], class_0[:, 1], color="red", label="Classe 0")

# Adiciona títulos e legendas
plt.title("Gráfico de Dispersão das Classes")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()

# Mostra o gráfico
plt.show()
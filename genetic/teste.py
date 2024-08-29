import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dados para o primeiro gráfico
x1 = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x1)

# Dados para o segundo gráfico
x2 = np.linspace(0, 2*np.pi, 100)
y2 = np.cos(x2)

# Criação das figuras e eixos
fig, (ax1, ax2) = plt.subplots(2, 1)

# Função de animação para atualizar os gráficos
def animate(i):
    ax1.clear()
    ax2.clear()
    
    # Atualiza o primeiro gráfico
    ax1.plot(x1[:i], y1[:i], color='blue')
    ax1.set_title('Gráfico 1')
    ax1.set_xlim(0, 2*np.pi)  # Fixa o tamanho do eixo x
    ax1.set_ylim(-1, 1)  # Fixa o tamanho do eixo y
    
    # Atualiza o segundo gráfico
    ax2.plot(x2[:i], y2[:i], color='red')
    ax2.set_title('Gráfico 2')
    ax2.set_xlim(0, 2*np.pi)  # Fixa o tamanho do eixo x
    ax2.set_ylim(-1, 1)  # Fixa o tamanho do eixo y

# Criação da animação
ani = animation.FuncAnimation(fig, animate, frames=len(x1), interval=100)

# Exibição da animação
plt.show()
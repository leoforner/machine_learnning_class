import matplotlib.pyplot as plt
import random



class ObjetoMovivel:
    def __init__(self, x, y,nome, QM):
        self.x = x
        self.y = y
        self.nome = nome
        self.QM = QM
        self.pontos = 0

    def mover(self, dx, dy):
        self.x += self.QM*dx
        self.y += self.QM*dy

    def exibir_posicao(self):
        print(f"{self.nome} posição atual: ({self.x}, {self.y})")




# Função para atualizar o gráfico em tempo real
def update_plot(persegidor, perseguido):
    plt.plot(persegidor.x, persegidor.y, 'ro', label='Persegidor')
    plt.plot(perseguido.x, perseguido.y, 'bo', label='Perseguido')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Posição dos objetos')
    plt.grid(True)
    plt.xlim(0, 20)  # Set x-axis limits to 0 and 20
    plt.ylim(0, 20)  # Set y-axis limits to 0 and 20
    plt.pause(0.5)
    plt.clf()


# Exemplo de uso
persegidor = ObjetoMovivel(0, 0, 'caçador', 1)
persegidor.exibir_posicao()  # Saída: Posição atual: (0, 0)

# Objeto a ser perseguido
perseguido = ObjetoMovivel(10, 10, 'presa', 1)
perseguido.exibir_posicao()  # Saída: Posição atual: (5, 5)



'''
# Lógica de perseguição
while persegidor.x != perseguido.x or persegidor.y != perseguido.y:
    # Movimento da presa 
    dxp = random.randint(-4, 4)
    dyp = random.randint(-4, 4)
    if perseguido.x + dxp >= 0 and perseguido.x + dxp < 20:
        perseguido.mover(dxp, 0)
    if perseguido.y + dyp >= 0 and perseguido.y + dyp < 20:
        perseguido.mover(0, dyp)
    
    perseguido.exibir_posicao()  # Exibe a nova posição da presa



    # Define a direção do movimento
    dx = perseguido.x - persegidor.x
    dy = perseguido.y - persegidor.y
    if dx != 0:
        dx = 1 if dx > 0 else -1
    if dy != 0:
        dy = 1 if dy > 0 else -1

    # Movimenta o objeto na direção do objeto perseguido
    persegidor.mover(dx, dy)
    persegidor.exibir_posicao()  # Exibe a nova posição do objeto


    # Verifica se o objeto saiu dos limites
    if persegidor.x < 0 or persegidor.x >= 20 or persegidor.y < 0 or persegidor.y >= 20:
        print("Objeto saiu dos limites!")
        break

    if perseguido.x < 0 or perseguido.x >= 20 or perseguido.y < 0 or perseguido.y >= 20:
        print("Objeto perseguido saiu dos limites!")
        break

    update_plot(persegidor, perseguido)  # Atualiza o gráfico
'''


'''

# Exemplo de uso: caça com movimento aleatório e caçador com ia genética 

# funções genéticas
def criacao(n):
    individuos = []

    for i in range(n):
        individuos.append(ObjetoMovivel(random.randint(0, 20),random.randint(0, 20),f'caçador{i}',(random.randint(0, 10))))
        
    return individuos

def fitness(população):
    for i in range(len(população)):
        if população[i].x - presa.x < 3 and população[i].y - presa.y < 3:
            população[i].pontos += 1
'''
'''
# Objeto a ser perseguido
presa = ObjetoMovivel(10, 10, 'presa', 1)
presa.exibir_posicao()  # Saída: Posição atual: (10, 10)

def move_presa():
    dxp = random.randint(-1, 1)
    dyp = random.randint(-1, 1)
    if presa.x + dxp >= 0 and presa.x + dxp < 20:
        presa.mover(dxp, 0)
    if presa.y + dyp >= 0 and presa.y + dyp < 20:
        presa.mover(0, dyp)
    
    presa.exibir_posicao()  # Exibe a nova posição da presa

# variáveis para movimento do caçador



# IA genética do caçador

'''







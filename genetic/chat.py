import random
import math
import matplotlib.pyplot as plt

# Parâmetros do algoritmo genético
pop_size = 1000
num_generations = 100
crossover_rate = 0.1
mutation_rate = 0.01
bits = 16  # Precisão da representação binária de y

# Função a ser minimizada
def fitness_function(y):
    return y + abs(math.sin(32*y))

# Codifica um valor real para uma representação binária
def encode(real_value):
    binary_str = bin(int(real_value * (2**bits - 1)))[2:].zfill(bits)
    return binary_str

# Decodifica uma representação binária para um valor real
def decode(binary_str):
    real_value = int(binary_str, 2) / (2**bits - 1) * math.pi
    return real_value

# Inicializa a população aleatoriamente
def initialize_population():
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice('01') for _ in range(bits))
        population.append(individual)
    return population

# Seleção por torneio
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    best = max(tournament, key=lambda x: fitness_function(decode(x)))
    return best

# Crossover de dois pontos
def crossover(parent1, parent2):
    crossover_point1 = random.randint(0, bits-2)
    crossover_point2 = random.randint(crossover_point1+1, bits-1)
    child = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    return child

# Mutação de um bit
def mutate(individual):
    mutation_point = random.randint(0, bits-1)
    new_individual = list(individual)
    new_individual[mutation_point] = '1' if new_individual[mutation_point] == '0' else '0'
    return ''.join(new_individual)

# Algoritmo genético principal
def genetic_algorithm():
    population = initialize_population()
    best_fitness_values = []

    for generation in range(num_generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population, 5)
            parent2 = tournament_selection(population, 5)

            if random.random() < crossover_rate:
                child = crossover(parent1, parent2)
            else:
                child = parent1

            if random.random() < mutation_rate:
                child = mutate(child)

            new_population.append(child)

        population = new_population

        # Encontrar o melhor indivíduo da geração
        best_individual = min(population, key=lambda x: fitness_function(decode(x)))
        best_fitness = fitness_function(decode(best_individual))
        best_fitness_values.append(best_fitness)

    return best_individual, best_fitness_values

# Executar o algoritmo e plotar os resultados
best_individual, best_fitness_values = genetic_algorithm()
best_y = decode(best_individual)
print("Melhor valor de y:", best_y)
print("Mínimo da função:", fitness_function(best_y))

plt.plot(best_fitness_values)
plt.xlabel("Geração")
plt.ylabel("Valor de fitness")
plt.title("Evolução do melhor fitness")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("Leonardo Augusto de Aguiar Forner")

def f_true(x):
    return 2 + 0.8 * x


# conjunto de dados {(x,y)}
xs = np.linspace(-3, 3, 100)
ys = np.array([f_true(x) + np.random.randn() * 0.5 for x in xs])


""" hipotese """


def h(x, theta):
    y = theta[0] + theta[1] * x
    return y


""" funcao de custo """


def J(reta, xs, ys):
    m = len(xs)
    y = reta
    j = (1 / (2 * m)) * sum([(y[i] - ys[i]) ** 2 for i in range(m)])
    return j


""" derivada parcial com respeito a theta [i] """


def gradient(i, theta, xs, ys, a):
    m = len(xs)
    theta[i] = (
        (
            theta[i]- a * (1 / m) * sum([(h(xs[j], theta) - ys[j]) for j in range(m)])
        )
        if i == 0
        else (
            theta[i] - a * (1 / m) * sum([(h(xs[j], theta) - ys[j]) * xs[j] for j in range(m)])
        )
    )


""" plota no mesmo grafico: 
- o modelo / hipotese (reta)
- a reta original (true function)
- e os dados com ruido (xs, ys) """


def animate_modelo(theta, xs, ys, a):
    fig, ax = plt.subplots()
    (line,) = ax.plot(xs, [h(x, theta) for x in xs], label="Modelo")
    scatter = ax.scatter(xs, ys)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-3, 6)
    ax.set_title("Scatter plot of xs and ys")

    def update(frame):

        ax.plot(xs, [f_true(x) for x in xs])

        nonlocal theta
        reta = [h(x, theta) for x in xs]
        j = J(reta, xs, ys)
        
        gradient(0, theta, xs, ys, a)
        gradient(1, theta, xs, ys, a)

        line.set_ydata(reta)
        ax.set_title(f"Custo: {j:.2f}")

        if frame % 10 == 0:
            print(f"frame = {frame}")
            print(f"J = {j}")
            print(f"theta = {theta}")

        return line, scatter

    ani = animation.FuncAnimation(fig, update, frames=50, interval=100, blit=True, repeat=False)
    plt.show()


animate_modelo([2, 5], xs, ys, 0.1)
import matplotlib.pyplot as plt

def plot_cost_over_epochs(theta, xs, ys, learning_rate, num_epochs):
    costs = []
    for epoch in range(num_epochs):
        reta = [h(x, theta) for x in xs]
        j = J(reta, xs, ys)
        costs.append(j)

        gradient(0, theta, xs, ys, learning_rate)
        gradient(1, theta, xs, ys, learning_rate)

    return costs

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

costs_1 = plot_cost_over_epochs([4, 10], xs, ys, 0.9, 5000)
axs[0].plot(range(5000), costs_1)
axs[0].set_xlabel("Epoch")
axs[0].set_ylabel("Cost")
axs[0].set_title("Learning Rate: 0.9")

costs_2 = plot_cost_over_epochs([4, 10], xs, ys, 0.1, 5000)
axs[1].plot(range(5000), costs_2)
axs[1].set_xlabel("Epoch")
axs[1].set_ylabel("Cost")
axs[1].set_title("Learning Rate: 0.1")

costs_3 = plot_cost_over_epochs([4, 10], xs, ys, 0.0001, 5000)
axs[2].plot(range(5000), costs_3)
axs[2].set_xlabel("Epoch")
axs[2].set_ylabel("Cost")
axs[2].set_title("Learning Rate: 0.0001")

plt.tight_layout()
plt.show()


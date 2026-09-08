import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Données
x_raw = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
N = len(y)
X = np.c_[x_raw, np.ones(N)]
x_dense = np.linspace(0, 7, 200)
X_dense = np.c_[x_dense, np.ones(len(x_dense))]


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def train_model(lr, epochs):
    weights = np.zeros(2)
    for _ in range(int(epochs)):
        z = X @ weights
        y_hat = sigmoid(z)
        gradient = X.T @ (y_hat - y)  #[cite: 1, 4, 6]
        weights -= lr * (gradient / N)
    return weights


# Création de la figure
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(bottom=0.25)  # Espace pour les curseurs

# Éléments graphiques initiaux
w_init = train_model(0.5, 1000)
ax.scatter(x_raw, y, color="royalblue", label="Données réelles")
(line,) = ax.plot(
    x_dense,
    sigmoid(X_dense @ w_init),
    color="crimson",
    label=r"Modèle $\hat{y}$",
)
ax.axhline(0.5, color="gray", linestyle="--", alpha=0.7)
ax.set_ylim(-0.05, 1.05)
ax.set_xlim(0, 7)
ax.set_xlabel("Heures de révision")
ax.set_ylabel("Probabilité")
ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.4)

# Définition des zones de curseurs
ax_lr = plt.axes([0.2, 0.12, 0.65, 0.03])
ax_epochs = plt.axes([0.2, 0.05, 0.65, 0.03])

slider_lr = Slider(ax_lr, "Learning Rate", 0.05, 2.0, valinit=0.5, valstep=0.05)
slider_epochs = Slider(
    ax_epochs, "Epochs", 50, 3000, valinit=1000, valstep=50
)


# Mise à jour dynamique
def update(val):
    lr = slider_lr.val
    epochs = slider_epochs.val
    w = train_model(lr, epochs)
    line.set_ydata(sigmoid(X_dense @ w))
    fig.canvas.draw_idle()


slider_lr.on_changed(update)
slider_epochs.on_changed(update)

plt.show()
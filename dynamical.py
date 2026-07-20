import numpy as np
import matplotlib.pyplot as plt

# Grid for the vector field
x = np.linspace(-1.5, 1.5, 30)
y = np.linspace(-1.2, 1.2, 25)
X, Y = np.meshgrid(x, y)

# Two-dimensional dynamical system
U = X - X**3
V = -Y

# Draw the flow
plt.figure(figsize=(8, 5))
plt.streamplot(X, Y, U, V, density=1.2)

# Three equilibrium points
plt.scatter([-1, 1], [0, 0], s=120, marker="o", edgecolors="black")
plt.scatter([0], [0], s=120, marker="s", edgecolors="black")

# Labels
plt.text(-1, 0.15, "M-: stable", ha="center")
plt.text(0, 0.15, "M0: saddle", ha="center")
plt.text(1, 0.15, "M+: stable", ha="center")

# Stable manifold of the saddle
plt.axvline(0, linestyle="--", label="stable manifold")

plt.title("Two-Dimensional Morse Decomposition")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.2, 1.2)
plt.grid(alpha=0.2)
plt.legend()
plt.tight_layout()
plt.savefig("morse_decomposition_2d.png", dpi=200)
plt.show()

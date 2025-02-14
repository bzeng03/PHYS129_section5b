import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100  # Number of bosons
epsilon = 1.0  # Energy of the excited state (in arbitrary units)
kB = 1.0  # Boltzmann constant (in arbitrary units)
T = np.linspace(0.1, 5, 100)  # Temperature range

# Compute average occupation numbers
beta = 1 / (kB * T)
n1_avg = N * np.exp(-beta * epsilon) / (1 + np.exp(-beta * epsilon))
n0_avg = N - n1_avg

# Plot
plt.figure(figsize=(8, 5))
plt.plot(T, n0_avg, label=r'$\langle n_0 \rangle_C$ (Ground State)', linewidth=2)
plt.plot(T, n1_avg, label=r'$\langle n_\epsilon \rangle_C$ (Excited State)', linewidth=2)
plt.xlabel("Temperature (T)")
plt.ylabel("Average Occupation Number")
plt.title("Occupation Numbers vs Temperature (Classical Case)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("plot_c.png")
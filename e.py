import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100  # Number of bosons
epsilon = 1.0  # Energy of the excited state (in arbitrary units)
kB = 1.0  # Boltzmann constant (in arbitrary units)
T = np.linspace(0.1, 5, 100)  # Temperature range

# Compute beta
beta = 1 / (kB * T)

# Compute quantum partition function
Z = (1 - np.exp(-beta * (N+1) * epsilon)) / (1 - np.exp(-beta * epsilon))

# Compute average occupation numbers in quantum case
n1_avg_q = (np.exp(-beta * epsilon) * (1 - np.exp(-beta * N * epsilon))) / (1 - np.exp(-beta * (N+1) * epsilon)) * N
n0_avg_q = N - n1_avg_q

# Plot
plt.figure(figsize=(8, 5))
plt.plot(T, n0_avg_q, label=r'$\langle n_0 \rangle$ (Ground State)', linewidth=2)
plt.plot(T, n1_avg_q, label=r'$\langle n_\epsilon \rangle$ (Excited State)', linewidth=2)
plt.xlabel("Temperature (T)")
plt.ylabel("Average Occupation Number")
plt.title("Occupation Numbers vs Temperature (Quantum Case)")
plt.legend()
plt.grid()
plt.show()
plt.savefig("plot_e.png")
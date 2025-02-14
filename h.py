import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Constants
epsilon = 1.0  # Energy unit
kB = 1.0  # Boltzmann constant
T = np.linspace(0.5, 5, 100)  # Temperature range
beta = 1 / (kB * T)  # Inverse temperature

# Define function to solve for chemical potential μ using the given equation for <N>
def avg_N(mu, beta):
    return (np.exp(beta * (epsilon - mu)) * (1 + np.exp(beta * epsilon) - 2 * np.exp(beta * mu))) / \
           ((np.exp(beta * (mu - epsilon)) - 1)**2 * (np.exp(beta * mu) - 1)**2)

# Target particle number
N_target = 100000

# Define a safer range for μ
mu_min = -5  # More negative starting value for μ
mu_max = -0.01  # Avoiding division errors near zero

# Solve for μ numerically for each temperature
mu_values = np.zeros_like(T)

for i in range(len(T)):
    func = lambda mu: avg_N(mu, beta[i]) - N_target  # Solve for μ such that <N> = N_target
    try:
        mu_values[i] = opt.brentq(func, mu_min, mu_max)  # Finding root in reasonable range
    except ValueError:
        mu_values[i] = np.nan  # Assign NaN if root finding fails

# Compute <n_0> using the second formula
n0_values = 1 / (np.exp(-beta * mu_values) - 1)

# Plot Ground State Occupation vs Temperature
plt.figure(figsize=(8, 5))
plt.plot(T, n0_values, label=r'$\langle n_0 \rangle$ (Ground State)', linewidth=2)
plt.xlabel("Temperature (T)")
plt.ylabel(r"Average Ground State Occupation $\langle n_0 \rangle$")
plt.title("Ground State Occupation vs Temperature")
plt.legend()
plt.grid()
plt.show()
plt.savefig("plot_h.png")
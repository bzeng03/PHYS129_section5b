import numpy as np
import matplotlib.pyplot as plt
from ij import analyze_bose_system  # Importing from ij.py

# Constants
N = 100000  # Total number of bosons (~10^5)
T_min, T_max = 0.1, 100000  # Extended temperature range
T_range = np.linspace(T_min, T_max, 200)  # More points for smoother curves

# Define near-degenerate energy levels
num_levels = 100
energy_spacing = 0.1
energy_levels = np.arange(num_levels) * energy_spacing

# Run the Bose system analysis
temps, mus, n0s, dn0_dTs = analyze_bose_system(N, T_range, energy_levels)

# Compute Specific Heat Cv = -d⟨n₀⟩/dT * T
Cv_values = -dn0_dTs * temps

# Plot settings
plt.style.use("seaborn-darkgrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 16))
axes = axes.flatten()  # Flatten to easily index subplots

# 1. Chemical potential plot
axes[0].plot(temps, -mus, color="b", linewidth=2)
axes[0].set_xlabel(r'Temperature $T$', fontsize=12)
axes[0].set_ylabel(r'Negative Chemical Potential $-\mu$', fontsize=12)
axes[0].set_title("Negative Chemical Potential vs Temperature", fontsize=14)
axes[0].grid(True)

# 2. Ground state occupation plot
axes[1].plot(temps, n0s, color="r", linewidth=2)
axes[1].set_xlabel(r'Temperature $T$', fontsize=12)
axes[1].set_ylabel(r'Ground State Occupation $\langle n_0 \rangle$', fontsize=12)
axes[1].set_title("Ground State Occupation vs Temperature", fontsize=14)
axes[1].grid(True)

# 3. Log-scale ground state occupation plot
axes[2].plot(temps, np.log(n0s), color="g", linewidth=2)
axes[2].set_xlabel(r'Temperature $T$', fontsize=12)
axes[2].set_ylabel(r'$\log(\langle n_0 \rangle)$', fontsize=12)
axes[2].set_title("Log of Ground State Occupation vs Temperature", fontsize=14)
axes[2].grid(True)

# 4. Occupation gradient plot
axes[3].plot(temps, -dn0_dTs, color="m", linewidth=2)
axes[3].set_xlabel(r'Temperature $T$', fontsize=12)
axes[3].set_ylabel(r'$-\partial \langle n_0 \rangle / \partial T$', fontsize=12)
axes[3].set_title("Negative Gradient of Ground State Occupation", fontsize=14)
axes[3].grid(True)

# 5. Specific Heat plot
axes[4].plot(temps, Cv_values, color="c", linewidth=2)
axes[4].set_xlabel(r'Temperature $T$', fontsize=12)
axes[4].set_ylabel(r'Specific Heat $C_V$', fontsize=12)
axes[4].set_title("Specific Heat vs Temperature", fontsize=14)
axes[4].grid(True)

# Remove empty subplot (3x2 layout has an extra slot)
fig.delaxes(axes[5])

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("plot_bose_system.png", dpi=300, bbox_inches="tight")
plt.show()
plt.savefig("plot_k.png")
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def occupation_sum(mu, beta, energy_levels):
    """Calculate sum of occupation numbers for given mu and beta"""
    return np.sum(1 / (np.exp(beta * (energy_levels - mu)) - 1))

def find_mu(N, beta, energy_levels):
    """Find chemical potential mu for given N and beta"""
    # Define function to find root of
    def func(mu):
        return occupation_sum(mu, beta, energy_levels) - N
    
    # Find root in range (-inf, min(energy_levels))
    # Start with reasonable bounds
    max_mu = np.min(energy_levels) - 1e-10
    min_mu = max_mu - 100  # Start with large negative value
    
    try:
        result = root_scalar(func, bracket=[min_mu, max_mu])
        return result.root
    except ValueError:
        # If bracketing fails, try with lower minimum
        min_mu = max_mu - 1000
        result = root_scalar(func, bracket=[min_mu, max_mu])
        return result.root

def dmu_dbeta(mu, beta, N, energy_levels):
    """Calculate dμ/dβ using implicit differentiation"""
    numerator = np.sum(
        (energy_levels - mu) / (np.exp(beta * (energy_levels - mu)) - 1)**2 
        * np.exp(beta * (energy_levels - mu))
    )
    denominator = np.sum(
        1 / (np.exp(beta * (energy_levels - mu)) - 1)**2 
        * np.exp(beta * (energy_levels - mu))
    )
    return -numerator/denominator

def ground_state_occupation(mu, beta, ground_energy):
    """Calculate ground state occupation number"""
    return 1 / (np.exp(beta * (ground_energy - mu)) - 1)

def dn0_dbeta(mu, beta, ground_energy, dmu_dbeta):
    """Calculate d⟨n₀⟩/dβ"""
    n0 = ground_state_occupation(mu, beta, ground_energy)
    return -n0**2 * np.exp(beta * (ground_energy - mu)) * (
        ground_energy - mu - dmu_dbeta
    )

def analyze_bose_system(N, T_range, energy_levels):
    """Analyze Bose system for range of temperatures"""
    kB = 1  # Boltzmann constant in natural units
    
    # Initialize arrays to store results
    temps = np.array(T_range)
    betas = 1 / (kB * temps)
    mus = np.zeros_like(betas)
    n0s = np.zeros_like(betas)
    dn0_dTs = np.zeros_like(betas)
    
    # Calculate quantities for each temperature
    for i, beta in enumerate(betas):
        # Find chemical potential
        mu = find_mu(N, beta, energy_levels)
        mus[i] = mu
        
        # Calculate ground state occupation
        n0s[i] = ground_state_occupation(mu, beta, energy_levels[0])
        
        # Calculate dμ/dβ
        dmu_db = dmu_dbeta(mu, beta, N, energy_levels)
        
        # Calculate d⟨n₀⟩/dT = -β²d⟨n₀⟩/dβ
        dn0_db = dn0_dbeta(mu, beta, energy_levels[0], dmu_db)
        dn0_dTs[i] = -beta**2 * dn0_db
    
    return temps, mus, n0s, dn0_dTs

# Example usage
N = 1e5  # Total number of particles
T_min, T_max = 0.1, 100000  # Extended temperature range
T_range = np.linspace(T_min, T_max, 200)  # More points for smoother curves

# Create near-degenerate energy levels
num_levels = 100
energy_spacing = 0.1
energy_levels = np.arange(num_levels) * energy_spacing

# Run analysis
temps, mus, n0s, dn0_dTs = analyze_bose_system(N, T_range, energy_levels)

# Plot results
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax5_dummy)) = plt.subplots(3, 2, figsize=(12, 15))
ax5_dummy.remove()  # Remove the extra subplot

# Plot 1: Chemical potential
ax1.plot(temps, -mus)
ax1.set_xlabel(r'$T$')
ax1.set_ylabel(r'$-\mu$')
ax1.grid(True)

# Plot 2: Ground state occupation
ax2.plot(temps, n0s)
ax2.set_xlabel(r'$T$')
ax2.set_ylabel(r'$\langle n_0 \rangle$')
ax2.grid(True)

# Plot 3: Log of ground state occupation
ax3.plot(temps, np.log(n0s))
ax3.set_xlabel(r'$T$')
ax3.set_ylabel(r'$\log(\langle n_0 \rangle)$')
ax3.grid(True)

# Plot 4: Occupation gradient
ax4.plot(temps, -dn0_dTs)
ax4.set_xlabel(r'$T$')
ax4.set_ylabel(r'$-\partial \langle n_0 \rangle/\partial T$')
ax4.grid(True)

# Plot 5: Specific heat
ax5.plot(temps, -dn0_dTs * temps)
ax5.set_xlabel(r'$T$')
ax5.set_ylabel(r'$C_v$')
ax5.grid(True)

plt.tight_layout()
plt.show()
plt.savefig("j.png")
# Task 1: Fermi-Dirac Statistics

## **Grand Partition Function for Fermions**

Fermions are particles with half-integer spin (e.g., electrons, protons, neutrons) and obey the Pauli exclusion principle, which states that no two identical fermions can occupy the same quantum state simultaneously.

### **1. Grand Partition Function Definition**
The grand partition function \(\mathcal{Z}_G\) is given by:

\[
\mathcal{Z}_G = \sum_{\{n_i\}} e^{-\beta (E - \mu N)}
\]

where:
- \( \beta = \frac{1}{k_B T} \) (inverse temperature),
- \( \mu \) is the chemical potential,
- \( N \) is the total number of particles,
- \( E \) is the total energy.

Since we are dealing with **fermions**, each quantum state can have either **0 or 1 particle** due to the **Pauli exclusion principle**.

### **2. Energy Levels in a 2-Level System**
Given the system has **energy levels** \( \epsilon, 2\epsilon, 3\epsilon, \dots, M\epsilon \), the occupation number \( n_i \) at each level can be **either 0 or 1**.

Thus, for each level \( i \), the grand partition function contribution is:

\[
Z_i = \sum_{n_i = 0,1} e^{-\beta (\epsilon_i - \mu)n_i} = 1 + e^{-\beta (\epsilon_i - \mu)}
\]

### **3. Total Partition Function**
Since all energy levels are independent, the **total grand partition function** is the product over all levels:

\[
\mathcal{Z}_G = \prod_{i=1}^{M} \left(1 + e^{-\beta (\epsilon_i - \mu)} \right)
\]

where \( M \) is the number of available energy levels.

### **4. Fermi-Dirac Distribution**
The probability of occupation of an individual level is given by the **Fermi-Dirac distribution**:

\[
\langle n_i \rangle = \frac{1}{e^{\beta (\epsilon_i - \mu)} + 1}
\]

This describes the statistical behavior of fermions in thermal equilibrium under the grand canonical ensemble.

### **Conclusion**
We have derived the grand partition function for a system of fermions obeying the Pauli exclusion principle and shown how it leads to the Fermi-Dirac distribution.

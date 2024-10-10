import numpy as np
import matplotlib.pyplot as plt

def initialize_lattice(N):
    """Initialize a NxN lattice with random spins."""
    lattice = np.random.choice([-1, 1], size=(N, N))
    return lattice

def calculate_energy(lattice):
    """Calculate the total energy of the lattice."""
    energy = 0
    N = lattice.shape[0]
    for i in range(N):
        for j in range(N):
            S = lattice[i, j]
            neighbors = lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + lattice[(i-1)%N, j] + lattice[i, (j-1)%N]
            energy += -neighbors * S
    return energy / 2  # Each pair counted twice

def monte_carlo_step(lattice, beta):
    """Perform one Monte Carlo step using the Metropolis algorithm."""
    N = lattice.shape[0]
    for _ in range(N*N):
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
        S = lattice[i, j]
        neighbors = lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + lattice[(i-1)%N, j] + lattice[i, (j-1)%N]
        delta_E = 2 * S * neighbors
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E * beta):
            lattice[i, j] = -S
    return lattice

def simulate_ising(N, T, steps):
    """Simulate the Ising model."""
    lattice = initialize_lattice(N)
    beta = 1.0 / T
    energies = []
    for step in range(steps):
        lattice = monte_carlo_step(lattice, beta)
        if step % 100 == 0:
            energies.append(calculate_energy(lattice))
    return lattice, energies

# Parameters
N = 20  # Lattice size
T = 2.0  # Temperature
steps = 10000  # Number of Monte Carlo steps

# Simulation
final_lattice, energies = simulate_ising(N, T, steps)

# Plotting
plt.imshow(final_lattice, cmap='coolwarm')
plt.title('Final Lattice Configuration')
plt.colorbar(label='Spin')
plt.show()

plt.plot(energies)
plt.title('Energy vs. Monte Carlo Steps')
plt.xlabel('Monte Carlo Steps (x100)')
plt.ylabel('Energy')
plt.show()

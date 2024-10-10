import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

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
    red_energies = []
    sq_red_energies = []
    for step in range(steps):
        lattice = monte_carlo_step(lattice, beta)
        if step % 100 == 0:
            #energies.append(calculate_energy(lattice))
            aux1 = calculate_energy(lattice)
            energies.append(aux1)
            if step >= 2000:
               red_energies.append(aux1)
               sq_red_energies.append(aux1*aux1)
    return lattice, energies, red_energies, sq_red_energies

# Parameters
N = 20  # Lattice size
steps = 20000  # Number of Monte Carlo steps

# Temperature LOOP
#T = 2.10  # Initial Temperature
TT= [1.40,1.60,1.80,2.00,2.190,2.195,2.200,2.205,2.210,2.215,2.220,2.225,2.230,2.235,2.240,2.245,2.250,2.255,2.260,2.265,2.270,2.275,2.280,2.40,2.50,2.60,2.70,2.80,3.00,4.00,5.00]

for T in TT:

# Simulation
 final_lattice, energies, red_energies, sq_red_energies = simulate_ising(N, T, steps)



 average_energy = stat.mean(red_energies)
 std_dev = stat.stdev(red_energies)

 sqr_average_energy = stat.mean(sq_red_energies)
 #sq_red_energies_stdev = stat.stdev(sq_red_energies)

 print (T,average_energy,std_dev,sqr_average_energy)
from numba import jit, typed
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
# from statsmodels.graphics import tsaplots

@jit(nopython=True)
def vizinhos(S: np.ndarray) -> np.ndarray:
    """
    Utilizaremos o índice 0 para o vizinho à direita, o 1 para o vizinho acima, o 2 para o vizinho à esquerda 
    e o 3 para o vizinho abaixo
    """
    N = S.size
    L = np.sqrt(N)
    
    dimension = (N, 4)
    viz_list = np.zeros(dimension, dtype=np.int16)
    
    for i in range(N):
        
        viz_list[i,0] = i+1
        if (i+1)%L == 0 : 
            viz_list[i,0] = i+1-L
        
        viz_list[i,1] = i+L
        if i > (N-L-1): 
            viz_list[i,1] = i + L -N 

        viz_list[i,2] = i-1
        if i % L == 0: 
            viz_list[i,2] = i-1 + L 

        viz_list[i,3] = i-L
        if i<L: 
            viz_list[i,3] = i-L+N
    return viz_list

# EnergiaType = Callable[[np.ndarray, np.ndarray],float]
@jit(nopython=True)
def get_energia(S: np.ndarray, viz: np.ndarray) -> float:
    energia = 0
    # Hamiltoniano
    for i in range(S.size):
        energia = energia - S[i]*S[viz[i,0]] - S[i]*S[viz[i,1]]
    return energia

@jit(nopython=True)
def monte_carlo_step(S: np.ndarray, viz: np.ndarray, ex: typed.Dict, ener: float, mag: int | float):
    for i in range(S.size):
        # Random site index    
        k = np.random.randint(S.size)

        h = S[viz[k,0]] + S[viz[k,1]] + S[viz[k,2]] + S[viz[k,3]]
        delta_E = 2*S[k]*h

        if np.random.rand() < ex[delta_E]:
            S[k] = -S[k]
            ener = ener + delta_E
            mag = np.sum(S)
    return S, ener, mag

def create_exp_dict(beta):
    ex = typed.Dict()
    ex[-8] = np.exp(8.0 * beta)
    ex[-4] = np.exp(4.0 * beta)
    ex[0] = 1.0
    ex[4] = np.exp(-4.0 * beta)
    ex[8] = np.exp(-8.0 * beta)
    return ex

if __name__ == "__main__":
    T: float = 1.5
    beta: float = 1 / T
    L: int = 32
    ex = create_exp_dict(beta)
    # ex: dict = {-8 : np.exp(8.0*beta),
    #             -4 : np.exp(4.0*beta),
    #             0 : 1,
    #             4 : np.exp(-4.0*beta),
    #             8 : np.exp(-8.0*beta) }   
    

    ENERGY_CONTAINER: list[list] = []
    MAG_CONTAINER: list[list] = []

    NUM_CONFIGURACOES_INICIAIS = 20
    MONTE_CARLO_STEPS: int = 1100
    
    for n in range(NUM_CONFIGURACOES_INICIAIS):
        # condicao inicial aleatoria
        spin_matrix = np.random.choice([-1, 1], size=(L*L))
        viz_list = vizinhos(S=spin_matrix)

        energy_list = []
        mag_list = []

        ener = get_energia(S=spin_matrix, viz=viz_list)
        mag = np.sum(spin_matrix)

        # De cada configuracao
        energy_list.append(ener)
        mag_list.append(mag)

        
        for _ in range(MONTE_CARLO_STEPS):
            spin_matrix, E_step, M_step = monte_carlo_step(S=spin_matrix, viz=viz_list, ex=ex, ener=ener, mag=mag)
            energy_list.append(E_step)
            mag_list.append(M_step)
        ENERGY_CONTAINER.append(energy_list)
        MAG_CONTAINER.append(mag_list)

    
    
    # Plots de energia
    for i in range(len(ENERGY_CONTAINER)):
        plt.plot(ENERGY_CONTAINER[i])
        plt.suptitle("Termalização")
        plt.title(f"Tamanho da rede L={L} | Temperaratura = {T}")
        plt.xlabel("Passos de Monte Carlo")
        plt.ylabel("Energia")
    # plt.savefig(f"Energy_L{L}_Temp{T}.png")
    plt.show()
    
    
    # # Plots de Magnetização
    for i in range(len(MAG_CONTAINER)):
        plt.plot(MAG_CONTAINER[i])
        plt.suptitle("Termalização")
        plt.title(f"Tamanho da rede L={L} | Temperaratura = {T}")
        plt.xlabel("Passos de Monte Carlo")
        plt.ylabel("Energia")
    # plt.savefig(f"Mag_L{L}_Temp{T}.png")
    plt.show()
     

    


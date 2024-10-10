import numpy as np
import matplotlib.pyplot as plt
from numba import jit, typed
from typing import Callable


class SpinLattice:
    def __init__(self, L, T, spins):
        self.L = L # lado da rede
        self.N = self.L * self.L # num de spins
        self.T = T # temperatura 
        self.spins = spins # matriz de spins
        self.beta = 1 / self.T
    
    def get_viz(self) -> np.ndarray:
        #self.N = self.L * self.L
        dimension = (self.N, 4)
        self.viz_list = np.zeros(dimension, dtype=np.int16)
        
        for i in range(self.N):
            
            self.viz_list[i,0] = i+1
            if (i+1) % self.L == 0 : 
                self.viz_list[i,0] = i+1-self.L
            
            self.viz_list[i,1] = i+self.L
            if i > (self.N-self.L-1): 
                self.viz_list[i,1] = i + self.L -self.N 
    
            self.viz_list[i,2] = i-1
            if i % self.L == 0: 
                self.viz_list[i,2] = i-1 + self.L 
    
            self.viz_list[i,3] = i-self.L
            if i<self.L: 
                self.viz_list[i,3] = i-self.L+self.N
        return self.viz_list

def random_config(N):
    # atribuir spins a spin_matrix da Classe
    spins = np.random.choice([-1,1] , N)
    return spins

def get_ener_mag(spins, viz):
    N = spins.size
    ener = 0
    for i in range(N):
        h = spins[viz[i,0]] + spins[viz[i, 1]]
        ener -= spins[i]*h
        mag = np.sum(spins)
    return ener, mag

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

# def make_subplots(energy_vecs: list[list], mag_vecs:list[list]):
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
    
#     for i in range(len(energy_vecs)):
#         ax1.plot(energy_vecs[i])
#     ax1.set_ylabel("Energia")
#     ax1.set_xlabel("Passos de MC")


#     for j in range(len(mag_vecs)):
#         ax2.plot(mag_vecs[j])
#     ax2.set_xlabel("Passos de MC")
#     ax2.set_ylabel("Magnetização")
#     plt.tight_layout()
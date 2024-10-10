# Anotações sobre Algoritmo Genético
**Exemplo de Parâmetros do algoritmo genético:**  
```python 
POPULATION_SIZE = 100  # 100 soluções
GENOME_LENGTH = 20 # O tamanho de cada uma das soluções
MUTATION_RATE = 0.01 # flipar um index ou fazer uma operação
CROSSOVER_RATE = 0.7 
# quão provável de fazer um crossover ao invés de retornar os pais p1 p2 sem nenhuma interação entre eles

GENERATIONS = 200 # Todo o processo será repetido 200x 

```

Crossover aqui é o método de reprodução entre pais (parents) para geração de filhos (offsprings), por exemplo:

```python  

def crossover(parent1, parent2):
    # Combine
    if random.random() > MUTATION_RATE:
        crossover_point = random.randint(1, len(parent1) - 1)
        return parent1[:crossover_point] + parent2[crossover_point:], parent1[crossover_point:] + parent2[:crossover_point]
    # Does nothing
    else:
        return parent1, parent2
```  
 

# Tipos de CrossOver  

1 -  Order Operator (OX)
 **Biblioteca: pyevolve**  
```python
 Crossovers.G1DListCrossoverOX(genome, **args)

```

2 - Partially-Mapped Operator (PMX)  
```python
#
```
3 - Cycle Crossover
```python
#
```
 
# Tipos de **Mutação**
1 - **Reciprocal Exchange** 
```python
#
```  
2 - **Inversion**
```python
#
```  






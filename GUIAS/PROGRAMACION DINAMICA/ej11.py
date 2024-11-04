"""
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;

(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de 
operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. 
Indicar y justificar la complejidad del algoritmo implementado. 
Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.
"""

# OPT(i) = min(OPT(i-1), OPT(i/2)) + 1

def operaciones(K):
    memo = [0] * (K+1)
    memo[1] = 1
    for i in range(2, K+1):
        if i % 2 == 0:
            memo[i] = min(memo[i-1], memo[i//2]) + 1
        else:
            memo[i] = memo[i-1] + 1
    return memo

def reconstruir_operaciones(K):
    memo = operaciones(K)
    sol = []
    i = K
    while i > 0:
        if i % 2 == 0 and memo[i] == memo[i//2] + 1:
            sol.append(f'Duplicar {i//2}')
            i = i // 2
        else:
            sol.append(f'Aumentar {i-1}')
            i -= 1
    return sol

# Complejidad: O(K) donde K es el número al que se quiere llegar.
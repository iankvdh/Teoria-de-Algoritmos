"""
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, 
encontrar, utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera 
hasta el paso n. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos: n = 0 
–> Debe devolver 1 (no moverse) n = 1 –> Debe devolver 1 (paso de 1) n = 2 –> Debe devolver 2 
(dos pasos de 1, o un paso de 2) n = 3 –> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un 
paso de 2 y uno de 1, o un paso de 1 y un paso de 2) n = 4 –> Debe devolver 7 n = 5 –> Debe devolver 13
"""

# sin memo
def escalera(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return escalera(n-1) + escalera(n-2) + escalera(n-3)

# con memo bottom up
def escalera_memo(n):
    memo = []
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    for i in range(4, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]

# Complejidad: O(n) donde n es la cantidad de escalones que tiene la escalera.
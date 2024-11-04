"""
Un bodegón tiene una única mesa larga con W lugares. 
Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, 
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, 
se los anota en un vector P donde P[i] contiene la cantidad de personas que integran 
el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las 
personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos 
que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la 
menor cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.
"""

"""
OPT(i, j) = max(OPT(i-1, j), OPT(i-1, j-P[i-1]) + P[i-1]) si P[i-1] <= j
            OPT(i-1, j) si P[i-1] > j
"""

def max_espacios(P, W):
    n = len(P)
    memo = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if P[i-1] <= j:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-P[i-1]] + P[i-1])
            else:
                memo[i][j] = memo[i-1][j]
    return memo

def reconstruccion_max_espacios(M, P, W):
    n = len(P)
    i = n
    j = W
    grupos = []
    while i > 0 and j > 0:
        if M[i][j] != M[i-1][j]:
            grupos.append(P[i-1])
            j -= P[i-1]
        i -= 1
    grupos.reverse()
    return grupos

"""
Complejidad: O(n*W)
Pseudo-polinomial, ya que la complejidad depende de la capacidad de la mesa.
W se puede considerar como un número entero, por lo que la complejidad es polinomial.

En bits, W se puede representar con log(W) bits. Por ende, W = 2^m, siendo m la cantidad
de bits que se utilizan para representar su valor entero. Por lo tanto, desde este punto
de vista, la complejidad es O(n*2^m), que es exponencial.

Generamos columnas con cada una de las permutaciones posibles de los grupos, y en cada una
de ellas calculamos la cantidad máxima de personas que pueden sentarse en la mesa.
"""

P = [1, 2, 3, 4, 5]
W = 10
memo = max_espacios(P, W)
print(f'Respuesta: {memo[-1][-1]}') # 10
print(f'Grupos tomados: {reconstruccion_max_espacios(memo, P, W)}') # [1, 2, 3, 4]
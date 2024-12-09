"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, 
y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos 
sin exceder la capacidad. Implementar un algoritmo que, por programación dinámica, reciba 
los valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para 
maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado.
Luego, reconstruir con la matriz obtenida qué elementos se deben guardar.
"""

"""
Ecuacion de recurrencia:

OPT(n, W) = max ->  OPT(n-1, W)
                ->  OPT(n-1, W - Pi) + Vi
"""
# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    valores = [e[0] for e in elementos]
    pesos = [e[1] for e in elementos]
    dp = mi_mochila(W, valores, pesos)
    return elementos_mochila(W, valores, pesos, dp)

def mi_mochila(W, valores, pesos):
    n = len(valores)
    memo = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if pesos[i-1] <= j:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-pesos[i-1]] + valores[i-1])
            else:
                memo[i][j] = memo[i-1][j]
    return memo

def elementos_mochila(w, valores, pesos, dp):
    n = len(valores)
    elementos = []
    i = n
    j = w
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            elementos.append((valores[i-1], pesos[i-1]))
            j -= pesos[i-1]
        i -= 1
    elementos.reverse()
    return elementos

"""
Complejidad: O(n*W)
Pseudo-polinomial, ya que la complejidad depende de la capacidad de la mochila.
W se puede considerar como un número entero, por lo que la complejidad es polinomial.

En bits, W se puede representar con log(W) bits. Por ende, W = 2^m, siendo m la cantidad
de bits que se utilizan para representar su valor entero. Por lo tanto, desde este punto
de vista, la complejidad es O(n*2^m), que es exponencial.

Generamos columnas con cada una de las permutaciones posibles de los pesos, y en cada una
de ellas calculamos el valor máximo que se puede obtener con los elementos que tenemos.
"""

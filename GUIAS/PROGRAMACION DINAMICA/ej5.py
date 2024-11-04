"""
(★) Dado un laberinto representado por una grilla, queremos calcular la
ganancia máxima que existe desde la posición (0,0) hasta la posición NxM.
Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)),
nos podemos mover hacia abajo o hacia la derecha. 
Pasar por un casillero determinado (i,j) nos da una ganancia de V(i,j).
Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto.
Hacer una reconstrucción del camino que se debe transitar.
Indicar y justificar la complejidad del algoritmo implementado.
Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?
"""

# bottom up con memo

def max_ganancia(laberinto):
    n = len(laberinto)
    m = len(laberinto[0])
    memo = [[0] * m for _ in range(n)]
    memo[0][0] = laberinto[0][0]
    for i in range(1, n):
        memo[i][0] = memo[i-1][0] + laberinto[i][0]
    for j in range(1, m):
        memo[0][j] = memo[0][j-1] + laberinto[0][j]
    for i in range(1, n):
        for j in range(1, m):
            memo[i][j] = max(memo[i-1][j], memo[i][j-1]) + laberinto[i][j]
    return memo[n-1][m-1]

# Complejidad: O(n*m) donde n es la cantidad de filas y m la cantidad de columnas del laberinto.
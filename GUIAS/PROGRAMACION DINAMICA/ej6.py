"""
Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad 
de posibles números de longitud n empezando por el botón del número inicial k. 
Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 
Implementar el algoritmo por programación dinámica. 
Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)

Para N=2, depende de con cuál dígito se comienza:

Empezando por 0, son válidos 00, 08 (cantidad: 2)

Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)

Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)

Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)

Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)

Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)

Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)

Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)

Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)

Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)

"""

def cantidad_numeros(n, k):
    movimientos = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    # Definimos la matriz de DP
    dp = [[0] * 10 for _ in range(n)]
    # Caso base
    for i in range(10):
        dp[0][i] = 1
    # Caso general
    for i in range(1, n):
        for j in range(10):
            for mov in movimientos[j]:
                dp[i][j] += dp[i-1][mov]
    return dp[n-1][k]

# Complejidad: O(n) donde n es la cantidad de "pasos" que se pueden dar en el teclado numérico.
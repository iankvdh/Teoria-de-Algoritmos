"""
(★★) Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, 
pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, 
determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar 
dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

# bottom up con memo
def max_ganancia(arr):
    n = len(arr)
    memo = [0] * n
    memo[0] = arr[0]
    memo[1] = max(arr[0], arr[1])
    for i in range(2, n):
        memo[i] = max(memo[i-1], memo[i-2] + arr[i])
    return memo

def reconstruir(memo, arr):
    n = len(arr)
    i = n - 1
    res = []
    while i >= 0:
        if i == 0:
            res.append(i)
            break
        if memo[i] == memo[i-1]:
            i -= 1
        else:
            res.append(i)
            i -= 2
    return res

# Complejidad: O(n) donde n es la cantidad de días en los que Juan tiene ofertas de trabajo.
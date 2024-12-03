"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata.
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que,
por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, 
y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
Para cada moneda, se calcula el mínimo entre la cantidad de monedas 
necesarias para dar el cambio sin usar la moneda actual, y la cantidad 
de monedas necesarias para dar el cambio usando la moneda actual.
Se toma el mínimo entre ambos valores.

If sum == 0:
    0 coins required
If sum > 0:
    minCoins(coins[0..m-1], sum ) = min { 1 + minCoins(sum-coin[i])} where, 0 <=i <= m-1 and coins[i] <= sum.
"""

def cambio_monedas(sistema, cambio):
    dp = [0] * (cambio + 1)
    for i in range(1, cambio + 1):
        dp[i] = float('inf')
        for j in range(len(sistema)):
            if sistema[j] <= i:
                dp[i] = min(dp[i], dp[i - sistema[j]] + 1)
    return dp

def monedas_cambio(sistema, cambio, dp):
    monedas = []
    i = cambio
    while i > 0:
        for j in range(len(sistema)):
            if sistema[j] <= i and dp[i] == dp[i - sistema[j]] + 1:
                monedas.append(sistema[j])
                i -= sistema[j]
                break
    return monedas

# Complejidad: O(n*cambio) donde n es la cantidad de monedas/billetes en el sistema monetario.
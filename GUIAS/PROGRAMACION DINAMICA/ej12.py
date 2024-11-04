"""
Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P 
que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta $Ci.
También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, 
que denominaremos Gi. Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe 
realizar Carlitos. Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores 
están expresados en pesos argentinos, dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, 
para pasar a pesos se debe hacer la conversión de divisa.
"""

"""
Para cada campaña, se calcula el máximo entre la ganancia de la campaña actual más la ganancia de la campaña anterior
que no se solape con la actual, y la ganancia de la campaña anterior.

Es igual al problema de la mochila, pero en vez de tener un peso, tenemos un costo.
"""

def campañas_publicitarias(P, costos, ganancias):
    n = len(costos)
    memo = [[0 for _ in range(P+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, P+1):
            if costos[i-1] <= j:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-costos[i-1]] + ganancias[i-1])
            else:
                memo[i][j] = memo[i-1][j]
    return memo

def campañas_elegidas(P, costos, ganancias, dp):
    n = len(costos)
    campañas = []
    i = n
    j = P
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            campañas.append(ganancias[i-1])
            j -= costos[i-1]
        i -= 1
    campañas.reverse()
    return campañas

"""
Complejidad: O(n*P)
Pseudo-polinomial, ya que la complejidad depende del presupuesto P.
P se puede considerar como un número entero, por lo que la complejidad es polinomial.

En bits, P se puede representar con log(P) bits. Por ende, P = 2^m, siendo m la cantidad
de bits que se utilizan para representar su valor entero. Por lo tanto, desde este punto
de vista, la complejidad es O(n*2^m), que es exponencial.

Generamos columnas con cada una de las permutaciones posibles de los costos, y en cada una
de ellas calculamos el valor máximo que se puede obtener con los elementos que tenemos.
"""

"""
Analisis de la conversion de monedas:
###
"""
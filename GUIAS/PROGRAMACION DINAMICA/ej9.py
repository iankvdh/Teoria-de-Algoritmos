"""
Tenemos un conjunto de números [v1, ..., vN], y queremos obtener un subconjunto 
de todos esos números tal que su suma sea igual o menor a un valor V, tratando 
de aproximarse lo más posible a V. Implementar un algoritmo que, 
por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, 
y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
Vemos que es un problema de mochila, pero en este caso no se busca maximizar el valor,
sino que se busca maximizar la suma de los valores de los elementos que se elijan,
sin pasarse de un valor V.

OPT(n,V) = max(OPT(n-1, V), OPT(n-1, V-valores[i]) + valores[i])
"""

def subconjunto_suma(valores, V):
    n = len(valores)
    dp = [[0] * (V+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for v in range(1, V+1):
            if valores[i-1] > v:
                dp[i][v] = dp[i-1][v]
            else:
                dp[i][v] = max(dp[i-1][v], dp[i-1][v-valores[i-1]] + valores[i-1])
    return dp

def elementos_subconjunto(valores, V, dp):
    n = len(valores)
    elementos = []
    i = n
    j = V
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            elementos.append(valores[i-1])
            j -= valores[i-1]
        i -= 1
    elementos.reverse()
    return elementos

"""
Complejidad: O(n*V)
Pseudo-polinomial, ya que la complejidad depende de la suma objetivo V.
V se puede considerar como un número entero, por lo que la complejidad es polinomial.

En bits, V se puede representar con log(V) bits. Por ende, V = 2^m, siendo m la cantidad
de bits que se utilizan para representar su valor entero. Por lo tanto, desde este punto
de vista, la complejidad es O(n*2^m), que es exponencial.

Generamos columnas con cada una de las permutaciones posibles de los valores, y en cada una
de ellas calculamos el valor máximo que se puede obtener con los elementos que tenemos.
"""

# igual creo que hay algo que está mal (pero dejo el código igual basado en lo que se habló en clase)

valores = [1, 2, 3, 4, 5]
V = 10
dp = subconjunto_suma(valores, V)
for i in dp:
    print(i)
print(elementos_subconjunto(valores, V, dp)) # [1, 4, 5] debería devolver [1, 2, 3, 4]

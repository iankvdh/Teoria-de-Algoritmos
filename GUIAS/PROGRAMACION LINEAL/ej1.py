import pulp

"""
(★) Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).
"""

"""
Identiquemos las variables del problema de la mochila:

{Tenemos una mochila con una capacidad W. Hay elementos a guardar, 
cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo que, por programación dinámica, reciba los valores 
y pesos de los elementos, y devuelva qué elementos deben ser guardados 
para maximizar la ganancia total. Indicar y justificar la complejidad del 
algoritmo implementado.}

W : capacidad de la mochila
Y(i) : elemento i -> Variable BINARIA (1 si lo puse en la mochila, 0 sino)
V(i) : costo del elemento i
P(i) : peso del elemento i

Nosotros queremos maximizar el valor de los elementos metidos en la mochila: 
MAX sum(V(i) * Y(i))

(La restricción es que no hay que exceder la capacidad de la mochila), entonces:
sum(P(i) * Y(i)) <= W
"""

def mochila_lineal(v, p, W):
    y = []
    for i in range(len(v)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))

    problema = pulp.LpProblem("elementos", pulp.LpMaximize)
    problema += pulp.LpAffineExpression([(y[i], p[i]) for i in range(len(y))]) <= W
    problema += pulp.LpAffineExpression([(y[i], v[i]) for i in range(len(y))])

    problema.solve()

    print(list(map(lambda yi: pulp.value(yi), y)))
    print(f"Peso usado: {sum([(p[i] * y[i]) for i in range(len(y))])}")
    print(f"Valor obtenido: {sum([(v[i] * y[i]) for i in range(len(y))])}")

# COMPLEJIDAD: Al utilizar variables BOOLEANAS, la complejidad algorítmica es EXPONENCIAL.
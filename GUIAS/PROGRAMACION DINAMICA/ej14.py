"""
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. 
Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad
de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede
obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de 
la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta
llegar a la casa n-1, que nos daría gn-1. Toda casa i se considera adyacente a las casas i-1 e i+1. 
Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con 
el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, 
los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. 
Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos 
encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que 
nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. 
Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles
casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, 
escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.
"""

# OPT(i) = max(OPT(i-1), OPT(i-2) + gi)
# OPT(0) = g0
# OPT(1) = max(g0, g1)

# Complejidad: O(n) donde n es la cantidad de casas en la calle. Se reutiliza juan el vago
# lo horrible es reconstruirlo xd

def construir_plan_malevolo(memo):
    sol = []
    i = len(memo)-1
    while i >= 0:
        if memo[i][1] == i:
            sol.append(i)
            i -=2
        else:
            i -=1
    sol.reverse()
    return sol


def _lunatico(ganancias):
    MEMO = [None] * (len(ganancias))
    MEMO[0] = (ganancias[0], 0)
    MEMO[1] = (max(ganancias[0], ganancias[1]), 0 if ganancias[0] > ganancias[1] else 1)
    for i in range(2, len(ganancias)):
        anteultimo = ganancias[i-2]
        ultimo = ganancias[i-1]
        actual = ganancias[i]
        MEMO[i] = (max(MEMO[i-2][0] + actual, MEMO[i-1][0]),
                   i if (MEMO[i-2][0] + actual > MEMO[i-1][0]) else i-1)
    return construir_plan_malevolo(MEMO)


def lunatico(ganancias):
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    if len(ganancias) == 2:
        return [ 0 if ganancias[0] > ganancias[1] else 1]
    
    sin_ultimo = _lunatico(ganancias[:len(ganancias)-1])
    sin_primero = _lunatico(ganancias[1:])

    for i in range(len(sin_primero)):
        sin_primero[i] += 1
    ganancia_sin_ultimo = 0
    ganancia_sin_primero = 0

    for i in sin_ultimo:
        ganancia_sin_ultimo += ganancias[i]
    for i in sin_primero:
        ganancia_sin_primero += ganancias[i]
    if ganancia_sin_primero > ganancia_sin_ultimo:
        return sin_primero
    return sin_ultimo

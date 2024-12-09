"""
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que 
anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. 
Para simplificar su trabajo, se los anota en un vector P donde P[i] 
contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. 
Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los 
integrantes de su grupo pueden sentarse. Implementar un algoritmo que, por backtracking, 
obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa 
(o en otras palabras, que dejan la menor cantidad de espacios vacíos).
"""

def max_grupos_bodegon(P, W):
    sol_optima = []
    sol_parcial = []
    return list(_max_grupos_bodegon(P, W, 0, sol_parcial, sol_optima))

def _max_grupos_bodegon(P, W, index, sol_parcial, sol_optima):
    if index == len(P):
        if sum(sol_parcial) > sum(sol_optima):
            return sol_parcial[:]
        return sol_optima

    if sum(sol_optima) == W:
        return sol_optima

    if P[index] > W:
        return _max_grupos_bodegon(P, W, index+1, sol_parcial, sol_optima)

    sol_parcial.append(P[index])

    if sum(sol_parcial) <= W:
        sol_optima = _max_grupos_bodegon(P, W, index+1, sol_parcial, sol_optima)

    sol_parcial.pop()
    return _max_grupos_bodegon(P, W, index+1, sol_parcial, sol_optima)

# Test
P = [ 5, 8, 6, 10, 18, 10, 18, 11, 4, 16, 9, 4, 16, 13, 7, 4, 3, 18, 13, 19 ]
W = 50
print(max_grupos_bodegon(P, W)) 
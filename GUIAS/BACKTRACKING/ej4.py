from graphs_src.grafo import Grafo

"""
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un 
conjunto de vértices que representen un máximo Independent Set del mismo.
"""

def independent_set(grafo):
    vertices = list(grafo.obtener_vertices())
    sol_parcial = set()
    sol_optima = set()
    for v in vertices:
        sol_parcial = ind_set(grafo, vertices, vertices.index(v), set(), set())
        if len(sol_parcial) > len(sol_optima):
            sol_optima = sol_parcial
    return list(sol_optima)

def ind_set(grafo, vertices, v_actual, visitados, sol_parcial):
    # caso de todos vertices sin aristas y un solo vertice
    if len(vertices) == len(sol_parcial):
        return sol_parcial

    # caso que ya recorri todos los vertices
    if len(vertices) == len(visitados):
        return sol_parcial

    # caso que no recorri todos los vertices pero llegue al final de mi lista
    if v_actual == len(vertices):
        return ind_set(grafo, vertices, 0, visitados, sol_parcial)

    sol_parcial.add(vertices[v_actual])
    visitados.add(vertices[v_actual])

    # reviso si mi sol_parcial cumple con ser ind_set, en tal caso avanzo
    if es_compatible(grafo, sol_parcial):
        return ind_set(grafo, vertices, v_actual + 1, visitados, sol_parcial)

    # si no es compatible, saco y avanzo
    sol_parcial.remove(vertices[v_actual])
    return ind_set(grafo, vertices, v_actual + 1, visitados, sol_parcial)

def es_compatible(grafo, sol_parcial):
    for v in sol_parcial:
        for w in grafo.adyacentes(v):
            if w in sol_parcial:
                return False
    return True


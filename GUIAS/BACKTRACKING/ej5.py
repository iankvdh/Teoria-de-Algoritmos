from graphs_src.grafo import Grafo

"""
Un camino hamiltoniano, es un camino de un grafo, 
que visita todos los vértices del grafo una sola vez. 
Implementar un algoritmo por backtracking que encuentre un 
camino hamiltoniano de un grafo dado.
"""

def camino_hamiltoniano(grafo):
    res = []
    vertices = grafo.obtener_vertices()
    for v in vertices:
        res = _camino_hamiltoniano(grafo,v, [])
        if len(res) == len(vertices):
            return res
    return -1 #no hay camino hamiltoniano    
    
def _camino_hamiltoniano(grafo, vertice, sol_parcial):
    sol_parcial.append(vertice)

    if len(sol_parcial) == len(grafo.obtener_vertices()):
        return sol_parcial

    for w in grafo.adyacentes(vertice):
        if w not in sol_parcial:
            return _camino_hamiltoniano(grafo, w, sol_parcial)

    sol_parcial.remove(vertice)
    return sol_parcial

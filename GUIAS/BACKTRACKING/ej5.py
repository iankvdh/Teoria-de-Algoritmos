from graphs_src.grafo import Grafo

"""
Un camino hamiltoniano, es un camino de un grafo, 
que visita todos los vértices del grafo una sola vez. 
Implementar un algoritmo por backtracking que encuentre un 
camino hamiltoniano de un grafo dado.
"""

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()
    
    for v in grafo:
        if _camino_hamiltoniano(grafo, v, visitados, camino):
            return camino
    
    return None

def _camino_hamiltoniano(grafo, v, visitados, camino):
    visitados.add(v)
    camino.append(v)
    
    if len(visitados) == len(grafo):
        return True
       
    for w in grafo.adyacentes(v):
        if w not in visitados:
            if _camino_hamiltoniano(grafo, w, visitados, camino):
                return True
    
    visitados.remove(v)
    camino.pop()
    
    return False
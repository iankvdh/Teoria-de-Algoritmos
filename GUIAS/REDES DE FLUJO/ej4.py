"""
(★) Dada una red residual, dar un algoritmo que encuentre un camino de aumento que minimice el número de aristas utilizadas.
"""

from graphs_src.grafo import *
from graphs_src.heap import Heap

def obtener_camino_de_aumento(grafo_residuaol, fuente, sumidero):
    """
    Camino de aumento: si encontramos un camino de la fuente (f) al sumidero (s) en el grafo residual,
    entonces encontramos un camino por el que podamos aumentar el flujo.
    Buscamos aumentar el flujo total pero puede reducirse el que pasa por alguna arista.
    """

    # Inicializamos estructuras para BFS
    visitados = set()
    padre = {}
    padre[fuente] = None
    visitados.add(fuente)
    
    # Cola para realizar la búsqueda en amplitud
    heap = Heap()
    heap.encolar(fuente)

    # Busco el camino más chico
    caminos_posibles = []

    # Realizamos BFS desde la fuente hasta el sumidero
    while heap:
        nodo_actual = heap.desencolar()

        # Si alcanzamos el sumidero, construimos el camino de aumento
        if nodo_actual == sumidero:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padre[nodo_actual]
            camino.append(fuente)
            camino.reverse()
            caminos_posibles.append(camino)

        # Exploramos los vecinos del nodo actual en el grafo residual
        for w in grafo_residuaol.obtener_adyacentes(nodo_actual):
            if not visitados[w]:
                heap.encolar(w)
                visitados[w] = True
                padre[w] = nodo_actual

    return min(caminos_posibles, key=len)

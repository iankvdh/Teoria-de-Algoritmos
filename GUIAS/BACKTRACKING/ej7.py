# KNIGHTs TOUR

"""
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez, 
determine los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez. 
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).
"""

"""
def problema_del_caballo():
  # debemos crear el grafo
  # por un lado, las 8x8 posiciones como vértices
  # luego se deben conectar con aristas los vértices, según movimiento del caballo
  camino = camino_hamiltoniano(grafo_construido_del_caballo)
  # reconstruir las posiciones del tablero según el camino
  # return solucion
"""
from graphs_src.grafo import Grafo

def knight_tour(n):
    grafo = Grafo()
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if abs(i - k) == 2 and abs(j - l) == 1:
                        grafo.agregar_arista((i, j), (k, l))
                    if abs(i - k) == 1 and abs(j - l) == 2:
                        grafo.agregar_arista((i, j), (k, l))
    camino = camino_hamiltoniano(grafo)
    if camino is None:
        return False
    return True

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()
    for v in grafo.obtener_vertices():
        if _camino_hamiltoniano(grafo, v, visitados, camino):
            return camino
    return None

def _camino_hamiltoniano(grafo, v, visitados, camino):
    visitados.add(v)
    camino.append(v)

    if len(visitados) == len(grafo.obtener_vertices()):
        return True
       
    for w in grafo.adyacentes(v):
        if w not in visitados:
            if _camino_hamiltoniano(grafo, w, visitados, camino):
                return True
    
    visitados.remove(v)
    camino.pop()
    return False

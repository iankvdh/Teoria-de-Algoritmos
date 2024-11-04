# Order: O(E log V)

from graphs_src.heap import Heap 
from graphs_src.grafo import Grafo

def camino_minimo_dijkstra(grafo, origen):
    distancias = {}
    padres = {}
    for vertice in grafo.obtener_vertices():
        distancias[vertice] = float('inf')
    distancias[origen] = 0
    padres[origen] = None
    heap = Heap()
    heap.encolar((origen, 0))
    while not heap.esta_vacia():
        vertice, distancia = heap.desencolar()
        for adyacente in grafo.obtener_adyacentes(vertice):
            peso = grafo.obtener_peso(vertice, adyacente)
            if distancias[vertice] + peso < distancias[adyacente]:
                distancias[adyacente] = distancias[vertice] + peso
                padres[adyacente] = vertice
                heap.encolar((adyacente, distancias[adyacente]))
    return distancias, padres


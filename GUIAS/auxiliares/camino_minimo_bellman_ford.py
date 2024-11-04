# Order: O(V*E)

from graphs_src.grafo import Grafo

def camino_minimo_bellman_ford(grafo, origen):
    distancias = {}
    padres = {}
    for vertice in grafo.obtener_vertices():
        distancias[vertice] = float('inf')
    distancias[origen] = 0
    padres[origen] = None
    aristas = grafo.obtener_aristas()
    for _ in range(grafo.obtener_vertices()):
        cambio = False
        for origen, destino, peso in aristas:
            if distancias[origen] + peso < distancias[destino]:
                cambio = True
                padres[destino] = origen
                distancias[destino] = distancias[origen] + peso
        if not cambio:
            break
    for origen, destino, peso in aristas:
        if distancias[origen] + peso < distancias[destino]:
            raise Exception("El grafo contiene un ciclo de peso negativo")
    return distancias, padres


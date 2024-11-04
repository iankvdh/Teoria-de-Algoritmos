# Order: O(V + E)

from graphs_src.grafo import Grafo
import graphs_src.cola as Cola

def bfs(grafo):
    padres = {}
    orden = {}
    visitados = set()
    for vertice in grafo.obtener_vertices():
        if vertice not in visitados:
            _bfs(grafo, vertice, visitados, padres, orden)
    return padres, orden

def _bfs(grafo, origen, visitados, padres, orden):
    visitados.add(origen)
    padres[origen] = None
    orden[origen] = 0
    cola = Cola()
    cola.encolar(origen)
    while not cola.esta_vacia():
        vertice = cola.desencolar()
        for adyacente in grafo.obtener_adyacentes(vertice):
            if adyacente not in visitados:
                padres[adyacente] = vertice
                orden[adyacente] = orden[vertice] + 1
                visitados.add(adyacente)
                cola.encolar(adyacente)

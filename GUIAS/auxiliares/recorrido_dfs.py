# Order: O(V + E)

from graphs_src.grafo import Grafo

def dfs(grafo):
    visitados = set()
    padres = {}
    orden = {}
    origen = grafo.obtener_vertice_aleatorio()
    padres[origen] = None
    orden[origen] = 0
    _dfs(grafo, origen, visitados, padres, orden)
    return padres, orden

def _dfs(grafo, vertice, visitados, padres, orden):
    visitados.add(vertice)
    for adyacente in grafo.obtener_adyacentes(vertice):
        if adyacente not in visitados:
            padres[adyacente] = vertice
            orden[adyacente] = orden[vertice] + 1
            _dfs(grafo, adyacente, visitados, padres, orden)
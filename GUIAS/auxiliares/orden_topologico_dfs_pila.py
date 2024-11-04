# Order: O(V + E)

from graphs_src.grafo import Grafo
import graphs_src.pila as Pila

def orden_topologico_dfs_pila(grafo):
    pila = Pila()
    visitados = set()
    for vertice in grafo.obtener_vertices():
        if vertice not in visitados:
            visitados.add(vertice)
            _dfs_orden_topologico(grafo, vertice, visitados, pila)
    orden = []
    while not pila.esta_vacia():
        orden.append(pila.desapilar())
    return orden

def _dfs_orden_topologico(grafo, vertice, visitados, pila):
    for adyacente in grafo.obtener_adyacentes(vertice):
        if adyacente not in visitados:
            visitados.add(adyacente)
            _dfs_orden_topologico(grafo, adyacente, visitados, pila)
    pila.apilar(vertice)
from auxiliares.graphs_src.heap import Heap 
import auxiliares.graphs_src.grafo as Grafo

### GREEDY ###
# Aplicar una regla sencilla que permita obtener el óptimo local a mi estado actual
# Aplican iterativamente esa regla, esperando llegar a un óptimo general
# SUCESION DE OPTIMOS LOCALES ---> ÓPTIMO GLOBAL

## KRUSKAL ##
# Siempre utilizar la arista de menor valor que aún no usé. El "Unionfind" me va a decir si corresponde a usar esa arista en el resultado o no.



## PRIM ##
# En base al vertice (v), saca del heap aquel vertice adyacente (w) que tenga menor peso y no haya sido visitado, así sucesivamente.



## DIJKSTRA ##
# Desde un cierto vertice, busco el camino minimo hacia el siguiente, así sucesivamente.
# Order: O(E log V)

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

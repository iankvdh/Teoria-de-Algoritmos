# Order: O(E log V)

from graphs_src.grafo import Grafo
from graphs_src.heap import Heap 

def arbol_tendido_minimo_prim(grafo):
    nuevo_grafo = Grafo()
    for vertice in grafo.obtener_vertices():
        nuevo_grafo.agregar_vertice(vertice)
    cola = Heap()
    visitados = set()
    vertice = grafo.obtener_vertice_aleatorio()
    for adyacente in grafo.obtener_adyacentes(vertice):
        cola.encolar((vertice, adyacente, grafo.obtener_peso(vertice, adyacente)))
    
    while not cola.esta_vacia():
        origen, destino, peso = cola.desencolar()
        if destino in visitados:
            continue
        visitados.add(destino)
        nuevo_grafo.agregar_arista(origen, destino, peso)
        for ady in grafo.obtener_adyacentes(destino):
            if ady not in visitados:
                cola.encolar((destino, ady, grafo.obtener_peso(destino, ady)))
    return nuevo_grafo
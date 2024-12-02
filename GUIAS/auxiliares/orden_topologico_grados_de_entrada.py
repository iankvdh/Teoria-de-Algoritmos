# Order: O(V + E)

from graphs_src.grafo import Grafo
import graphs_src.auxiliar as aux
import graphs_src.cola as Cola

def orden_topologico_grados_de_entrada(grafo):
    grados = aux.calcular_grados_entrada(grafo)
    cola = Cola()
    orden = []
    for vertice in grafo.obtener_vertices():
        if grados[vertice] == 0:
            cola.encolar(vertice)
    while not cola.esta_vacia():
        vertice = cola.desencolar()
        orden.append(vertice)
        for adyacente in grafo.adyacentes(vertice):
            grados[adyacente] -= 1
            if grados[adyacente] == 0:
                cola.encolar(adyacente)
    return orden


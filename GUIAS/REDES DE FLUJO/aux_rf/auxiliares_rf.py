from graphs_src.grafo import *
from graphs_src.heap import Heap 
from graphs_src.grafo import Grafo

def flujo(grafo, fuente, sumidero):
    """
    Algoritmo de Ford-Fulkerson para encontrar el flujo máximo en un grafo.
    grafo:grafo del que se quiere encontrar el flujo máximo.
    fuente: vertice con grado de entrada 0.
    sumidero: vertice con grado de salida 0.
    """
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            flujo[(v, w)] = 0

    grafo_residuo = Grafo()
    for v in grafo.obtener_vertices():
        grafo_residuo.agregar_vertice(v)
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            grafo_residuo.agregar_arista(v, w, grafo.obtener_peso(v, w))

    while (camino := obtener_camino(grafo_residuo, fuente, sumidero)) is not None:
        capacidad_residual_camino = min_peso(grafo_residuo, camino)
        for i in range(1, len(camino)):
            if grafo.contiene_arista(camino[i - 1], camino[i]):
                flujo[(camino[i - 1], camino[i])] += capacidad_residual_camino
                actualizar_grafo_residual(grafo_residuo, camino[i - 1], camino[i], capacidad_residual_camino)
            else:
                flujo[(camino[i], camino[i - 1])] -= capacidad_residual_camino
                actualizar_grafo_residual(grafo_residuo, camino[i], camino[i - 1], capacidad_residual_camino)

    return flujo


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

def reconstruir_camino_minimo(origen, destino, padres, distancias):
    if distancias[destino] == float('inf'):
        return None
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.append(origen)
    camino.reverse()
    return camino

def obtener_camino(grafo, origen, destino):
    distancias, padres = camino_minimo_dijkstra(grafo, origen)
    # devolver true si el destino es alcanzable desde el origen
    if distancias[destino] == float('inf'):
        return None
    return reconstruir_camino_minimo(origen, destino, padres, distancias)

def min_peso(grafo, camino):
    min_peso = float('inf')
    for i in range(1, len(camino)):
        peso = grafo.obtener_peso(camino[i - 1], camino[i])
        if peso < min_peso:
            min_peso = peso
    return min_peso

def actualizar_grafo_residual(grafo, origen, destino, valor):
    peso_anterior = grafo.obtener_peso(origen, destino)
    if peso_anterior == valor:
        grafo.eliminar_arista(origen, destino)
    else:
        grafo.modificar_peso(origen, destino, peso_anterior - valor)
    
    if not grafo.contiene_arista(destino, origen):
        grafo.agregar_arista(destino, origen, valor)
    else:
        grafo.modificar_peso(destino, origen, grafo.obtener_peso(destino, origen) + valor)


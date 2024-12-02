# Auxiliar functions for graphs

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

def calcular_grados_entrada(grafo):
    grados = {}
    for vertice in grafo.obtener_vertices():
        grados[vertice] = 0
    for vertice in grafo.obtener_vertices():
        for adyacente in grafo.adyacentes(vertice):
            grados[adyacente] += 1
    return grados
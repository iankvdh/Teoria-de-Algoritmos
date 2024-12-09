# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, 
# indique si es posible pintar cada vértice con n colores de tal forma 
# que no hayan dos vértices adyacentes con el mismo color.

def colorear(grafo, n):
    if grafo is None or n is None:
        return None

    colores = {}
    vertices = grafo.obtener_vertices()

    return n_coloreo_aux(grafo, vertices, colores, n, 0)

def es_compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True

def n_coloreo_aux(grafo, vertices, colores, n, idx):
    if idx == len(vertices):
        return True

    v = vertices[idx]

    for color in range(n):
        colores[v] = color
        if es_compatible(grafo, v, colores):
            if n_coloreo_aux(grafo, vertices, colores, n, idx + 1):
                return True
        del colores[v]

    return False


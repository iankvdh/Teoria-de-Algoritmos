# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, 
# indique si es posible pintar cada vértice con n colores de tal forma 
# que no hayan dos vértices adyacentes con el mismo color.

def n_coloreo(grafo, n):
    if grafo is None or n is None:
        return None
    colores = {}
    v = grafo.obtener_vertice_aleatorio()
    return n_coloreo_aux(grafo, v, colores, 0, n)

def es_compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if colores[w] == colores[v]:
            return False
    return True

def n_coloreo_aux(grafo, v, colores, color, n):
    colores[v] = color
    
    if len(colores) == grafo.obtener_vertices():
        if es_compatible(grafo, v, colores):
            return True
        else: 
            del colores[v]
            return False
        
    if not es_compatible(grafo, v, colores):
        del colores[v]
        return False
    
    for w in grafo.adyacentes(v):
        if w in colores:
            continue
        for color in range(n):
            if n_coloreo_aux(grafo, v, colores, color, n):
                return True
    
    del colores[v]
    return False

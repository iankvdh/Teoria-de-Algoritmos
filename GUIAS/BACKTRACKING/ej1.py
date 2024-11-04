# Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a V, 
# devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

def subconjunto_n(grafo, n):
    solucion = []
    vertices = grafo.obtener_vertices()
    return subconjunto_n_wrapper(grafo, n, vertices, 0, solucion)

def subconjunto_n_wrapper(grafo, n, vertices, v_actual_i, solucion):
    if len(solucion) == n: 
        return es_compatible(grafo, solucion)
    if v_actual_i == len(vertices):
        return False
    # poda?
    if not es_compatible(grafo, solucion):
        return False
    
    solucion.append(vertices[v_actual_i])
    if subconjunto_n_wrapper(grafo, n, vertices, v_actual_i + 1, solucion):
        return True
    solucion.remove(vertices[v_actual_i])
    return subconjunto_n_wrapper(grafo, n, vertices, v_actual_i + 1, solucion)
    
def es_compatible(grafo, solucion):
    for v in solucion:
        for w in solucion:
            if v == w: 
                continue
            if not grafo.estan_unidos(v, w):
                return False
    return True
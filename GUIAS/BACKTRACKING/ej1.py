# Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a V, 
# devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    solucion = set()
    vertices = grafo.obtener_vertices()
    subconjunto_n_wrapper(grafo, n, vertices, 0, solucion)
    if len(solucion) == 0:
        return None
    return list(solucion)

def subconjunto_n_wrapper(grafo, n, vertices, v_actual_i, solucion):
    if len(solucion) == n:
        return True
    if v_actual_i >= len(vertices):
        return False
    v_actual = vertices[v_actual_i]
    if es_solucion(grafo, solucion, v_actual):
        solucion.add(v_actual)
        if subconjunto_n_wrapper(grafo, n, vertices, v_actual_i + 1, solucion):
            return True
        solucion.remove(v_actual)
    return subconjunto_n_wrapper(grafo, n, vertices, v_actual_i + 1, solucion)

def es_solucion(grafo, solucion, v_actual):
    for v in solucion:
        if grafo.son_adyacentes(v, v_actual):
            return False
    return True

from graphs_src import grafo

"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo 
en el cual todas las aristas del grafo tienen al menos uno de sus 
extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices 
del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un 
Grafo no dirigido nos devuelva un conjunto de vértices que representen un 
mínimo Vertex Cover del mismo (es decir, que sea el conjunto de tamaño mínimo).
"""

def vertex_cover_min(grafo):
    vertices = list(grafo.obtener_vertices())
    sol_parcial = set(vertices)
    sol_optima = set(vertices)
    return list(vertex_cover_min_rec(grafo, vertices, sol_parcial, 0, sol_optima))

def vertex_cover_min_rec(grafo, vertices, sol_parcial, indice, sol_optima):
    if indice == len(vertices):
        if len(sol_parcial) < len(sol_optima):
            sol_optima.clear()
            sol_optima.update(sol_parcial)
        return set(sol_optima)

    v = vertices[indice]

    # sin considerar al vertice actual
    sol_parcial.remove(v)
    if es_valida(grafo, sol_parcial, v):
       sol_optima = vertex_cover_min_rec(grafo, vertices, sol_parcial, indice+1, sol_optima)
    
    # considerando al vertice actual
    sol_parcial.add(v)
    return vertex_cover_min_rec(grafo, vertices, sol_parcial, indice+1, sol_optima)

def es_valida(grafo, respuesta, v):
    for w in grafo.adyacentes(v):
        if not w in respuesta:
            return False
    return True

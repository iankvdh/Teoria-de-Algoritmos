import pulp
from graphs_src import grafo

"""
(★) Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).
"""

"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo 
en el cual todas las aristas del grafo tienen al menos uno de sus 
extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices 
del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un 
Grafo no dirigido nos devuelva un conjunto de vértices que representen un 
mínimo Vertex Cover del mismo (es decir, que sea el conjunto de tamaño mínimo).

Identificamos las variables:
- x_v: variable binaria que indica si el vértice v pertenece al Vertex Cover

Función objetivo:
- Minimizar la cantidad de vértices en el Vertex Cover

Restricciones:
- Para cada arista (u, v) que pertenezcan a E, al menos uno de los extremos debe estar en el Vertex Cover
es otras palabras,

x_u + x_v >= 1 para cada arista (u, v) que pertenezca a E
"""

def vertex_cover_min(grafo):
    # Obtener el conjunto de vértices y aristas del grafo
    vertices = grafo.obtener_vertices()
    aristas = []
    for vertice in vertices:
        for adyacente in grafo.obtener_adyacentes(vertice):
            aristas.append((vertice, adyacente))

    problema = pulp.LpProblem("Vertex_Cover_Minimo", pulp.LpMinimize)

    x = {v: pulp.LpVariable(f"x{v}", cat="Binary") for v in vertices}

    # Función objetivo: minimizar la cantidad de vértices en el Vertex Cover
    problema += pulp.lpSum([x[v] for v in vertices])

    # Restricciones: para cada arista (u, v) que pertenezcan a E, al menos uno de los extremos debe estar en el Vertex Cover
    for (u, v) in aristas:
        problema += x[u] + x[v] >= 1

    # Resolver el problema
    problema.solve()

    # Obtener los vértices seleccionados en el Vertex Cover
    vertex_cover = [v for v in vertices if pulp.value(x[v]) == 1]

    return vertex_cover
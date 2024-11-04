import pulp
from graphs_src import grafo

"""
(★★★) Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo.
"""

"""
Identifiquemos las variables:
- y_v: variable binaria que indica si el vértice v pertenece al Independent Set

Función objetivo:
- Maximizar
    sum(y_v) para todo v en V

Restricciones:
- Para cada vértice v en V, si v pertenece al Independent Set, entonces ninguno de sus adyacentes puede pertenecer al Independent Set
es otras palabras,
    y_v + sum(y_w) <= 1 + (n + 1) * (1 - y_v) para todo v en V

El (n+1) * (1 - y_v) es una forma de forzar a que si y_v = 0, entonces sum(y_w) <= 1 -> METODO DE BIG-M
"""

def independent_set(grafo):
    vertices  = grafo.obtener_vertices()
    y=dict()
    for v in vertices:
        y[v] = pulp.LpVariable(f"y{v}",cat = "Binary")
    problema = pulp.LpProblem("Independent set", pulp.LpMaximize)
    for v in vertices:
        problema += y[v] + pulp.lpSum([y[w] for w in grafo.adyacentes(v)]) <= 1 + (len(vertices) +1) * (1 - y[v])
    problema += pulp.lpSum(y[v] for v in vertices)
    problema.solve()

    return [v for v in vertices if pulp.value("y{v}") == 1]
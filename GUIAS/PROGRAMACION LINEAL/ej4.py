import pulp
from graphs_src import grafo

"""
(★) Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).
"""

"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, 
tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. 
Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

Identificamos las variables:
- x_v: variable binaria que indica si el vértice v pertenece al Dominating Set

Función objetivo:
- Minimizar la cantidad de vértices en el Dominating Set

Restricciones:
- Para cada vértice u que pertenezca a V, o bien u está en el Dominating Set, o bien al menos uno de sus adyacentes está en el Dominating Set
es otras palabras,

x_v + sum(x_u) >= 1 para todo u adyacente a v
"""

def dominating_set_min(grafo):
    # Obtener el conjunto de vértices y aristas del grafo
    vertices = grafo.obtener_vertices()

    problema = pulp.LpProblem("Dominating_Set_Minimo", pulp.LpMinimize)

    x = {v: pulp.LpVariable(f"x{v}", cat="Binary") for v in vertices}

    # Función objetivo: minimizar la cantidad de vértices en el Dominating Set
    problema += pulp.lpSum([x[v] for v in vertices])

    # Restricciones: para cada vértice u que pertenezca a V, o bien u está en el Dominating Set, o bien al menos uno de sus adyacentes está en el Dominating Set
    for u in vertices:
        problema += x[u] + pulp.lpSum([x[v] for v in grafo.adyacentes(u)]) >= 1

    problema.solve()

    dom_set = [v for v in vertices if pulp.value(x[v]) == 1]

    return dom_set
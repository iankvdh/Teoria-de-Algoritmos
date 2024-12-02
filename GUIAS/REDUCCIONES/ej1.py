"""
(★) El problema del Independent Set se define como: dado un grafo no dirigido,
obtener el máximo subconjunto de vértices del grafo tal que ningun par de vértices
del subconjunto sea adyacente entre si. Dicho conjunto es un Independet Set. 
Definir el problema de decisión del Independent Set. Luego, implementar un verificador
polinomial para este problema.
¿Cuál es la complejidad del verificador implementado? Justificar
"""

"""
Definición del problema de decisión del Independent Set:
Dado un grafo no dirigido G y un número entero k, determinar si existe un Independent Set
de tamaño k en G.

Independent Set: Un conjunto de vértices D de un grafo G, tal que para toda arista (u, v) de G,
u no pertenece a D o v no pertenece a D.
"""

from graphs_src.grafo import *

def independent_set_verifier(grafo, k, conjunto):
    if len(conjunto) != k:
        return False

    for v in conjunto:
        for w in grafo.adyacentes(v):
            if w in conjunto:
                return False
            
    return True

# Complejidad del verificador:  O(n^2) donde n es la cantidad de vértices del grafo.
# Justificación: Para cada vértice en el conjunto, se recorren todos los adyacentes de dicho vértice.
# POR ESTE VERIFICADOR, EL PROBLEMA DE DECISIÓN DEL INDEPENDENT SET ES NP.
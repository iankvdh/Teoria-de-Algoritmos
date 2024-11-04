"""
(★) El problema del Vertex Cover se define como: dado un grafo no dirigido, 
obtener el mínimo subconjunto de vértices del grafo tal que toda arista del 
grafo tenga al menos uno de sus vértices perteneciendo al subconjunto. Dicho 
conjunto es un Vertex Cover. Definir el problema de decisión del Vertex Cover. 
Luego, implementar un verificador polinomial para este problema. 
¿Cuál es la complejidad del verificador implementado? Justificar
"""

"""
Definición del problema de decisión del Vertex Cover:
Dado un grafo no dirigido G y un número entero k, determinar si existe un Vertex Cover
de tamaño k en G.

Vertex Cover: Un conjunto de vértices D de un grafo G, tal que para toda arista (u, v) de G,
u pertenece a D o v pertenece a D.
"""

from graphs_src.grafo import *

def vertex_cover_verifier(grafo, k, conjunto):
    if len(conjunto) != k:
        return False

    for v in conjunto:
        for w in grafo.obtener_adyacentes(v):
            if w not in conjunto:
                return False
            
    return True

# Complejidad del verificador:  O(n^2) donde n es la cantidad de vértices del grafo.
# Justificación: Para cada vértice en el conjunto, se recorren todos los adyacentes de dicho vértice.
# POR ESTE VERIFICADOR, EL PROBLEMA DE DECISIÓN DEL VERTEX COVER ES NP.
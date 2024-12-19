"""
(★★) Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). 
Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos 
s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo 
resuelve y cómo se consigue el máximo número de caminos disjuntos. 
¿Cuál es el orden temporal de la solución implementada?
"""

from graphs_src.grafo import Grafo
from graphs_src import cola as queue

def transformar_grafo(grafo, s, t): #O(V+E)
    grafo_dirigido = Grafo(grafo.obtener_vertices())
    
    vertices_nuevos = set() # esto es para no agregarlos al camino
    for v, w in grafo.obtener_aristas():
        if v == s:
            grafo_dirigido.agregar_arista(s, w, 1)
            continue
        if w == s: 
            grafo_dirigido.agregar_arista(s, v, 1)
            continue
        if v == t:
            grafo_dirigido.agregar_arista(w, t, 1)
            continue
        if w == t:
            grafo_dirigido.agregar_arista(v, t, 1)
            continue

        grafo_dirigido.agregar_arista(v, w, 1)
        vertice_nuevo = grafo.agregar_vertice(f'{v},{w}')
        vertices_nuevos.add(vertice_nuevo)
        grafo_dirigido.agregar_vertice(vertice_nuevo)
        grafo_dirigido.agregar_arista(w, vertice_nuevo, 1) 
        grafo_dirigido.agregar_arista(vertice_nuevo, v, 1)         
    return grafo_dirigido

def obtener_camino_aumentante(grafo, s, t):
    pass

def obtener_min_peso(grafo, camino):
    pass

def actualizar_grafo_res(grafo, u, v, max_ganancia):
    pass

def obtener_grafo_residual_ford_fulkerson(grafo, s, t): #O(V*E) porque todas las aristas tienen peso 1. Sino sería O(V*E^2)
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    
    grafo_res = grafo.copy()
    
    while (camino := obtener_camino_aumentante(grafo_res, s, t)) is not None:
        max_ganancia = obtener_min_peso(grafo_res, camino)
        
        for i in range(1, len(camino)):
            u = camino[i-1]
            v = camino[i]
            
            if grafo.hay_arista(u,v):
                flujo[(u,v)] += max_ganancia
            else:
                flujo[(v,u)] -= max_ganancia
            
            actualizar_grafo_res(grafo_res, u, v, max_ganancia)
    
    return grafo_res

def bfs(grafo, s): # O(V+E)
    visitados = set()
    cola = queue()
    cola.encolar(s)
    visitados.add(s)
    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                cola.encolar(w)
                visitados.add(w)
    return visitados


def obtener_corte_min(grafo, s, t): #O(V*E) porque todas las aristas tienen peso 1
    grafo_res = obtener_grafo_residual_ford_fulkerson(grafo, s, t)

    conj_fuente = bfs(grafo_res, s)
    
    peso_aristas_corte_min = 0
    for v in grafo_res:
        for w in grafo_res.adyacentes(v):
            if v in conj_fuente and w not in conj_fuente:
                peso_aristas_corte_min += grafo_res.obtener_peso_arista(v,w)

    return peso_aristas_corte_min

def main(grafo, v, w): # O(V*E)
    grafo_transformado = transformar_grafo(grafo, v, w)
    return obtener_corte_min(grafo_transformado, v, w)
"""
(★★) Dado un grafo no dirigido, un match es un subconjunto de las aristas en el cual para todo 
vértice v a lo sumo una arista del match incide en v (en el match, tienen grado a lo sumo 1). 
Decimos que el vértice v está matcheado si hay alguna arista que incida en él (sino, está unmatcheado).
El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor 
cantidad posible). Dar una metodología para encontrar el matching máximo de un grafo, explicando 
en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el matching máximo. 
¿Cuál es el orden temporal de la solución implementada?
"""

from graphs_src.grafo import Grafo
from graphs_src import cola as queue

def es_bipartito(grafo):
    """
    Verifica si un grafo es bipartito utilizando BFS.
    Retorna True si es bipartito, y los conjuntos U y V.
    """
    color = {}
    for v in grafo.obtener_vertices():
        if v not in color:
            cola = queue()
            cola.encolar(v)
            color[v] = 0  # Asignar un color inicial

            while not cola.esta_vacia():
                actual = cola.desencolar()
                for ady in grafo.adyacentes(actual):
                    if ady not in color:
                        color[ady] = 1 - color[actual]  # Asignar color opuesto
                        cola.encolar(ady)
                    elif color[ady] == color[actual]:
                        return False, None, None  # No es bipartito

    U = {v for v in color if color[v] == 0}
    # U es el conjunto de nodos con color 0
    V = {v for v in color if color[v] == 1}
    # V es el conjunto de nodos con color 1
    return True, U, V

def transformar_a_flujo(grafo, U, V):
    """
    Transforma el grafo bipartito en un grafo dirigido con fuente y sumidero para aplicar flujo máximo.
    """
    grafo_flujo = Grafo(dirigido=True)
    fuente = "s"
    sumidero = "t"

    grafo_flujo.agregar_vertice(fuente)
    grafo_flujo.agregar_vertice(sumidero)

    # Agregar aristas desde la fuente a los nodos de U
    for u in U:
        grafo_flujo.agregar_vertice(u)
        grafo_flujo.agregar_arista(fuente, u, 1)

    # Agregar aristas desde los nodos de V al sumidero
    for v in V:
        grafo_flujo.agregar_vertice(v)
        grafo_flujo.agregar_arista(v, sumidero, 1)

    # Agregar aristas originales entre U y V con capacidad 1
    for u in U:
        for v in grafo.adyacentes(u):
            if v in V:
                grafo_flujo.agregar_arista(u, v, 1)            

    return grafo_flujo, fuente, sumidero

def obtener_camino_aumentante(grafo, s, t):
    pass

def obtener_min_peso(grafo, camino):
    pass

def actualizar_grafo_res(grafo, u, v, max_ganancia):
    pass

def ford_fulkerson(grafo, s, t): #O(V*E) porque todas las aristas tienen peso 1. Sino sería O(V*E^2)
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
    
    return grafo_res, flujo

def calcular_flujo_maximo(grafo_residual, flujo, fuente, sumidero):
    """
    Calcula el flujo máximo dado un grafo residual y un flujo inicial.
    """
    flujo_maximo = 0
    # Sumar el flujo que sale del nodo fuente
    for v in grafo_residual.adyacentes(fuente):
        flujo_maximo += flujo.get((fuente, v), 0)
    return flujo_maximo

def matching_maximo(grafo):
    """
    Calcula el matching máximo en un grafo bipartito.
    """
    es_bip, U, V = es_bipartito(grafo)
    if not es_bip:
        return None

    grafo_flujo, fuente, sumidero = transformar_a_flujo(grafo, U, V)
    grafo_res, flujo = ford_fulkerson(grafo_flujo, fuente, sumidero)
    return calcular_flujo_maximo(grafo_res, flujo, fuente, sumidero)

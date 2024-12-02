"""
(★★) Dada una red y un diccionario que representa los valores de los flujos para las aristas, 
todos valores que respetan la restricción de cada arista, construir la red residual que refleja 
el estado actual de la red en función a los valores de flujo dados.
"""

from graphs_src.grafo import *
from graphs_src.heap import Heap

def red_residual(grafo, flujo):
    """
    Construye la red residual de un grafo en función de los valores de flujo dados.
    grafo: grafo original.
    flujo: diccionario con los valores de flujo para cada arista.
    """
    grafo_residuo = Grafo()
    for v in grafo.obtener_vertices():
        grafo_residuo.agregar_vertice(v)
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            # las mismas del grafo original pero con los pesos siendo la capacidad restante
            if flujo[(v, w)] < grafo.obtener_peso(v, w):
                grafo_residuo.agregar_arista(v, w, grafo.obtener_peso(v, w) - flujo[(v, w)])
            # las antiparalelas con los pesos siendo el flujo
            if flujo[(v, w)] > 0:
                grafo_residuo.agregar_arista(w, v, flujo[(v, w)])
    return grafo_residuo
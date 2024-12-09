from graphs_src import grafo
from auxiliares.graphs_src.auxiliar import calcular_grados_entrada

# Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

def es_isomorfico(grafo1, grafo2):
    """
    Determina si dos grafos son isomorfos utilizando backtracking.
    """
    # Verificar si tienen el mismo número de vértices
    if len(grafo1.obtener_vertices()) != len(grafo2.obtener_vertices()):
        return False

    # Listas de vértices de ambos grafos
    vertices1 = grafo1.obtener_vertices()
    vertices2 = grafo2.obtener_vertices()

    # Mapeo entre los vértices del primer grafo al segundo grafo
    mapeo = {}
    usados = set()  # Vértices del segundo grafo ya asignados
    return backtrack(vertices1, vertices2, grafo1, grafo2, 0, mapeo, usados)


def backtrack(vertices1, vertices2, grafo1, grafo2, indice, mapeo, usados):
    """
    Función recursiva para probar todas las correspondencias posibles entre vértices.
    """
    if indice == len(vertices1):
        # Si se ha asignado un mapeo a todos los vértices, verificar las aristas
        return verificar_aristas(vertices1, vertices2, grafo1, grafo2, indice, mapeo, usados)

    # Obtener el vértice actual del primer grafo
    v1 = vertices1[indice]

    for v2 in vertices2:
        if v2 not in usados:  # Si el vértice del segundo grafo no está usado
            # Asignar mapeo
            mapeo[v1] = v2
            usados.add(v2)

            # Avanzar al siguiente vértice
            if backtrack(vertices1, vertices2, grafo1, grafo2, indice + 1, mapeo, usados):
                return True

            # Backtracking: deshacer asignación
            del mapeo[v1]
            usados.remove(v2)

    return False

def verificar_aristas(vertices1, vertices2, grafo1, grafo2, indice, mapeo, usados):
    """
    Verifica que las aristas en grafo1 se correspondan con las aristas en grafo2 según el mapeo actual.
    """
    for v1 in vertices1:
        for vecino1 in grafo1.adyacentes(v1):
            v2 = mapeo[v1]
            vecino2 = mapeo.get(vecino1)

            # Si el mapeo no conserva la conexión o el peso, no es isomorfo
            if vecino2 is None or not grafo2.estan_unidos(v2, vecino2) or grafo1.peso_arista(v1, vecino1) != grafo2.peso_arista(v2, vecino2):
                return False
    return True

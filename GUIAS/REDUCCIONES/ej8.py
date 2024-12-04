"""
(★★) Definir los problemas de decisión de Camino Hamiltoniano y Ciclo Hamiltoniano. 
Sabiendo que Ciclo Hamiltoniano es NP-Completo, demostrar que Camino Hamiltoniano es NP-Completo.
"""

"""
1) Definición del problema de decisión de Camino Hamiltoniano:

Camino Hamiltoniano: Dado un grafo G, se busca un camino simple que visite cada vértice de G exactamente una vez.

2) Definición del problema de decisión de Ciclo Hamiltoniano:

Ciclo Hamiltoniano: Dado un grafo G, se busca un ciclo simple que visite cada vértice de G exactamente una vez.

"""

def verificar_camino_hamiltoniano(G, camino):
    # Verificar si existe un camino Hamiltoniano en G
    n = len(G)
    if len(camino) != n:
        return False
    visitados = set()
    for i in range(n-1):
        # si no llegué al final del camino, verifico si los vértices están unidos
        if camino[i] not in G:
            return False
        if camino[i] in visitados:
            return False
        if i <= n-2:
            if G.estan_unidos(camino[i], camino[i+1]) == False:
                return False
        visitados.add(camino[i])
    return True

"""
3) Reducción de Ciclo Hamiltoniano a Camino Hamiltoniano:

Ciclo Hamiltoniano es NP, ya que se puede verificar en tiempo polinomial si un ciclo dado en un grafo visita cada vértice exactamente una vez.

Queremos demostrar que Camino Hamiltoniano es NP-Completo. Para ello, se puede reducir Ciclo Hamiltoniano a Camino Hamiltoniano, es decir,
se puede transformar un problema de Ciclo Hamiltoniano en un problema de Camino Hamiltoniano.

Ciclo Hamiltoniano <=p Camino Hamiltoniano:
Dado un grafo G, se busca un ciclo Hamiltoniano en G.
Se puede transformar este problema a un problema de Camino Hamiltoniano de la siguiente manera:
- Se busca un camino Hamiltoniano en G. Si existe un camino Hamiltoniano en G, entonces se puede extender el camino para formar un ciclo Hamiltoniano.


4) Demostración:
Si existe un ciclo Hamiltoniano en G, entonces existe un camino Hamiltoniano en G.
Sea C un ciclo Hamiltoniano en G. Entonces, se puede obtener un camino Hamiltoniano en G eliminando una arista de C.

Si existe un camino Hamiltoniano en G, entonces existe un ciclo Hamiltoniano en G.
Sea P un camino Hamiltoniano en G. Entonces, se puede obtener un ciclo Hamiltoniano en G agregando una arista a P.

Por lo tanto, se puede reducir Ciclo Hamiltoniano a Camino Hamiltoniano.
"""


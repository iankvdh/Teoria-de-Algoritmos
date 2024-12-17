"""
(★★★) El problema de selección de caminos (Path Selection) pregunta: dado un grafo dirigido G 
y un set de pedidos P1, P2, …, Pc de caminos dentro de dicho grafo y un número k, 
¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados 
comparta ningún nodo? Dato: Path Selection es un problema NP-Completo. 
Ahora bien, queremos demostrar nuevamente (pero de otra forma a la vista en clase) que 
Independent Set es un problema NP-Completo. 
Demostrar que Independent Set es un problema NP-Completo, utilizando Path Selection para esto.
"""

"""
1) Definición del problema de decisión de Path Selection:

Path Selection: Dado un grafo dirigido G y un set de pedidos P1, P2, ..., Pc de caminos dentro de dicho grafo y un número k, se busca determinar si es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo.

2) Definición del problema de decisión de Independent Set:

Independent Set: Dado un grafo G y un número k, se busca un conjunto de vértices D de G tal que ningún par de vértices en D esté conectado por una arista, y |D| >= k.
"""

def verificador_ind_set(G, k, D):
    """
    Verifica si la solución de Independent Set es correcta.
    D es el conjunto de vértices que se utilizarán como Independent Set.
    """
    if len(D) < k:
        return False

    # chequeo de que ningún par de vértices en D esté conectado por una arista
    for u in D:
        for v in D:
            if u != v and G.existe_arista(u, v):
                return False
    return True

"""
3) Reducción de Path Selection a Independent Set:

(Path Selection) <=p (Independent Set)

Para reducir Path Selection a Independent Set, se puede realizar la siguiente transformación:

Dada una instancia de Path Selection con un grafo dirigido G y un set de pedidos P1, P2, ..., Pc de caminos dentro de dicho grafo, y un número k, queremos demostrar que es posible seleccionar al menos k de esos caminos de manera que ningún par de caminos seleccionados comparta ningún nodo.

Construimos un grafo no dirigido G' de la siguiente manera:

- Cada camino Pi del conjunto de caminos corresponde a un nodo vi en el grafo G'.
Por lo tanto, el grafo G' tendrá un nodo por cada camino de la instancia de Path Selection.

- Dibujamos una arista entre dos nodos vi y vj en G' si los caminos Pi y Pj comparten algún nodo en el grafo dirigido G.
Esto asegura que los caminos que comparten nodos están "conectados" en G'.

- El número k de la instancia de Path Selection se mantiene igual en la instancia de Independent Set.

4) Demostración:

Si existe una solución para Path Selection que selecciona al menos k caminos sin nodos compartidos, entonces en G' seleccionamos los nodos correspondientes a esos caminos. Como esos caminos no comparten nodos, no existe ninguna arista entre los nodos seleccionados en G'. Por lo tanto, los nodos seleccionados forman un conjunto independiente de tamaño k.

Si existe un conjunto independiente de tamaño k en G', entonces seleccionamos los caminos correspondientes a esos nodos en G.
Como los nodos en un conjunto independiente no tienen aristas entre sí, los caminos correspondientes no comparten nodos.

Por lo tanto, se puede reducir Path Selection a Independent Set. Y como Path Selection es NP-Completo, entonces Independent Set también es NP-Completo por transitividad.
"""
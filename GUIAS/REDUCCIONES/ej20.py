"""
(★★★★) El problema de elección de caminos (Path Selection) pregunta: dado un grafo 
dirigido G y un set de pedidos P1,P2,⋯,Pc de caminos dentro de dicho grafo y un número k, 
¿es posible seleccionar al menos k de esos caminos tales que ningún par de caminos 
seleccionados comparta ningún nodo? Demostrar que Path Selection es un problema NP-Completo. 
Ayuda: este problema tiene mucha semejanza con Independent Set.
"""

"""
1) Definición del problema de decisión de Path Selection:

Path Selection: Dado un grafo dirigido G y un set de pedidos P1, P2, ..., Pc de caminos dentro de dicho grafo y un número k, se busca determinar si es posible seleccionar al menos k de esos caminos tales que ningún par de caminos seleccionados comparta ningún nodo.

2) Definición del problema de decisión de Independent Set:

Independent Set: Dado un grafo G y un número k, se busca un conjunto de vértices D de G tal que ningún par de vértices en D esté conectado por una arista, y |D| >= k.
"""

def verificador_path_selection(G, pedidos, k, caminos):
    """
    Verifica si la solución de Path Selection es correcta.
    """
    if len(caminos) < k:
        return False

    # chequeo de que ningún par de caminos seleccionados comparta ningún nodo
    for i in range(len(caminos)):
        for j in range(i+1, len(caminos)):
            if set(caminos[i]).intersection(set(caminos[j])):
                return False
    return True

"""
3) Reducción de Independent Set a Path Selection:

(Independent Set) <=p (Path Selection)

Para reducir Independent Set a Path Selection, se puede realizar la siguiente transformación:

- Para cada nodo v que pertenece al conjunto de nodos V del grafo original G, creamos un nodo correspondiente v' en G'.
- Para cada arista (u, v) que pertenece al conjunto de aristas E del grafo original G, agregamos un camino dirigido u' → v' en G'.
- Para cada nodo v en V, definimos un camino Pv que comienza y termina en el nodo v'.
- Cada camino Pv es un "camino trivial" que pasa únicamente por el nodo v'.

Queremos seleccionar al menos k caminos Pv del conjunto P tales que ningún par de caminos comparta ningún nodo. 
En este contexto, si seleccionamos dos caminos Pu y Pv, implicaría que los nodos u y v no pueden tener ninguna 
arista entre ellos en el grafo original G.

4) Demostración:

Si existe un conjunto independiente de tamaño k en G, entonces seleccionamos los caminos correspondientes a esos nodos en G'. Como los nodos en un conjunto independiente no tienen aristas entre sí, los caminos correspondientes no comparten ningún nodo.

Si existen k caminos en G' que no comparten ningún nodo, entonces los nodos correspondientes en G forman un conjunto independiente de tamaño k.

Por lo tanto, se puede reducir Independent Set a Path Selection. Y como Independent Set es NP-Completo, entonces Path Selection también es NP-Completo por transitividad.
"""
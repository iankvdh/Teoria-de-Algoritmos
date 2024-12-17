"""
(★★★) Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, 
tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. 
El problema de decisión del set dominante implica, dado un grafo G y un número k, determinar si existe 
un set dominante D de a lo sumo tamaño k. 
Demostrar que el Dominating Set Problem es un problema NP-Completo. 
Ayuda: recomendamos recordar Vertex Cover, que puede ser útil para esto.
"""

"""
1) Definición del problema de decisión del Dominating Set Problem:

Dados un grafo G y un número k, se busca un conjunto de vértices D de G tal que cada vértice de G está en D o es adyacente a un vértice en D, y |D| <= k.

2) Definición del problema de decisión de Vertex Cover:
Dados un grafo G y un número k, se busca determinar si existe un conjunto de vértices D de G tal que cada arista de G tiene al menos un extremo en D, y |D| <= k.
"""

def verificador_dominating_set(G, k, D):
    """
    Verifica si la solución del Dominating Set es correcta.
    D es el conjunto de vértices que se utilizarán como set dominante.
    """
    if len(D) > k:
        return False

    # chequeo de que cada vértice de G está en D o es adyacente a un vértice en D
    for v in G.obtener_vertices():
        if v not in D:
            for u in G.obtener_adyacentes(v):
                if u not in D:
                    return False            
    return True

"""
3) Reducción de Vertex Cover a Dominating Set:

(Vertex Cover) <=p (Dominating Set)

Para reducir Vertex Cover a Dominating Set, se puede realizar la siguiente transformación:

Para un grafo G = (V, E) y un número k, construiremos un nuevo grafo G' tal que:
El conjunto dominante D en G' corresponderá a un conjunto de vértices que resuelve el problema de Vertex Cover en G.
- Empezamos con el grafo original G = (V, E).
- Para cada arista e = (u, v) en E, añadimos un nuevo vértice w_uv al grafo G'.
- Conectamos el nuevo vértice w_uv con los dos extremos de la arista, es decir, con u y v.

De esta forma, el grafo G' tendrá:
- Los vértices originales V.
- Los nuevos vértices w_uv (uno por cada arista e en E).

4) Demostración:

En G', un Vertex Cover de tamaño k en G corresponde a un Dominating Set de tamaño k en G'.

Esto ocurre porque:
- En un Vertex Cover, para cubrir cada arista (u, v), al menos uno de los vértices u o v debe estar en el conjunto C.
- En G', el vértice w_uv (añadido para cada arista) necesita ser dominado. Esto se logra si al menos uno de los vértices u o v está en el Dominating Set D.

Entonces, si existe un Vertex Cover de tamaño k en G, entonces existe un Dominating Set de tamaño k en G'. Y viceversa.

Por lo tanto, se puede reducir Vertex Cover a Dominating Set y, como Vertex Cover es NP-Completo, entonces Dominating Set también es NP-Completo por transitividad.
"""

"""
(★★) El Hitting-Set Problem se define de la siguiente forma: Dado un conjunto de elementos A con n elementos,
y m subconjuntos B1, B2, ..., Bm de A (es decir, Bi es un subconjunto de A para todo i), junto con un número k,
¿existe un subconjunto C de A con tamaño menor o igual a k tal que C contenga al menos un elemento de cada 
subconjunto Bi (es decir, la intersección de C con Bi no es vacía para todo i)?

Demostrar que el Hitting-Set Problem es un problema NP-Completo.
"""

"""

1) Definición del problema de decisión del Hitting-Set Problem:

Hitting-Set Problem: Dado un conjunto de elementos A con n elementos, y m subconjuntos B1, B2, ..., Bm de A, junto con un número k, se busca determinar si existe un subconjunto C de A con tamaño menor o igual a k tal que C contenga al menos un elemento de cada subconjunto Bi.

2) Definición del problema de decisión de Dominating Set:

Dominating Set: Dado un grafo G y un número k, se busca un conjunto de vértices D de G tal que cada vértice de G está en D o es adyacente a un vértice en D, y |D| <= k.
"""

def verificador_hitting_set(A, conjs_B, k, C):
    """
    Verifica si la solución del hitting set es correcta.
    """
    if len(C) > k:
        return False

    for bi in conjs_B:
        aparece = False
        for c in C:
            if c in bi:
                aparece = True
                break
        if not aparece:
            return False
    return True

"""
3) Reducción de Dominating Set a Hitting-Set Problem:

(Dominating Set) <=p (Hitting-Set Problem)

Para reducir Dominating Set a Hitting-Set Problem, se puede realizar la siguiente transformación:
Dado un grafo G y un número k, se busca un conjunto de vértices D de G tal que cada vértice de G está en D o es adyacente a un vértice en D, y |D| <= k.
Se puede transformar este problema a un problema de Hitting-Set de la siguiente manera:
- Se construye un conjunto A con los vértices de G.
- Se construye un conjunto de subconjuntos B1, B2, ..., Bm de A de la siguiente manera:
    - Para cada vértice v en G, se construye un subconjunto Bv de A con los vértices adyacentes a v.
- Se busca un subconjunto C de A con tamaño menor o igual a k tal que C contenga al menos un vértice de cada subconjunto Bv.
"""
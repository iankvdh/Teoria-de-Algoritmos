"""
(★★) En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. 
El rey Aragorn no quiere que todo su esfuerzo en construir calles resulte en vano, por lo que quiere poner 
guardianes a vigilar las calles por las noches. El problema es que cuesta mucho dinero entrenar a dichos 
guardianes, por lo que quiere reducir al mínimo la cantidad que sean necesarios entrenar. Sabe que cada 
guardian puede estar vigilando desde una esquina, y desde allí tener visibilidad hasta cualquier otra 
esquina directa. Necesita determinar la cantidad mínima de guardianes que son necesarios para cubrir todas
las calles de su reino. Como primera medida, consulta con el oráculo Discipulus Theoriae Algoritmi 
(es decir, quien lee esta consigna), para determinar si esto es conseguible en corto tiempo 
(el oráculo le pregunó algo sobre tiempo polinomial, que Aragorn no entendió y le dijo “si, eso”).
Tenemos que explicarle a Aragorn que este pedido no es realizable (y debe armarse de paciencia, o no buscar 
el mínimo exacto), porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo (en su 
versión de problema de decisión: 
“¿Se pueden vigilar todas las calles con esta topología con un máximo de K guardianes?”).
"""

"""
1) Definición del problema de decisión de Guardianes de Gondor:

Guardianes de Gondor: Dado un grafo G y un número k, se busca determinar si es posible cubrir todas las aristas de G con un máximo de k vértices.

2) Definición del problema de decisión de Vertex Cover:

Vertex Cover: Dado un grafo G y un número k, se busca determinar si existe un conjunto de vértices D de G tal que cada arista de G tiene al menos un extremo en D, y |D| <= k.
"""

def verificador_guardianes_gondor(G, k, D):
    """
    Verifica si la solución de Guardianes de Gondor es correcta.
    D es el conjunto de vértices que se utilizarán como guardianes.
    """
    if len(D) > k:
        return False

    # chequeo de que cada arista tenga al menos un extremo en D
    for u, v in G.obtener_aristas():
        if u not in D and v not in D:
            return False
    return True

"""
3) Reducción de Vertex Cover a Guardianes de Gondor:

(Vertex Cover) <=p (Guardianes de Gondor)

Para reducir Vertex Cover a Guardianes de Gondor, se puede realizar la siguiente transformación:
Dado un grafo G y un número k, se busca determinar si existe un conjunto de vértices D de G tal que cada arista de G tiene al menos un extremo en D, y |D| <= k.

El reino de Gondor puede representarse como un grafo no dirigido donde:

- Los vértices representan las esquinas de las calles.
- Las aristas representan las calles que conectan dos esquinas.
- Un guardián colocado en una esquina (vértice) puede "vigilar" todas las calles (aristas) que salen de esa esquina.

Se puede transformar este problema a un problema de Guardianes de Gondor de la siguiente manera:
- Se construye un grafo G' con los mismos vértices que G.
- Se busca determinar si es posible cubrir todas las aristas de G' con un máximo de k vértices.

4) Demostración:

Si existe un conjunto de vértices D de G tal que cada arista de G tiene al menos un extremo en D, y |D| <= k, entonces es posible cubrir todas las aristas de G' con un máximo de k vértices.

Sea D un conjunto de vértices de G tal que cada arista de G tiene al menos un extremo en D, y |D| <= k. Entonces, se puede colocar un guardián en cada vértice de D. Cada guardián puede "vigilar" todas las aristas que salen de su vértice correspondiente. Por lo tanto, es posible cubrir todas las aristas de G' con un máximo de k vértices.

Por lo tanto, se puede reducir Vertex Cover a Guardianes de Gondor. Y como Vertex Cover es NP-Completo, entonces Guardianes de Gondor también es NP-Completo por transitividad.
"""
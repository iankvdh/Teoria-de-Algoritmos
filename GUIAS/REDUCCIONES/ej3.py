"""
(★★) Dados los problemas de decisiones de Independent Set y Vertex Cover, 
realizar dos reducciones. 
a. Reducir Independent Set a Vertex Cover. 
b. Reducir Vertex Cover a Independent Set.
"""

"""

1) Cual es el problema de decisión de Vertex Cover?

Vertex Cover: Un conjunto de vértices D de un grafo G, tal que para toda arista (u, v) de G,
u pertenece a D o v pertenece a D. Es decir, busca un subconjunto de vértices que cubra todas las aristas del grafo.

2) Cual es el problema de decisión de Independent Set?

Independent Set: Un conjunto de vértices D de un grafo G, tal que para toda arista (u, v) de G,
u no pertenece a D o v no pertenece a D. Es decir, busca un subconjunto de vértices que no tengan aristas entre sí.

3) Reducción de Independent Set a Vertex Cover:

Para reducir Independent Set a Vertex Cover, se puede realizar la siguiente transformación:
Dado un grafo G y un número entero k, se busca un Independent Set de tamaño k en G.
Se puede transformar este problema a un problema de Vertex Cover de la siguiente manera:
Se busca un Vertex Cover de tamaño |V| - k en G.

Demostración:
Si existe un Independent Set de tamaño k en G, entonces existe un Vertex Cover de tamaño |V| - k en G.
Sea D un Independent Set de tamaño k en G. Entonces, el conjunto de vértices V - D es un Vertex Cover de tamaño |V| - k en G.
Si D es un Independent Set, entonces no hay aristas entre los vértices de D. Por lo tanto, todas las aristas de G están cubiertas por los vértices de V - D.

Si existe un Vertex Cover de tamaño |V| - k en G, entonces existe un Independent Set de tamaño k en G.
Sea D un Vertex Cover de tamaño |V| - k en G. Entonces, el conjunto de vértices V - D es un Independent Set de tamaño k en G.
Si D es un Vertex Cover, entonces todos los vértices de G están cubiertos por los vértices de D. Por lo tanto, no hay aristas entre los vértices de V - D.

Por lo tanto, se puede reducir Independent Set a Vertex Cover.

4) Reducción de Vertex Cover a Independent Set:

Para reducir Vertex Cover a Independent Set, se puede realizar la siguiente transformación:
Dado un grafo G y un número entero k, se busca un Vertex Cover de tamaño k en G.
Se puede transformar este problema a un problema de Independent Set de la siguiente manera:
Se busca un Independent Set de tamaño |V| - k en G.

Demostración:
Si existe un Vertex Cover de tamaño k en G, entonces existe un Independent Set de tamaño |V| - k en G.
Sea D un Vertex Cover de tamaño k en G. Entonces, el conjunto de vértices V - D es un Independent Set de tamaño |V| - k en G.
Si D es un Vertex Cover, entonces todos los vértices de G están cubiertos por los vértices de D. Por lo tanto, no hay aristas entre los vértices de V - D.

Si existe un Independent Set de tamaño |V| - k en G, entonces existe un Vertex Cover de tamaño k en G.
Sea D un Independent Set de tamaño |V| - k en G. Entonces, el conjunto de vértices V - D es un Vertex Cover de tamaño k en G.
Si D es un Independent Set, entonces no hay aristas entre los vértices de D. Por lo tanto, todas las aristas de G están cubiertas por los vértices de V - D.

Por lo tanto, se puede reducir Vertex Cover a Independent Set.
"""
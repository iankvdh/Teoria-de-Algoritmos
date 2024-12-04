"""
Definir los problemas de decisión de Grafo Bipartito y 3-Coloreo. 
Sabiendo que 3-Coloreo es NP-Completo, reducir Grafo Bipartito a 3-Coloreo. 
¿Podemos afirmar que Grafo Bipartito es un problema NP-Completo?
"""

"""

1) Definición del problema de decisión de Grafo Bipartito:

Grafo Bipartito: Dado un grafo G, se busca determinar si los vértices de G pueden ser divididos en dos conjuntos disjuntos U y V, de tal forma que cada arista de G conecte un vértice de U con un vértice de V.

2) Definición del problema de decisión de 3-Coloreo:

3-Coloreo: Dado un grafo G, se busca determinar si los vértices de G pueden ser coloreados con 3 colores de tal forma que dos vértices adyacentes no tengan el mismo color.

"""

def verificador_bipartito(grafo, u, v):
    """
    Verifica si un grafo es bipartito.
    """
    if len(u) + len(v) != len(grafo.obtener_vertices()):
        return False

    for vertice in grafo.obtener_vertices():
        if vertice in u:
            for adyacente in grafo.obtener_adyacentes(vertice):
                if adyacente in u:
                    return False
        if vertice in v:
            for adyacente in grafo.obtener_adyacentes(vertice):
                if adyacente in v:
                    return False
                
    return True

"""
3) Como buscamos analizar si Grafo Bipartito es un problema NP-Completo, vamos a reducir Grafo Bipartito a 3-Coloreo.
De esta forma, al ser 3-Coloreo NP-completo por enunciado, sabemos que si logramos dicha reducción, Grafo Bipartito también lo será por transitividad.

Grafo Bipartito <=p 3-Coloreo:

Para reducir Grafo Bipartito a 3-Coloreo, se puede realizar la siguiente transformación:
- Dado un grafo G, se busca determinar si los vértices de G pueden ser divididos en dos conjuntos disjuntos U y V, de tal forma que cada arista de G conecte un vértice de U con un vértice de V.
- Se utiliza la caja negra de 3-coloreo pero en vez de pasar 3 colores, se pasan 2 colores. 
Esto entonces es una transformación polinomial, ya que se puede hacer en tiempo polinomial.

4) Demostración:
Si tenemos un grafo G que es bipartito, entonces podemos colorear los vértices de G con 2 colores de tal forma que dos vértices adyacentes no tengan el mismo color. Esto se prueba fácilmente ya que los vértices de G pueden ser divididos en dos conjuntos disjuntos U y V, de tal forma que cada arista de G conecte un vértice de U con un vértice de V. Por lo tanto, se puede colorear los vértices de G con 2 colores de tal forma que dos vértices adyacentes no tengan el mismo color.

Si tenemos un grafo G que puede ser coloreado con 2 colores de tal forma que dos vértices adyacentes no tengan el mismo color, entonces G es bipartito. Esto se prueba fácilmente ya que si los vértices de G pueden ser coloreados con 2 colores de tal forma que dos vértices adyacentes no tengan el mismo color, entonces los vértices de G pueden ser divididos en dos conjuntos disjuntos U y V, de tal forma que cada arista de G conecte un vértice de U con un vértice de V. Por lo tanto, G es bipartito.

Ahora bien, nosotros sabemos que 3-Coloreo es NP-Completo. Por lo tanto, si reducimos Grafo Bipartito a 3-Coloreo, entonces NO PODEMOS AFIRMAR que Grafo Bipartito es NP-Completo con esta demostración. Si, es NP pero no podemos afirmar que sea NP-Completo.

Es más, existe un algoritmo polinómico eficiente para determinar si un grafo es bipartito, basado en recorrer el grafo (por ejemplo, usando BFS o DFS) y verificar si es 2-coloreable. 

Por lo tanto, Grafo Bipartito no es NP-Completo con esta demostración.
"""
    

"""
(★★) Definir los problemas de decisión de Independent Set y K-Clique. 
Hacer una reducción de Independet Set a K-Clique. 
Dada esta reducción, ¿podemos afirmar que K-Clique es un problema NP-Completo?
"""

"""
1) Definición del problema de decisión de Independent Set:

Independent Set: Dado un grafo G y un número entero k, se busca un conjunto de vértices D de G tal que ningún par de vértices en D esté conectado por una arista en G y |D| >= k.

2) Definición del problema de decisión de K-Clique:

K-Clique: Dado un grafo G y un número entero k, se busca un subgrafo H de G tal que H sea un clique de tamaño k.

3) Reducción de Independent Set a K-Clique:

Para reducir Independent Set a K-Clique, se puede realizar la siguiente transformación:
(Independent Set) <=p (K-Clique)
Para reducir Independent Set a K-Clique, se construye un grafo G' de la siguiente manera:
- Se toma el grafo G original de Independent Set.
- Se invierte las aristas de G, es decir, si dos vértices estaban conectados por una arista en G, en G' no hay arista entre ellos.
- Se busca un K-Clique en el grafo G' de tamaño k.

4) Demostración:
Si existe un Independent Set de tamaño k en el grafo G, entonces existe un K-Clique de tamaño k en el grafo G'. Sea D un conjunto de vértices de G tal que en cada vértice de D no hay aristas entre ellos. Entonces, D es un Independent Set de tamaño k en el grafo G. Si D es un Independent Set, entonces no hay aristas entre los vértices de D en G. Por lo tanto, D es un K-Clique de tamaño k en el grafo G'.

Si existe un K-Clique de tamaño k en el grafo G', entonces existe un Independent Set de tamaño k en el grafo G. Sea H un subgrafo de G' tal que H es un K-Clique de tamaño k. Entonces, en H no hay aristas entre los vértices de H en G'. Si se invierten las aristas de G', entonces en G no hay aristas entre los vértices de H. Por lo tanto, H es un Independent Set de tamaño k en el grafo G.

Por lo tanto, se puede reducir Independent Set a K-Clique.
"""
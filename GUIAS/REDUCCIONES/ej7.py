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
Dado un grafo G y un número entero k, se busca un Independent Set de tamaño k en G.
Se puede transformar este problema a un problema de K-Clique de la siguiente manera:
Se busca un K-Clique de tamaño k en el complemento de G.

Demostración:
Si existe un Independent Set de tamaño k en G, entonces existe un K-Clique de tamaño k en el complemento de G.
Sea D un Independent Set de tamaño k en G. Entonces, el conjunto de vértices V - D es un K-Clique de tamaño k en el complemento de G.
Si D es un Independent Set, entonces no hay aristas entre los vértices de D. Por lo tanto, en el COMPLEMENTO de G, todas las aristas están presentes entre los vértices de V - D.

Si existe un K-Clique de tamaño k en el complemento de G, entonces existe un Independent Set de tamaño k en G.
Sea D un K-Clique de tamaño k en el complemento de G. Entonces, el conjunto de vértices V - D es un Independent Set de tamaño k en G.
Si D es un K-Clique, entonces todas las aristas del complemento de G están presentes entre los vértices de D. Por lo tanto, en G, no hay aristas entre los vértices de V - D.

Por lo tanto, se puede reducir Independent Set a K-Clique.
"""
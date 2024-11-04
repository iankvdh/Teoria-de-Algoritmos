"""
(★★) Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Independent Set es un problema NP-Completo.
"""

"""
1) Definición del problema de decisión de las N-Reinas:

N-Reinas: Dado un tablero de ajedrez de tamaño NxN, se busca colocar N reinas en el tablero de tal manera que ninguna reina pueda atacar a otra reina en una sola jugada. 
Es decir, no puede haber dos reinas en la misma fila, columna o diagonal. El problema de decisión de las N-Reinas es determinar si es posible colocar N reinas en el tablero 
de ajedrez de tamaño NxN de tal manera que ninguna reina pueda atacar a otra reina en una sola jugada.

2) Reducción de N-Reinas a Independent Set:

Como N-Reinas es NP-Completo, si reducimos N-Reinas <p Independent Set, entonces Independent Set es NP-Completo por transitividad.

Para reducir N-Reinas a Independent Set, se puede realizar la siguiente transformación:

Dado un tablero de ajedrez de tamaño NxN y un número entero k, se busca colocar N reinas en el tablero de tal manera que ninguna reina pueda atacar a otra reina en una sola jugada. 

Se puede transformar este problema a un problema de Independent Set de la siguiente manera:

Se busca un Independent Set de tamaño k en un grafo G. Se construye el grafo G de la siguiente manera: 
- Cada vértice del grafo G representa una casilla del tablero de ajedrez de tamaño NxN.
- Dos vértices están conectados por una arista si las casillas correspondientes en el tablero de ajedrez están en la misma fila, columna o diagonal.

Demostración:
Si es posible colocar N reinas en el tablero de ajedrez de tamaño NxN de tal manera que ninguna reina pueda atacar a otra reina en una sola jugada, entonces existe un 
Independent Set de tamaño k en el grafo G.
Sea D un conjunto de casillas del tablero de ajedrez de tamaño NxN tal que en cada casilla de D se coloca una reina. Entonces, D es un Independent Set de tamaño k en el grafo G.
Si D es un Independent Set, entonces no hay aristas entre las casillas de D. Por lo tanto, no hay reinas que puedan atacarse entre sí en el tablero de ajedrez de tamaño NxN.
Si existe un Independent Set de tamaño k en el grafo G, entonces es posible colocar N reinas en el tablero de ajedrez de tamaño NxN de tal manera que ninguna reina pueda 
atacar a otra reina en una sola jugada. Sea D un Independent Set de tamaño k en el grafo G. Entonces, en cada casilla de D se coloca una reina en el tablero de ajedrez de tamaño NxN.
"""
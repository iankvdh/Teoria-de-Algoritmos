"""
(★) Explicar para cada uno de los siguientes casos, qué modificaciones 
se deben aplicar sobre una red para convertirla en una red de flujo 
apta para la utilización del algoritmo de Ford-Fulkerson.

a. En la red existen bucles.

b. En la red hay ciclos de dos vértices (aristas antiparalelas).

c. En la red hay más de una fuente.

d. En la red hay más de un sumidero.
"""

"""
a) En el caso de que existan bucles en la red, se deben eliminar los mismos, ya que el algoritmo de Ford-Fulkerson
no puede manejarlos. Si hay, eliminamos las aristas que forman el bucle.

b) En el caso de que haya ciclos de dos vértices, se deben eliminar las aristas antiparalelas, ya que el algoritmo
de Ford-Fulkerson no puede manejarlas. Para ello, se debe modificar el grafo de la red, agregando un nuevo vértice 
que conecte el origen del bucle con el destino del mismo, y asignarle un peso igual al del bucle, tanto en la 
entrada del nuevo vertice como en la salida.

c) En el caso de que haya más de una fuente, se debe agregar un nuevo vértice que conecte todas las fuentes, y
asignarle un peso igual a la suma de los pesos de las aristas que conectan las fuentes con el nuevo vértice.

d) En el caso de que haya más de un sumidero, se debe agregar un nuevo vértice que conecte todos los sumideros, y
asignarle un peso igual a la suma de los pesos de las aristas que conectan los sumideros con el nuevo vértice.
"""
"""
(★) ¿Cuál es la relación entre el flujo máximo de una red, y un corte mínimo que separe su fuente y sumidero?
"""

"""
El flujo máximo de una red es igual a la capacidad mínima de un corte mínimo que separe su fuente y sumidero.

*Teorema de flujo máximo y corte mínimo* 

El valor del flujo máximo que puede enviarse desde la fuente hasta el sumidero en una red de flujo es igual 
a la capacidad del corte mínimo que separa la fuente del sumidero.

- Flujo máximo: Es la cantidad máxima de flujo que se puede enviar desde el nodo fuente al nodo sumidero en 
la red, considerando las capacidades de las aristas como limitantes.

- Corte mínimo: Un corte en una red es una partición de los nodos en dos subconjuntos: uno que contiene la fuente 
y otro que contiene el sumidero. La capacidad del corte es la suma de las capacidades de las aristas que van desde 
el subconjunto de la fuente al subconjunto del sumidero. El corte mínimo es el corte cuya capacidad es la más baja 
entre todos los cortes posibles.

- El valor del flujo máximo en una red siempre es igual a la capacidad del corte mínimo.
- Este teorema muestra que para maximizar el flujo de una red, es suficiente encontrar un corte mínimo.
- Proporciona una forma de certificar que se ha encontrado el flujo máximo: si se puede identificar un corte cuyo 
valor de capacidad sea igual al flujo actual, entonces ese flujo es máximo.

Importancia práctica:
El teorema de flujo máximo y corte mínimo es fundamental en optimización de redes y tiene aplicaciones en diversas
áreas, como en logística, telecomunicaciones y diseño de circuitos, donde se busca maximizar el flujo o minimizar
el costo de separaciones o "cuellos de botella" en una red.
"""
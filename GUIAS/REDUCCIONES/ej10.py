"""
Definir los problemas de decisión de Subset Sum y Problema de la Mochila. 
Sabiendo que Subset Sum es NP-Completo, demostrar que el Problema de la Mochila es NP-Completo.
"""

"""
1) Definición del problema de decisión de Subset Sum:

Subset Sum: Dado un conjunto de números enteros S y un número entero k, se busca determinar si existe un subconjunto no vacío de S cuya suma sea igual a k.

2) Definición del problema de decisión del Problema de la Mochila:

Problema de la Mochila: Dado un conjunto de n elementos, cada uno con un peso w_i y un valor v_i, y una capacidad C, se busca determinar si existe un subconjunto de elementos cuyo peso total no exceda C.
"""

def verificador_mochila(solucion, elementos, capacidad):
    """
    Verifica si la solución de la mochila es correcta.
    """
    peso_total = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            peso_total += elementos[i][0]
    return peso_total <= capacidad

"""
3) Reducción de Subset Sum a Problema de la Mochila:

Nosotros buscamos realizar lo siguiente: Subset Sum <=p Problema de la Mochila.

Para reducir Subset Sum a Problema de la Mochila, se puede realizar la siguiente transformación:
Dado un conjunto de números enteros S y un número entero k, se busca determinar si existe un subconjunto no vacío de S cuya suma sea igual a k.
Se puede transformar este problema a un problema del Problema de la Mochila de la siguiente manera:
- Se busca un subconjunto de elementos cuya suma sea igual a k.
- Se construye un conjunto de elementos con los números de S y sus valores iguales a sus pesos.
- Se busca un subconjunto de elementos cuyo peso total no exceda k.
Esta transformación es polinomial, ya que se puede hacer en tiempo polinomial.

4) Demostración:

Si existe un subconjunto no vacío de S cuya suma sea igual a k, entonces existe un subconjunto de elementos cuyo peso total no exceda k.
Sea D un subconjunto no vacío de S tal que la suma de los elementos de D sea igual a k. Entonces, se puede construir un subconjunto de elementos con los números de D y sus valores iguales a sus pesos. Este subconjunto de elementos tiene un peso total igual a k, que no excede k.

Si existe un subconjunto de elementos cuyo peso total no exceda k, entonces existe un subconjunto no vacío de S cuya suma sea igual a k.
Sea D un subconjunto de elementos tal que el peso total de D no exceda k. Entonces, se puede construir un subconjunto no vacío de S con los números de D. La suma de los elementos de S es igual al peso total de D, que no excede k.

Por lo tanto, se puede reducir Subset Sum a Problema de la Mochila.

Por lo tanto, como Subset Sum es NP-Completo, entonces el Problema de la Mochila también es NP-Completo por transitividad.
"""
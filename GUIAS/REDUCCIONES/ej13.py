"""
(★★) Realizar una reducción polinomial del siguiente problema a otro de los vistos durante la cursada. 
Ayuda: pensar en alguno de los vistos de programación dinámica. 
Dada esta reducción, ¿se puede afirmar que este problema es NP-Completo?
Dado un número n, encontrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados.
"""

"""
1) Definición del problema de decisión de Suma de Cuadrados:
Suma de Cuadrados: Dado un número n, se busca encontrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados.

2) Definición del problema de decisión de Problema del cambio de monedas:
Problema del cambio de monedas: Dado un conjunto de monedas con valores enteros positivos y un valor entero positivo n, se busca determinar si es posible formar n con las monedas dadas de la forma más económica (con menos monedas).
"""

def verificador_monedas(sistema, cambio, monedas_usadas):
    """
    Verifica si el cambio es correcto.
    """
    suma = 0
    for i in range(len(monedas_usadas)):
        if monedas_usadas[i] not in sistema:
            return False
        suma += monedas_usadas[i]
    return suma == cambio

"""
3) Reducción de Suma de Cuadrados a Problema del cambio de monedas:

Para reducir Suma de Cuadrados a Problema del cambio de monedas, se puede realizar la siguiente transformación:
Dado un número n, se busca encontrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados.
Se puede transformar este problema a un problema del Problema del cambio de monedas de la siguiente manera:
- Se busca encontrar la cantidad más económica (con menos términos) de escribir n como una suma de cuadrados.
- Se construye un conjunto de monedas con los cuadrados de los números enteros.
- Se busca encontrar la cantidad más económica (con menos términos) de escribir n como una suma de monedas.
Esta transformación es polinomial, ya que se puede hacer en tiempo polinomial.

Demostración:

Si existe una cantidad más económica (con menos términos) de escribir n como una suma de cuadrados, entonces existe una cantidad más económica (con menos términos) de escribir n como una suma de monedas. Sea D una cantidad más económica (con menos términos) de escribir n como una suma de cuadrados. Entonces, se puede construir un conjunto de monedas con los cuadrados de los números enteros. Este conjunto de monedas tiene una cantidad más económica (con menos términos) de escribir n como una suma de monedas.

Si existe una cantidad más económica (con menos términos) de escribir n como una suma de monedas, entonces existe una cantidad más económica (con menos términos) de escribir n como una suma de cuadrados. Sea D una cantidad más económica (con menos términos) de escribir n como una suma de monedas. Entonces, se puede construir una cantidad más económica (con menos términos) de escribir n como una suma de cuadrados con los cuadrados de los números enteros.

Por lo tanto, se puede reducir Suma de Cuadrados a Problema del cambio de monedas.

Ahora bien, existe un algoritmo eficiente basado en programación dinámica que resuelve el problema en tiempo polinómico cuando las denominaciones de las monedas son pequeñas.

Entonces... es NP-Completo?


"""

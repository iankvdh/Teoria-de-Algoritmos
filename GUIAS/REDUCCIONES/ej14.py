"""
(★★) En su tiempo libre, Carlitos colecciona figuritas del mundial. 
Incluso a más de un año de la coronación de gloria, hay mucho entusiasmo por estas. Llegó a coleccionar 
tantas que ahora se dedica a revenderlas (para sacar unos pesos extra de su trabajo principal como publicista). 
Tiene tantas figuritas que ya no revende al público directamente, sino a otros revendedores y cadenas de kioscos.
En general, cuando le piden, le pide un lote de figuritas “por una cantidad determinada de dinero”. 
Cada tipo de figurita tiene un valor diferente (es decir, la de Messi no vale lo mismo que la del Bobo Weghorst). 
Podemos decir que absolutamente todos los tipos de figuritas tienen valores diferentes, todos valores enteros, 
y que Carlitos cuenta con una cantidad ridículamente alta de cada una de ellas. Por un análisis que hizo, 
sabe que si le piden figuritas por un determinado monto, le conviene dar la menor cantidad de figuritas posibles 
(siempre cumpliendo con el monto exacto pedido), incluso repitiendo figuritas en caso de ser necesario. 
El problema de las figuritas de Carlitos dice: dados los valores de los diferentes tipos de figuritas y un monto 
al que llegar, determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto dando la 
mínima cantidad de figuritas para ello. Asumir todos valores enteros, y que hay figurita de valor 1. 

Por otro lado, recordemos que el Problema de Subset Sum es NP-Completo. 
Redefinir ambos problemas en sus versiones de problema de decisión, y realizar una reducción polinomial de uno a otro. 
¿Podemos con esta reducción afirmar que el problema de Carlitos es NP-Completo?
"""

"""
1) Definición del problema de decisión de Subset Sum:

Subset Sum: Dado un conjunto de números enteros S y un número entero k, se busca determinar si existe un subconjunto no vacío de S cuya suma sea igual a k.

2) Definición del problema de decisión del Problema de las Figuritas de Carlitos:

Problema de las Figuritas de Carlitos: Dados los valores de los diferentes tipos de figuritas y un monto al que llegar, determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto dando la mínima cantidad de figuritas para ello.
"""

def verificador_carlitos(solucion, valores, monto):
    """
    Verifica si la solución de Carlitos es correcta.
    """
    suma = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            suma += valores[i]
    return suma == monto

"""
3) Sabemos que Subset Sum es NP-Completo. Por lo tanto, vamos a intentar reducir Subset Sum a Problema de las Figuritas de Carlitos.
Si logramos dicha reducción, entonces podremos afirmar que el problema de Carlitos es NP-Completo por transitividad.

Subset Sum <=p Problema de las Figuritas de Carlitos:

Para reducir Subset Sum a Problema de las Figuritas de Carlitos se puede realizar la siguiente transformación:
Dado un conjunto de números enteros S y un número entero k, se busca determinar si existe un subconjunto no vacío de S cuya suma sea igual a k.
Se puede transformar este problema a un problema del Problema de las Figuritas de Carlitos de la siguiente manera:
- Se busca determinar si existe un subconjunto no vacío de S cuya suma sea igual a k.
- Se construye un conjunto de valores con los números de S.
- Se busca determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto dando la mínima cantidad de figuritas para ello.
Esta transformación es polinomial, ya que se puede hacer en tiempo polinomial.

4) Demostración:

Si existe un subconjunto no vacío de S cuya suma sea igual a k, entonces existe un conjunto de figuritas de Carlitos cuya suma sea igual a k.
Sea D un subconjunto no vacío de S tal que la suma de los elementos de D sea igual a k. Entonces, se puede construir un conjunto de figuritas de Carlitos con los valores de D. Este conjunto de figuritas tiene una suma igual a k.

Si existe un conjunto de figuritas de Carlitos cuya suma sea igual a k, entonces existe un subconjunto no vacío de S cuya suma sea igual a k.
Sea D un conjunto de figuritas de Carlitos tal que la suma de los valores de D sea igual a k. Entonces, se puede construir un subconjunto no vacío de S con los valores de D. La suma de los elementos de S es igual a la suma de los valores de D.

Por lo tanto, se puede reducir Subset Sum a Problema de las Figuritas de Carlitos.

Por lo tanto, el problema de las Figuritas de Carlitos es NP-Completo por transitividad.
"""
# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. 
# Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. 
# El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, 
# y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
# Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? 
# Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar

# Algoritmo Greedy:
# Ordenar el sistema monetario de mayor a menor.
# Iterar sobre el sistema monetario.
# Si el valor actual es menor o igual al cambio restante, agregarlo al resultado.
# Restar al cambio restante el valor actual.
# Repetir hasta que no quede más cambio.

def cambio(monedas, monto):
    sistema = sorted(monedas)[::-1]
    cambio = []
    for tipo_cambio in sistema:
        if monto == 0:
            break
        cantidad = monto // tipo_cambio
        monto -= cantidad * tipo_cambio
        cambio.extend([tipo_cambio] * cantidad)
    return cambio

"""
Es un algoritmo Greedy porque en cada paso buscamos el optimo local con el fin de llegar a un optimo global.
En cada paso, seleccionamos la moneda de mayor valor que sea menor o igual al cambio restante, maximizando la cantidad
de monedas de mayor valor que se pueden utilizar. De esta forma, garantizamos que la cantidad de monedas utilizadas sea
mínima. 
Si, es un algoritmo óptimo, ya que selecciona la menor cantidad de monedas posibles, y no existe una solución mejor que
seleccionar la menor cantidad de monedas posibles.
Complejidad: O(n log n) por el ordenamiento.
"""
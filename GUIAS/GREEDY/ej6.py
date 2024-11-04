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
# Complejidad: O(n log n) por la cota superior del ordenamiento.

def cambio(monto, sistema_monetario):
    sistema = sorted(sistema_monetario)[::-1]
    cambio = {}
    for tipo_cambio in sistema:
        dividendo = monto//tipo_cambio
        monto = monto % tipo_cambio 
        cambio[tipo_cambio] = dividendo  
    return cambio

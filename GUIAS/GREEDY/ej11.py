# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, 
# por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos 
# de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad 
# posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y 
# para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? 
# Justificar. Indicar y justificar la complejidad del algoritmo implementado.

def bolsas(capacidad, productos):
    elementos_ordenados = sorted(productos)
    bolsa_con_productos = []
    bolsas = []

    for peso in elementos_ordenados:
        if peso > capacidad:
            continue
        elif sum(bolsa_con_productos) + peso <= capacidad:
            bolsa_con_productos.append(peso)
        else:
            bolsas.append(bolsa_con_productos)
            bolsa_con_productos = [peso]

    if bolsa_con_productos:
        bolsas.append(bolsa_con_productos)

    return bolsas

capacidad = 5
productos = [4, 2, 1, 3, 5]
print(bolsas(capacidad, productos))

# El algoritmo implementado no encuentra siempre la solución óptima.
# Por ejemplo, si la capacidad de la bolsa es 5 y los productos son [4, 2, 1, 3, 5], el algoritmo
# devolverá [[1, 2], [3], [4], [5]], cuando la solución óptima sería [[5], [4, 1], [3, 2]].
# La complejidad del algoritmo es O(n log n) debido a la ordenación de los productos.

# Es greedy porque en cada paso elige el producto más pequeño que pueda meter en la bolsa, buscando 
# la solución óptima local en cada paso. Sin embargo, no garantiza la solución óptima global. Se puede
# demostrar que este algoritmo no siempre encuentra la solución óptima con el contraejemplo mencionado.
# Se podría razon de forma contraria, ordenando los productos de mayor a menor, pero tampoco se garantiza
# que se encuentre la solución óptima.
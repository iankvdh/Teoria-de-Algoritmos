# Tenemos unos productos dados por un arreglo, donde R[i] nos dice el precio del producto. 
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación 
# y los precios aumentan todo el tiempo. El precio del producto i el día j es (R[i])j+1 (j comenzando en 0). 
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
# Indicar y justificar la complejidad del algoritmo implementado. 
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
# ¿Por qué se trata de un algoritmo Greedy? Justificar 
# ¿Qué modificaciones se deben realizar para un estado de deflación, con productos que bajan de precio todo el tiempo?

# Algoritmo Greedy:
# Ordenar los productos por precio (de mayor a menor).
# Iterar sobre los productos.
# Sumar el precio del producto actual al total.
# Repetir hasta que no queden más productos.

# Complejidad: O(n log n) por el ordenamiento.

def precio_minimo(productos):
    productos.sort(reverse=True)
    precio = 0
    for i, producto in enumerate(productos):
        precio += producto * (i + 1)
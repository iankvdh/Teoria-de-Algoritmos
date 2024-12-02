# Tenemos unos productos dados por un arreglo, donde R[i] nos dice el precio del producto. 
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación 
# y los precios aumentan todo el tiempo. El precio del producto i el día j es (R[i])^j+1 (j comenzando en 0). 
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

def precio_inflacion(R):
    R.sort(reverse=True)
    precio = 0
    print(R)
    for i, producto in enumerate(R):
        precio += producto ** (i + 1)
    return precio

"""
Es un algoritmo Greedy porque en cada paso buscamos el optimo local con el fin de llegar a un optimo global.
En cada paso, seleccionamos el producto de mayor precio, minimizando el precio total de los productos comprados.
De esta forma, garantizamos que el precio total sea mínimo. Si compramos los productos de menor precio primero,
el precio de un producto de mayor precio aumentará, y el precio total será mayor. Por lo tanto, seleccionar los
productos de mayor precio primero minimiza el precio total.
Si, es un algoritmo óptimo, ya que selecciona los productos de mayor precio primero, minimizando el precio total.
No existe una solución mejor que seleccionar los productos de mayor precio primero.
Complejidad: O(n log n) por el ordenamiento.
"""

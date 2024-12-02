"""
En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una 
era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente 
la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. Si bien para 
reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten 
esperar, y cada día debemos comprar uno de los productos.
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar
"""

# Algoritmo Greedy:
# Ordenar los productos por precio (de menor a mayor).
# Iterar sobre los productos.
# Sumar el precio del producto actual al total.
# Repetir hasta que no queden más productos.

def precio_deflacion(R):
    R.sort()
    precio = 0
    for i, producto in enumerate(R):
        # El precio del producto i el día j+1 es exactamente la mitad del precio en el día j.
        producto = producto / (2 ** i)
        precio += producto
    return precio

"""
Es un algoritmo Greedy porque en cada paso buscamos el optimo local con el fin de llegar a un optimo global.
En cada paso, seleccionamos el producto de menor precio, minimizando el precio total de los productos comprados.
De esta forma, garantizamos que el precio total sea mínimo. Al "aprovechar" la espera de la deflación, 
seleccionamos los productos de menor precio primero, "esperando" a que los productos de mayor precio disminuyan.
Si, es un algoritmo óptimo, ya que selecciona los productos de menor precio primero, minimizando el precio total.
No existe una solución mejor que seleccionar los productos de menor precio primero.
Complejidad: O(n log n) por el ordenamiento.
"""
"""
(★) Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad.

a. Dado un número por parámetro, si es la solución al problema de Búsqueda del máximo en un arreglo 
b. Dado un arreglo, si es la solución a tener el arreglo ordenado 
c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos N-reinas en un tablero NxN
"""

"""
a. Dado un número por parámetro, si es la solución al problema de Búsqueda del máximo en un arreglo
"""

def verificador_maximo(arr, n):
    # Complejidad: O(n)
    return n == max(arr)

"""
b. Dado un arreglo, si es la solución a tener el arreglo ordenado
"""

def verificador_ordenado(arr):
    # Complejidad: O(n log n)
    return arr == sorted(arr)

"""
c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos N-reinas en un tablero NxN
"""

def verificador_reinas(arr, n):
    # Complejidad: O(n)
    return len(arr) >= n

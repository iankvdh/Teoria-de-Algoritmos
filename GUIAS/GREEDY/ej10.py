# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. 
# El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. 
# Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de tal forma que no haya 
# bifurcaciones con vigilancia a más de 50 km. Justificar que la solución es óptima. 
# Indicar y justificar la complejidad del algoritmo implementado. 

# Ejemplo:
    # Ciudad	Bifurcación (km)

    # Castelli	        185
    # Gral Guido	    242
    # Lezama	        156
    # Maipú	            270
    # Sevigne	        194

# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. 
# Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. 
# Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.

# En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la
# única solución óptima sería colocar un móvil policial en Sevigne.

# Algoritmo Greedy:
# Iterar sobre las bifurcaciones.
# Si la distancia entre la bifurcación actual y la anterior es mayor a 50, colocar un móvil policial.
# Repetir hasta que no queden más bifurcaciones.

# Complejidad: O(n) donde n es la cantidad de bifurcaciones.

def patrullas(ciudades):
    ciudades_ordenadas = sorted(ciudades, key=lambda x: x[1])
    solucion = []

    rango_max = float('-inf')
    ultima_estacion = float('-inf')

    for index, ciudad in enumerate(ciudades_ordenadas):
        if ciudad[1] < rango_max or ciudad[1] < ultima_estacion + 50:
            continue

        if rango_max == float('-inf'):
            rango_max = ciudad[1] + 50
        elif ciudad[1] > rango_max:
            solucion.append(ciudades_ordenadas[index - 1])
            ultima_estacion = ciudades_ordenadas[index - 1][1]
            rango_max = float('-inf')

    if ciudades_ordenadas:
        ultima_estacion = ciudades_ordenadas[-1]
        if ultima_estacion[1] > ultima_estacion + 50:
            solucion.append(ultima_estacion)

    return solucion
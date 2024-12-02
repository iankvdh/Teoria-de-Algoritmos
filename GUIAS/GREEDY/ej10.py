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


def patrullas(ciudades):
    if len(ciudades) == 0:
        return []
    ciudades_ord = sorted(ciudades, key=lambda x: x[1])
    res = []
    i = 0
    n = len(ciudades_ord)
    while i < n:
        patrulla_abarca = ciudades_ord[i][1] + 50
        while i < n and ciudades_ord[i][1] <= patrulla_abarca:
            i += 1
        res.append(ciudades_ord[i - 1])
        while i < n and ciudades_ord[i][1] <= res[-1][1] + 50:
            i += 1
    return res

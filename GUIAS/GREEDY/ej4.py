# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, 
# representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, 
# e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
# Indicar y justificar la complejidad del algoritmo implementado.

# Algoritmo Greedy:
# Ordenar las charlas por horario de fin.
# Tomar la primera charla.
# Iterar sobre las charlas restantes.
# Si la charla actual comienza después de la charla seleccionada, seleccionarla.
# Repetir hasta que no queden más charlas.

def charlas_a_dar(charlas):
    if len(charlas) == 0:
        return []
    charlas.sort(key=lambda x: x[1])
    charlas_a_dar = [charlas[0]]
    for charla in charlas[1:]:
        if charla[0] >= charlas_a_dar[-1][1]:
            charlas_a_dar.append(charla)
    return charlas_a_dar

"""
Es un algortimo Greedy porque en cada paso buscamos el optimo local con el fin de llegar a un optimo global.
En cada paso, seleccionamos la charla que termina antes, y luego seleccionamos la charla que comienza después 
de la charla seleccionada. De esta forma, garantizamos que la cantidad de charlas seleccionadas sea máxima.
Si, es un algoritmo óptimo, ya que selecciona la mayor cantidad de charlas posibles, y no existe una solución
mejor que seleccionar la mayor cantidad de charlas posibles.
Complejidad: O(n log n) por el ordenamiento.
"""
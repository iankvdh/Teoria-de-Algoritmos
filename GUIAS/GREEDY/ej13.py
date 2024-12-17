"""
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas
vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el 
sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango 
de cobertura de R kilómetros (valor constante conocido). 
Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre 
esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos 
construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor 
cantidad de antenas posibles. 
 
Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué se trata de un algoritmo greedy. 
¿El algoritmo da la solución óptima siempre?
"""

def cobertura(casas, R, K):
    if not casas:
        return []
    casas.sort()
    antenas = []
    if casas[0] > K:
        # si la casa esta fuera de la ruta return
        return []
    # agrego la primera antena dentro del rango de la ruta
    antenas.append(casas[0]+R if casas[0]+R <= K else K)
    for casa in casas:
        if casa > antenas[-1] + R:
            pos_antena = min(casa + R, K)
            antenas.append(pos_antena)
    return antenas

"""
Es un algoritmo greedy ya que en cada paso se toma la mejor decisión local, es decir, se coloca la antena
en la posición más óptima en ese momento. Además, la solución óptima global se obtiene a partir de las
soluciones óptimas locales. Al colocar la antena en la posición más alejada posible, se minimiza la cantidad
de antenas a colocar.
La complejidad del algoritmo es O(n log n) ya que se ordena la lista de casas.
"""

# "Solución de Ian Von der Heyde"
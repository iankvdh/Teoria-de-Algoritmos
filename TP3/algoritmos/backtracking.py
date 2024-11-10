from auxiliares import *

"""
Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema (valga la redundancia) en la versión de optimización: 
Dado un tablero de n*m casilleros, y una lista de k barcos (donde el barco i tiene b_i de largo) una lista de las demandas de las n filas 
y una lista de las m demandas de las columnas, dar la asignación de posiciones de los barcos de tal forma que se reduzca al mínimo la 
cantidad de demanda incumplida. Pueden no utilizarse todos los barcos. Si simplemente no se cumple que una columna que debería tene 3 
casilleros ocupados tiene 1, entonces contará como 2 de demanda incumplida. Por el contrario, no está permitido exceder la cantidad demandada. 
Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.
"""

def bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos):
    mejor_solucion = {
        "demanda_incumplida": float('inf'),
        "tablero": None
    }
    _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, 0, 0, mejor_solucion)
    return mejor_solucion["tablero"]

def _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, i, j, mejor_solucion):
    n = len(tablero)
    m = len(tablero[0])

    if i == n:
        demanda_incumplida = calcular_demanda_incumplida(tablero, restricciones_filas, restricciones_columnas)
        if demanda_incumplida < mejor_solucion["demanda_incumplida"]:
            mejor_solucion["demanda_incumplida"] = demanda_incumplida
            mejor_solucion["tablero"] = [fila.copy() for fila in tablero]
        return

    if j == m:
        _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, i + 1, 0, mejor_solucion)
        return

    if sum(tablero[i]) == restricciones_filas[i]:
        _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, i + 1, 0, mejor_solucion)
        return

    if sum(tablero[fila][j] for fila in range(n)) == restricciones_columnas[j]:
        _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, i, j + 1, mejor_solucion)
        return

    for barco in barcos:
        if j + barco <= m:
            barco_cabe = all(tablero[i][j + k] == 0 for k in range(barco))
            if barco_cabe:
                for k in range(barco):
                    tablero[i][j + k] = BARCO
                if es_compatible(tablero, restricciones_filas, restricciones_columnas, i, j, barco, HORIZONTAL):
                    barcos_restantes = barcos.copy()
                    barcos_restantes.remove(barco)
                    _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos_restantes, i, j + barco, mejor_solucion)
                for k in range(barco):
                    tablero[i][j + k] = 0

        elif i + barco <= n:
            barco_cabe = all(tablero[i + k][j] == 0 for k in range(barco))
            if barco_cabe:
                for k in range(barco):
                    tablero[i + k][j] = BARCO
                if es_compatible(tablero, restricciones_filas, restricciones_columnas, i, j, barco, VERTICAL):
                    barcos_restantes = barcos.copy()
                    barcos_restantes.remove(barco)
                    _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos_restantes, i, j + 1, mejor_solucion)
                for k in range(barco):
                    tablero[i + k][j] = 0

    _bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos, i, j + 1, mejor_solucion)


"""
# Ejemplo de uso
n = 3
m = 3
restricciones_filas = [3, 1, 2]
restricciones_columnas = [3, 2, 0]
barcos = [2, 2]


tablero = [[0] * m for _ in range(n)]
solucion = bt_batalla_naval(tablero, restricciones_filas, restricciones_columnas, barcos)
for fila in solucion:
    print(fila)
print("Demanda incumplida:", calcular_demanda_incumplida(solucion, restricciones_filas, restricciones_columnas))
"""
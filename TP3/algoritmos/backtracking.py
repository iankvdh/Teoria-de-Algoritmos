from algoritmos.leer_archivos import leer_inputs, leer_resultados_esperados

class Batalla_Naval:
    tablero = None
    mejor_tablero = None
    vacio = "-"
    maxima_demanda_cumplida = 0  
    n = 0
    m = 0
    
    def __init__(self, restricciones_filas, restricciones_columnas, barcos):
        self.n = len(restricciones_filas)
        self.m = len(restricciones_columnas)
        self.restricciones_filas = restricciones_filas[:]
        self.restricciones_columnas = restricciones_columnas[:]
        self.demanda_restante_filas = restricciones_filas[:]  
        self.demanda_restante_columnas = restricciones_columnas[:]  
        self.barcos = sorted(barcos, reverse=True)
        self.tablero = [[self.vacio for _ in range(self.m)] for _ in range(self.n)]
        self.mejor_tablero = [[self.vacio for _ in range(self.m)] for _ in range(self.n)]
        self.bloques_disponibles = {(i, j) for i in range(self.n) for j in range(self.m)}
        self.backtracking(0, 0)

    def backtracking(self, indice, demanda_cumplida_actual):

        if demanda_cumplida_actual + sum(self.barcos[indice:]) * 2 <= self.maxima_demanda_cumplida:
            return
        
        if indice == len(self.barcos):
            if demanda_cumplida_actual > self.maxima_demanda_cumplida:
                self.maxima_demanda_cumplida = demanda_cumplida_actual
                self.mejor_tablero = [fila[:] for fila in self.tablero]
            return
        
        largo = self.barcos[indice]
        bloques_vacios = self.get_bloques_disponibles()

        for fila, col in bloques_vacios:
            for orientacion in (0, 1):
                if self.entra_en_el_tablero(fila, col, largo, orientacion) and not self.exede_demanda(fila, col, largo, orientacion):
                    if not self.tiene_adyacentes(fila, col, largo, orientacion):
                        self.colocar_barco(fila, col, orientacion, largo, str(indice))
                        demanda_cumplida = self.contar_demanda_cumplida_de_barco(largo)
                        self.backtracking(indice + 1, demanda_cumplida_actual + demanda_cumplida)
                        self.quitar_barco(fila, col, largo, orientacion)
        
        if demanda_cumplida_actual + sum(self.barcos[indice:]) * 2 > self.maxima_demanda_cumplida:
            self.backtracking(indice + 1, demanda_cumplida_actual)


    def entra_en_el_tablero(self, fila, col, largo, orientacion):
        try:
            if orientacion == 0:  # Horizontal
                return all(self.tablero[fila][j] == self.vacio for j in range(col, col + largo))
            else:  # Vertical
                return all(self.tablero[i][col] == self.vacio for i in range(fila, fila + largo))
        except IndexError:
            return False

    def exede_demanda(self, fila, col, largo, orientacion):
        if orientacion == 0:  # Horizontal
            if self.demanda_restante_filas[fila] < largo:
                return True
            if any(self.demanda_restante_columnas[j] < 1 for j in range(col, col + largo)):
                return True
        else:  # Vertical
            if self.demanda_restante_columnas[col] < largo:
                return True
            if any(self.demanda_restante_filas[i] < 1 for i in range(fila, fila + largo)):
                return True
        return False

    def contar_demanda_cumplida_de_barco(self, largo):
        return largo*2

    def tiene_adyacentes(self, fila, col, largo, orientacion):
        if orientacion == 0:  # Horizontal
            for j in range(col - 1, col + largo + 1):
                if not (0 <= j < self.m):
                    continue
                for i in [fila - 1, fila, fila + 1]:
                    if 0 <= i < self.n and self.tablero[i][j] != self.vacio:
                        return True
        else:  # Vertical
            for i in range(fila - 1, fila + largo + 1):
                if not (0 <= i < self.n):
                    continue
                for j in [col - 1, col, col + 1]:
                    if 0 <= j < self.m and self.tablero[i][j] != self.vacio:
                        return True
        return False

    def colocar_barco(self, fila, col, orientacion, largo, ship_indice):
        if orientacion == 0:  # Horizontal
            for j in range(col, col + largo):
                self.tablero[fila][j] = ship_indice
                self.demanda_restante_columnas[j] -= 1
            self.demanda_restante_filas[fila] -= largo
        else:  # Vertical
            for i in range(fila, fila + largo):
                self.tablero[i][col] = ship_indice
                self.demanda_restante_filas[i] -= 1
            self.demanda_restante_columnas[col] -= largo
    

    def quitar_barco(self, fila, col, largo, orientacion):
        if orientacion == 0:  # Horizontal
            for j in range(col, col + largo):
                self.tablero[fila][j] = self.vacio
                self.demanda_restante_columnas[j] += 1
            self.demanda_restante_filas[fila] += largo
        else:  # Vertical
            for i in range(fila, fila + largo):
                self.tablero[i][col] = self.vacio
                self.demanda_restante_filas[i] += 1
            self.demanda_restante_columnas[col] += largo

    def get_bloques_disponibles(self):
        bloques_vacios = []
        for i in range(self.n):
            for j in range(self.m):
                if self.tablero[i][j] == self.vacio and not self.tiene_adyacentes(i, j, 1, 0): 
                    bloques_vacios.append((i, j))
        return bloques_vacios
    
    def print_solution(self):
        restricciones_columnas = [" ", " "] + [str(c) + " " for c in self.restricciones_columnas]
        print(''.join(restricciones_columnas))
        for i in range(self.n):
            fila_str = [str(self.restricciones_filas[i]) + " "] + [self.mejor_tablero[i][j] + " " for j in range(self.m)]
            print(''.join(fila_str))
        print()
    
    def print_posiciones_barcos(self):
        # a partir del mejor_tablero, obtener las posiciones de los barcos, cada numero corresponde al barco en la posicion i
        posiciones_barcos = [[] for _ in range(len(self.barcos))]
        for i in range(self.n):
            for j in range(self.m):
                if self.mejor_tablero[i][j] != self.vacio:
                    posiciones_barcos[int(self.mejor_tablero[i][j])].append((i, j))
        for i in range(len(posiciones_barcos)):
            if len(posiciones_barcos[i]) <= 0:
                posiciones_barcos[i] = None
        
        for i, pos in enumerate(posiciones_barcos):
            if pos is None:
                print(f"Barco {i}: None")
            elif len(pos) == 1:
                print(f"Barco {i}: ({pos[0][0]}, {pos[0][1]})")
            else:
                print(f"Barco {i}: ({pos[0][0]}, {pos[0][1]}) - ({pos[-1][0]}, {pos[-1][1]})")
    

    def get_best_grid(self):
        return self.mejor_tablero

    def get_optimal_demand(self):
        return self.maxima_demanda_cumplida
    
def mostrar_resultados_ruta_abs_bt(ruta_absoluta):
    demandas_filas, demandas_columnas, barcos = leer_inputs(ruta_absoluta)
    batalla_naval = Batalla_Naval(demandas_filas, demandas_columnas, barcos)
    print(" --------------- Resultados --------------- ")
    print("Tablero:")
    batalla_naval.print_solution()
    print("Demanda cumplida:", batalla_naval.get_optimal_demand())
    print("Demanda total: ", sum(demandas_filas) + sum(demandas_columnas))
    print("Posiciones de los barcos:")
    batalla_naval.print_posiciones_barcos()
    print(" ------------------------------------------ ")

from src.auxiliares import leer_numeros_desde_txt
import os
import sys

# python3 main.py ~/TDA/TDA-FIUBA-75.29/TP2/data/5.txt

"""
1) Si Sophia elige la primer moneda (coins[i]):
    option1= {
            coins[i]+dp[i+2][j], si coins[i+1]≥coins[j]
            coins[i]+dp[i+1][j-1], si no 
             }
2) Si Sophia elige la ultima moneda (coins[j]):
    option2 = {
            coins[j]+dp[i+1][j-1], si coins[i]≥coins[j-1]
            coins[j]+dp[i][j-2], si no
              }

OPT[i][j] = max(option1,option2)
"""


def jugar(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]
    # Llenar la tabla dp como en el algoritmo original
    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if not i + 2 <= j:
                dp[i][j] = max(coins[i], coins[j])
                continue
            if coins[i+1] >= coins[j]:
                option1 = coins[i] + (dp[i+2][j])
            else:
                option1 = coins[i] + (dp[i+1][j-1])

            if coins[i] >= coins[j-1]:
                option2 = coins[j] + (dp[i+1][j-1])
            else:
                option2 = coins[j] + (dp[i][j-2])
            dp[i][j] = max(option1, option2)
    return dp 


def reconstruir_monedas_tomadas_por_sophia(coins, dp):
    i, j = 0, len(coins) - 1
    monedas_sophia = []
    turno = 0
    
    while i <= j:
            # Si esta en las primeras 2 diagonales (casos base) Sophia elige la moneda mas grande
            if not i + 2 <= j:
                option1 = coins[i]
            # Sino Sophia elige segun la ecuacion de recurrencia
            else:
                if coins[i+1] >= coins[j]:
                    option1 = coins[i] + (dp[i+2][j])
                else:
                    option1 = coins[i] + (dp[i+1][j-1])
            # Verificar si la matriz de optimos coincede con la opcion 1. En caso contrario coincide con la opcion 2
            if dp[i][j] == option1:
                monedas_sophia.append(coins[i])
                turno += 1
                if coins[i+1] >= coins[j]:
                    # Mateo tomaría la moneda en coins[i+1]
                    i += 2  
                else:
                    # Mateo tomaría la moneda en coins[j]
                    i += 1
                    j -= 1 
            else:
                monedas_sophia.append(coins[j])
                if coins[i] >= coins[j-1]:
                    # Mateo tomaría la moneda en coins[i]
                    i += 1
                    j -= 1  
                else:
                    # Mateo tomaría la moneda en coins[j-1]
                    j -= 2
    return monedas_sophia


def rec_to_str(rec, coins):
    n = len(coins)
    rec_str = ["" * n for _ in range(n)] 
    i, j = 0, len(coins) - 1
    turno = 0
    indice_rec_sophia = 0
    puntos_sophia = 0
    puntos_mateo = 0

    while i <= j:
        if turno % 2 == 0:
            if rec[indice_rec_sophia] == coins[i]:
                rec_str[turno] = (f"Sophia debe agarrar la primera ({coins[i]})")
                puntos_sophia += coins[i]
                i += 1
            else:
                rec_str[turno] = (f"Sophia debe agarrar la ultima ({coins[j]})")
                puntos_sophia += coins[j]
                j -= 1
            indice_rec_sophia += 1
        else:  
            if coins[i] > coins[j]:
                rec_str[turno] = (f"Mateo agarra la primera ({coins[i]})")
                puntos_mateo += coins[i] 
                i += 1
            else:
                rec_str[turno] = (f"Mateo agarra la ultima ({coins[j]})")
                puntos_mateo += coins[j] 
                j -= 1
        turno += 1
    return rec_str, puntos_sophia, puntos_mateo

def cargar_set_datos(ruta_archivo_abs):
    try:
        if os.path.isabs(ruta_archivo_abs):
            coins = leer_numeros_desde_txt(ruta_archivo_abs)
            dp_table = jugar(coins)

            monedas_sophia = reconstruir_monedas_tomadas_por_sophia(coins, dp_table)
            
            rec_str, puntos_sophia, puntos_mateo = rec_to_str(monedas_sophia, coins)
            print("\n".join(rec_str))
            #print("monedas_sophia: ", monedas_sophia)
            print("Ganancia Sophia: ", puntos_sophia)
            print("Ganancia Mateo: ", puntos_mateo)
        else:
            print("La ruta no es absoluta.")
    except Exception as e:
        print("Error al cargar el archivo: ", e)









class Ejemplo():
    def __init__(self):
        self.tamanio = -1
        self.movimientos = ""
        self.ganancia_sofia = -1
        self.ganancia_mateo = -1
    def guardar_tamanio(self, tamanio):
        self.tamanio = tamanio
    def guardar_movimientos(self, movimientos):
        self.movimientos = movimientos
    def guardar_ganancia_sofia(self, ganancia_sofia):
        self.ganancia_sofia = ganancia_sofia
    def guardar_ganancia_mateo(self, ganancia_mateo):
        self.ganancia_mateo = ganancia_mateo
    def __str__(self):
        return f"tamanio: {self.tamanio}, movimientos: {self.movimientos}, ganancia_sofia: {self.ganancia_sofia}, ganancia_mateo: {self.ganancia_mateo}"


def test_all():
    ejemplos = []
    ej = Ejemplo()
    with open("src/Resultados Esperados.txt") as f:
        for linea in f.readlines():
            if ".txt" in linea:
                ej.guardar_tamanio(int(linea.split(".")[0]))
            elif ";" in linea:
                ej.guardar_movimientos(linea)
            elif "Ganancia Sophia" in linea:
                ej.guardar_ganancia_sofia(int(linea.split(" ")[-1]))
            elif "Ganancia Mateo" in linea:
                ej.guardar_ganancia_mateo(int(linea.split(" ")[-1]))
                ejemplos.append(ej)
                ej = Ejemplo()

    for ej in ejemplos:
        print(f"*****TESTING {ej.tamanio}.txt*****")
        print("TEST GANANCIAS")                        
        dp_table = jugar(leer_numeros_desde_txt(f"{ej.tamanio}.txt"))
        coins= leer_numeros_desde_txt(f"{ej.tamanio}.txt")
        monedas_sophia = reconstruir_monedas_tomadas_por_sophia(coins, dp_table)
        res, puntos_sophia, puntos_mateo = rec_to_str(monedas_sophia, coins)
        

        ganancia_sofia_obtenida = dp_table[0][-1]
        ganancia_mateo_obtenida = sum(leer_numeros_desde_txt(f"{ej.tamanio}.txt")) - ganancia_sofia_obtenida
        print(f"{ej.tamanio}.txt: {ej.ganancia_sofia} {ej.ganancia_mateo}", end=" ")
        assert ganancia_sofia_obtenida == ej.ganancia_sofia, f"{ganancia_sofia_obtenida} != {ej.ganancia_sofia}"
        assert ganancia_mateo_obtenida == ej.ganancia_mateo, f"{ganancia_mateo_obtenida} != {ej.ganancia_mateo}"
        print("\033[92mTODO OK\033[0m")

        print("TEST MOVIMIENTOS")
        movimientos_esperados = ej.movimientos.split("; ")
        
        fallo = False
        for i, mov in enumerate(movimientos_esperados):
            if mov.rstrip() != res[i].rstrip():
                if i == len(movimientos_esperados) - 1:
                    if mov.split(" ")[-1].rstrip() == res[i].split(" ")[-1].rstrip():
                        continue
                print(f"\033[91mERROR\033[0m en linea {i}")
                print(f"{mov.rstrip()} != {res[i].rstrip()}")
                fallo = True
                break
        if not fallo:
            print("\033[92mTODO OK\033[0m")
        print("")










def chequeo(linea):
    movimientos = linea.split(";")
    sofia = 0
    mateo = 0
    for mov in movimientos:
        if "Sophia" in mov:
            sofia += int(mov.split(" ")[-1][1:-1])
        else:
            mateo += int(mov.split(" ")[-1][1:-1])
    return sofia, mateo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejecute de la siguiente manera: python main.py <ruta_absoluta_set_datos>")
        sys.exit(1)

    ruta_abs = sys.argv[1]

    linea = "Sophia debe agarrar la ultima (217); Mateo agarra la primera (455); Sophia debe agarrar la primera (852); Mateo agarra la primera (725); Sophia debe agarrar la ultima (378); Mateo agarra la primera (410); Sophia debe agarrar la primera (835); Mateo agarra la primera (239); Sophia debe agarrar la ultima (125); Mateo agarra la primera (404); Sophia debe agarrar la primera (462); Mateo agarra la primera (629); Sophia debe agarrar la primera (587); Mateo agarra la primera (171); Sophia debe agarrar la primera (604); Mateo agarra la primera (826); Sophia debe agarrar la primera (838); Mateo agarra la primera (384); Sophia debe agarrar la primera (336); Mateo agarra la ultima (21)"
    
    cargar_set_datos(ruta_abs)
    #test_all()



from src.lectura_archivos import leer_numeros_desde_txt
import os
import sys

"""
*ECUACION DE RECURRENCIA*

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
            print("Ganancia Sophia: ", puntos_sophia)
            print("Ganancia Mateo: ", puntos_mateo)
        else:
            print("La ruta no es absoluta.")
    except Exception as e:
        print("Error al cargar el archivo: ", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ejecute de la siguiente manera: python main.py <ruta_absoluta_set_datos>")
        sys.exit(1)

    ruta_abs = sys.argv[1]

    cargar_set_datos(ruta_abs)

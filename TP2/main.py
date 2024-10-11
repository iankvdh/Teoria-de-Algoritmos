from src.auxiliares import leer_numeros_desde_txt
import os
import sys

PRIMER_MONEDA = 0
ULTIMA_MONEDA = 1

def optimal_game(coins):
    
    size = len(coins)
    # Inicializamos la tabla con (0, 0) en lugar de solo 0 para todas las posiciones
    dp_table = [[(0, 0)] * size for _ in range(size)]

    # Inicializa la diagonal con los valores de las monedas
    for i in range(size):
        dp_table[i][i] = (coins[i], 0) 

    # Cargamos la segunda diagonal
    for j in range(size-1):
        dp_table[j][j+1] = (max(coins[j], coins[j+1]), 0)

    i = 0
    j = 2
    iter_aux = j
    
    # OPT(i,j) = MAX(m_i + MIN(OPT(i+2, j), OPT(i+1, j-1), m_j + MIN(OPT(i+1,j-1), OPT(i,j-2)))
    entre = 0
    while not (i == 0 and j == size):
        m_i = coins[i]
        m_j = coins[j]
        opt_izq = dp_table[i+2][j][0]
        opt_centro = dp_table[i+1][j-1][0]
        opt_der = dp_table[i][j-2][0]
        
        min_opt_i = min(opt_izq, opt_centro)
        min_opt_j = min(opt_centro, opt_der)

        ganancia = max(m_i + min_opt_i, m_j + min_opt_j)

        if m_i + min_opt_i >= m_j + min_opt_j:
            de_donde_vengo = min_opt_i
        else:
            de_donde_vengo = min_opt_j

        dp_table[i][j] = (ganancia, de_donde_vengo)
        # dp_table[i][j] = (i,j)
        i += 1
        j += 1
        if j >= size:
            i = 0
            iter_aux += 1
            j = iter_aux

    for row in dp_table:
        print(row)

    return dp_table


def reconstruccion(dp_table, coins):
    res = [None] * len(coins)
    i = 0
    j = len(coins) - 1
    turno = 0

    while i <= j:
        diferencia = dp_table[i][j][0] - dp_table[i][j][1]

        if turno % 2 == 0:
            # Juega Sophia
            if coins[i] == diferencia:

                if coins[i] == coins[j]:
                    down = dp_table[i+1][j][0]
                    left = dp_table[i][j-1][0]

                    if down > left:
                        res[turno] = ULTIMA_MONEDA
                        j -= 1
                    else:
                        res[turno] = PRIMER_MONEDA
                        i += 1
                else:                
                    res[turno] = PRIMER_MONEDA
                    i += 1
            else:
                res[turno] = ULTIMA_MONEDA
                j -= 1
        else:
            # Juega Mateo
            if coins[i] > coins[j]:
                res[turno] = PRIMER_MONEDA
                i += 1
            else:
                res[turno] = ULTIMA_MONEDA
                j -= 1
        
        turno += 1

    return res


def res_to_str(res, coins):
    res_str = []
    i = 0
    j = len(coins) - 1

    turno = 0
    suma_sophia = 0
    suma_mateo = 0
    for jugada in res:
        if turno % 2 == 0:
            if jugada == PRIMER_MONEDA:
                res_str.append(f"Sophia debe agarrar la primera ({coins[i]})")
                suma_sophia += coins[i]
                i += 1
            else:
                res_str.append(f"Sophia debe agarrar la ultima ({coins[j]})")
                suma_sophia += coins[j]
                j -= 1
        else:
            if jugada == PRIMER_MONEDA:
                res_str.append(f"Mateo agarra la primera ({coins[i]})")
                suma_mateo += coins[i]
                i += 1
            else:
                res_str.append(f"Mateo agarra la ultima ({coins[j]})")
                suma_mateo += coins[j]
                j -= 1
        turno += 1
    print("suma sofia:", suma_sophia)
    print("suma mateo:", suma_mateo)
    total = sum(coins)
    print("total:", sum(coins))
    print("diferencia:", sum(coins) - suma_sophia - suma_mateo)
    return res_str


def coin_game(coins):
    dp_table, max_profit = optimal_game(coins)
    
    for row in dp_table:
        print(row) 

    rec = reconstruccion(dp_table, coins)
    print(rec)
    res = res_to_str(rec, coins)
    print(res)
    
    print("max_profit S", max_profit[0])
    print("max_profit M:", max_profit[1],"\n")

def cargar_set_datos(ruta_archivo_abs):
    try:
        if os.path.isabs(ruta_archivo_abs):
            lista = leer_numeros_desde_txt(ruta_archivo_abs)
            #resultado, suma_s, suma_m =
            dp_table = optimal_game(lista)
            res = reconstruccion(dp_table, lista)
            resultado = res_to_str(res, lista)
            print("\n".join(resultado))
            print(dp_table[0][-1][0])
            # print("\n".join(resultado))
            # print("--------------------")
            # print(f"Total de Sophia: {suma_s}")
            # print(f"Total de Mateo: {suma_m}")
        else:
            print("La ruta no es absoluta.")
    except Exception as e:
        print("Error al cargar el archivo: ", e)




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
    # print(chequeo(linea))
    
    cargar_set_datos(ruta_abs)
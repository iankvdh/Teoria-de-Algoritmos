
SOPHIA = 0
MATEO = 1

def optimal_game(coins):
    size = len(coins)
    # Inicializamos la tabla con (0, 0) en lugar de solo 0 para todas las posiciones
    dp_table = [[(0, 0)] * size for _ in range(size)]

    # Inicializa la diagonal con los valores de las monedas
    for j in range(size):
        dp_table[j][j] = (coins[j], 0) 

    i = 0
    j = 1
    aux = 1
    while not (i == 0 and j == size):
        left = dp_table[i][j - 1]
        down = dp_table[i + 1][j]

        choice_i = coins[i] + min(down[0], down[1])
        choice_j = coins[j] + min(left[0], left[1])
        if choice_i > choice_j:
            mateo_choice = max(down[0], down[1])
            sophia_choice = choice_i
        else:
            mateo_choice = max(left[0], left[1])
            sophia_choice = choice_j    

        dp_table[i][j] = (sophia_choice,mateo_choice) 

        i += 1
        j += 1
        if j >= size:
            i = 0
            aux += 1
            j = aux
    
    return dp_table, dp_table[0][size-1] 




       




def reconstruccion(dp_table, coins):
    res = [None] * len(coins)
    i = 0
    j = len(coins) - 1
    turn = SOPHIA

    while i <= j:
        left = dp_table[i][j - 1]
        down = dp_table[i + 1][j]

        profit_sophia = dp_table[i][j][0]

        if turn == SOPHIA:
            if coins[i] + min(down[0], down[1]) == profit_sophia:
                res[i] = SOPHIA
                i += 1
            else:
                res[j] = SOPHIA
                j -= 1
        else:
            if coins[i] > coins[j]:
                res[i] = MATEO
                i += 1
            else:    
                res[j] = MATEO
                j -= 1

        turn = MATEO if turn == SOPHIA else SOPHIA
    return res



def res_to_str(res, coins):
    res_str = []
    i = 0
    j = len(coins) - 1
    turn = SOPHIA

    while i <= j:
        if turn == SOPHIA:
            if res[i] == SOPHIA:
                res_str.append("Primera moneda para Sophia")
                i += 1
            else:
                res_str.append("Última moneda para Sophia")
                j -= 1
        else:  
            if res[i] == MATEO:
                res_str.append("Primera moneda para Mateo")
                i += 1
            else:
                res_str.append("Última moneda para Mateo")
                j -= 1

        turn = MATEO if turn == SOPHIA else SOPHIA
    return res_str


def coin_game(coins):
    dp_table, max_profit = optimal_game(coins)
    
    for row in dp_table:
        print(row) 

    print("\n", "max_profit S", max_profit[0], "max_profit M:", max_profit[1],"\n")

    rec = reconstruccion(dp_table, coins)
    print(rec)
    res = res_to_str(rec, coins)
    print(res)
    

# Ejemplo de uso
#coins = [8, 15, 3, 7]
coins = [3, 2, 2, 3, 1, 2]     
coin_game(coins)



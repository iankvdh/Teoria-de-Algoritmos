"""
Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes 
decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar 
y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, 
si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M 
por la mudanza. Dados los arreglos de costos de operación en Londres (L) y California (C), 
indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo 
que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
OPT(i) = min(
    L[i] + OPT(i-1), # si operamos en Londres
    C[i] + OPT(i-1), # si operamos en California
    L[i] + M + OPT(i-2), # si operamos en Londres y el mes anterior venimos de California
    C[i] + M + OPT(i-2) # si operamos en California y el mes anterior venimos de Londres
)
"""

def mudanza(L, C, M):
    n = len(L)
    dp = [0] * (n+1)
    dp[1] = min(L[0], C[0])
    for i in range(2, n+1):
        dp[i] = min(
            L[i-1] + dp[i-1],
            C[i-1] + dp[i-1],
            L[i-1] + M + dp[i-2],
            C[i-1] + M + dp[i-2]
        )
    return dp

def reconstruccion(dp, L, C, M): # a chequear
    n = len(dp) - 1
    i = n
    localizaciones = []
    while i > 0:
        if dp[i] == L[i-1] + dp[i-1]:
            localizaciones.append('Londres')
            i -= 1
        elif dp[i] == C[i-1] + dp[i-1]:
            localizaciones.append('California')
            i -= 1
        elif dp[i] == L[i-1] + M + dp[i-2]:
            localizaciones.append('Londres')
            localizaciones.append('California')
            i -= 2
        else:
            localizaciones.append('California')
            localizaciones.append('Londres')
            i -= 2
    localizaciones.reverse()
    return localizaciones

L = [1, 20, 6, 9, 3, 10]
C = [50, 20, 2, 4, 5, 8]
M = 5
print(reconstruccion(mudanza(L, C, M), L, C, M))

# Complejidad: O(n) donde n es la cantidad de meses que queremos minimizar el costo de operación.
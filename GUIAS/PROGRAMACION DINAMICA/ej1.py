"""
Implementar un algoritmo que, utilizando programación dinámica, 
obtenga el valor del n-ésimo número de fibonacci. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

# OPT(i) = OPT(i-1) + OPT(i-2)

# TOP DOWN #
def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_memo_wrap(n, memo)

def fib_memo_wrap(n, memo):
    if n == 0:
        return 1
    if n == 1:
        return 1
        
    if memo[n-1] == None:
        memo[n-1] = fib_memo_wrap(n-1, memo)
    
    if memo[n-2] == None:
        memo[n-2] = fib_memo_wrap(n-2, memo)
    
    return memo[n-1] + memo[n-2]

# BOTTOM UP #
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo = [None] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

# Complejidad: O(n) donde n es el número de fibonacci que se quiere calcular.
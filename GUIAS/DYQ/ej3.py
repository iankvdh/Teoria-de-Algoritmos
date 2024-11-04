# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo 
# O(logn). Por ejemplo, para n=10 debe devolver 3, y para n=25 debe devolver 5. Justificar el orden del algoritmo.

def parte_entera_raiz(n):
    return parte_entera_raiz_wrapper(n, 0, n)

def parte_entera_raiz_wrapper(n, inicio, fin):
    if inicio == fin:
        return inicio
    medio = (inicio + fin) // 2
    if medio * medio == n:
        return medio
    if medio * medio < n and (medio + 1) * (medio + 1) < n:
        return parte_entera_raiz_wrapper(n, medio + 1, fin)
    return parte_entera_raiz_wrapper(n, inicio, medio)

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 1 (llamo 2 veces recursivamente pero con el if-statement
# B = 2 (parto el arreglo en 2)
# C = 0 (costo  de partir y juntar es O(1))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(1) = 0 = C --> T(n) = O(n^C * logB(n)) = O(log n)
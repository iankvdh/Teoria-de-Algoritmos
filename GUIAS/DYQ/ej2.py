# Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. 
# Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. 
# Se registra un 1 si pasa los tests, 0 en caso contrario. De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] 
# (es decir, unos seguidos de ceros). 
# Se pide: 
#   a. una función de orden O(logn) que, por división y conquista, encuentre el índice del primer 0, 
#      de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. 
#      Si no hay ningún 0 (solo hay unos), debe devolver -1. 
# 
#   b. demostrar con el Teorema Maestro que la función es, en efecto, O(logn).

def indice_primer_cero(arr):
    res = _indice_primer_cero(arr,0,len(arr)-1)
    if (arr[res]==1):
        return -1
    return res

def _indice_primer_cero(arr,inicio,fin):
    if inicio==fin:
        return inicio
    mitad = (inicio+fin) // 2
    if arr[mitad] > 0:
        return _indice_primer_cero(arr,mitad+1,fin)
    return _indice_primer_cero(arr,inicio,mitad)

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 1 (llamo 2 veces recursivamente pero con el if-statement
# B = 2 (parto el arreglo en 2)
# C = 0 (costo  de partir y juntar es O(1))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(1) = 0 = C --> T(n) = O(n^C * logB(n)) = O(log n)

def potencia(b, n):
    if n == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1.
    elif n % 2 == 0:
        # Si n es par, aplicamos b^n = (b^(n/2))^2
        half_power = potencia(b, n // 2)
        return half_power * half_power
    else:
        # Si n es impar, aplicamos b^n = b * b^(n-1)
        return b * potencia(b, n - 1)

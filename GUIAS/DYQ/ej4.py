# Aquí está el texto que pediste:

# Se tiene un arreglo de  N >= 3 elementos en forma de pico, es decir: estrictamente creciente hasta una determinada posición p, 
# y estrictamente decreciente a partir de ella (con  0 < p < N - 1). 
# Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.

# Se pide:
# - a. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico.
# - b. Justificar el orden del algoritmo mediante el teorema maestro.

def encontrar_pico(arr):
    return _encontrar_pico(arr, 0, len(arr) - 1)

def _encontrar_pico(arr, inicio, final):
    if inicio == final:
        return inicio
    medio = (inicio + final) // 2
    if arr[medio] < arr[medio + 1] and arr[medio] < arr[medio - 1]:
        return _encontrar_pico(arr, medio + 1, final)
    return _encontrar_pico(arr, inicio, medio)

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 1 (llamo 2 veces recursivamente pero con el if-statement
# B = 2 (parto el arreglo en 2)
# C = 0 (costo  de partir y juntar es O(1))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(1) = 0 = C --> T(n) = O(n^C * logB(n)) = O(log n)
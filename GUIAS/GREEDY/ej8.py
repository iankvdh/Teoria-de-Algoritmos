# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, 
# y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos 
# sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores 
# y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
# Indicar y justificar la complejidad del algoritmo implementado. 
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
# ¿Por qué se trata de un algoritmo Greedy? Justificar

# ¿Qué diferencias se perciben si en vez de tener que colocar los elementos completos, se pueden fraccionar para nuestra conveniencia?

# Algoritmo Greedy:
# Ordenar los elementos por valor/peso.
# Iterar sobre los elementos.
# Si el peso actual no excede la capacidad, agregarlo al resultado.
# Restar a la capacidad el peso del elemento actual.
# Repetir hasta que no queden más elementos.
# Complejidad: O(n log n) por el ordenamiento.

def mochila(W, elementos):
    elementos.sort(key=lambda x: x[0]/x[1], reverse=True)
    peso_actual = 0
    valor_actual = 0
    elementos_guardados = []
    for elemento in elementos:
        if peso_actual + elemento[1] <= W:
            peso_actual += elemento[1]
            valor_actual += elemento[0]
            elementos_guardados.append(elemento)
    return elementos
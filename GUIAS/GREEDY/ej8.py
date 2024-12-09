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

def mochila(elementos, W):
    elementos.sort(key=lambda x: x[0]/x[1], reverse=True)
    peso_actual = 0
    valor_actual = 0
    elementos_guardados = []
    for i in range(len(elementos)):
        if peso_actual + elementos[i][1] <= W:
            peso_actual += elementos[i][1]
            valor_actual += elementos[i][0]
            elementos_guardados.append(elementos[i])
    return elementos_guardados

"""
Es un algoritmo Greedy porque en cada paso buscamos el optimo local con el fin de llegar a un optimo global.
En cada paso, seleccionamos el elemento con mayor valor/peso, maximizando el valor total de los elementos guardados.
De esta forma, garantizamos que el valor total sea máximo. Si seleccionamos los elementos con menor valor/peso primero,
el valor total será menor. Por lo tanto, seleccionar los elementos con mayor valor/peso primero maximiza el valor total.
No, no es un algoritmo óptimo. Existen casos en los que seleccionar los elementos con mayor valor/peso no maximiza el valor
total. Por ejemplo, si los elementos tienen valores muy altos y pesos muy bajos, seleccionar los elementos con mayor valor/peso
no maximiza el valor total.
Las diferencia si se pueden fraccionar los elementos es que se pueden seleccionar partes de los elementos y completar la mochila
con partes de diferentes elementos. Sería mejor, ya que se pueden seleccionar partes de los elementos con mayor valor/peso, maximizando
aún más el valor total.
"""
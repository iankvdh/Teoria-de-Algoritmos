# DEADLINES: https://algoritmos-rw.github.io/tda_bg/material/guias/greedy/ (EJ9)

# Dada una lista de tareas, donde cada tarea tiene un tiempo de ejecución y un deadline,
# se desea minimizar la latencia de las tareas. La latencia de una tarea es la cantidad de tiempo
# que la tarea termina después de su deadline. Implementar un algoritmo Greedy que reciba dos listas,
# una con los deadlines de las tareas y otra con los tiempos de ejecución de las tareas, y devuelva
# una lista con tuplas que contengan el tiempo de ejecución de la tarea y la latencia de la tarea.
# Indicar y justificar la complejidad del algoritmo implementado.

# Algoritmo Greedy:
# Ordenar las tareas por deadline.
# Iterar sobre las tareas.
# Calcular la finalización de la tarea.
# Si la finalización es antes del deadline, la latencia es 0.
# Si no, la latencia es la diferencia entre la finalización y el deadline.

# Complejidad: O(n log n) por el ordenamiento.

def minimizar_latencia(L_deadline, T_tareas):
    indices_ordenados = sorted(range(len(L_deadline)), key=lambda k: L_deadline[k])
    deadlines_menor_a_mayor = [L_deadline[i] for i in indices_ordenados]
    tiempo_tareas_ordenadas_por_deadline = [T_tareas[i] for i in indices_ordenados]
    tareas_ordenadas = []
    tiempo_actual = 0
    for i, tarea in enumerate(deadlines_menor_a_mayor):
        finalizacion_tarea = tiempo_actual + tiempo_tareas_ordenadas_por_deadline[i]
        if finalizacion_tarea < deadlines_menor_a_mayor[i]:
            latencia_tarea_actual = 0
        else:
            latencia_tarea_actual = finalizacion_tarea - deadlines_menor_a_mayor[i]
        tiempo_actual += tiempo_tareas_ordenadas_por_deadline[i]
        tareas_ordenadas.append((tiempo_tareas_ordenadas_por_deadline[i], latencia_tarea_actual))
    return tareas_ordenadas
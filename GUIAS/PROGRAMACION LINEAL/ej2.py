import pulp

"""
(★) Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).
"""

"""
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero [no quiere trabajar dos días seguidos].
Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo 
que no aceptará trabajar dos días seguidos.Hacer una reconstrucción para verificar qué días debe trabajar. 
Indicar y justificar la complejidad del algoritmo implementado.

Variables:
y(i): dia i (binario)
g(i): ganancia i (int)

Restricciones:
Hoy + Mañana < 2 
y(i) + y(i+1) <= 1

Ecuacion a maximizar: Max(sum(y(i) * g(i)))

"""

def juan_el_vago(ganancias):
    n = len(ganancias)
    
    problema = pulp.LpProblem("Juan_el_vago", pulp.LpMaximize)

    x = [pulp.LpVariable(f"x{i}", cat="Binary") for i in range(n)]

    # Función objetivo: maximizar la suma de las ganancias por los días trabajados
    problema += pulp.lpSum([ganancias[i] * x[i] for i in range(n)])

    # Restricciones: no puede trabajar dos días consecutivos
    for i in range(n - 1):
        problema += x[i] + x[i + 1] <= 1

    problema.solve()

    seleccionados = [i for i in range(n) if pulp.value(x[i]) == 1]
    monto_maximo = sum([ganancias[i] for i in seleccionados])

    print(f"Juan debe trabajar en los días: {seleccionados}")
    print(f"El monto máximo que puede ganar es: {monto_maximo}")

# Ejemplo de uso
ganancias = [3, 2, 5, 10, 7]
juan_el_vago(ganancias)

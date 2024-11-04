import pulp

"""
Implementar un modelo de programación lineal que resuelva el problema de 3-SAT mínimo: 
que encuentre una solución que satisfaga, utlizando la menor cantidad de variables en true posible.

(ni idea que es 3-SAT, Copy-Paste de Chat-GPT)
"""

# Función para resolver el problema de 3-SAT mínimo
def solve_3sat_minimum(clauses):
    # Crear un problema de programación lineal
    prob = pulp.LpProblem("3-SAT_Minimum", pulp.LpMinimize)
    
    # Obtener un conjunto de todas las variables
    variables = set()
    for clause in clauses:
        for literal in clause:
            variables.add(abs(literal))

    x = pulp.LpVariable.dicts("x", variables, cat='Binary')

    # Objetivo: minimizar el número de variables en true
    prob += pulp.lpSum(x[i] for i in variables), "Minimize_True_Variables"

    # Agregar restricciones para cada cláusula
    for clause in clauses:
        prob += (x[abs(clause[0])] + x[abs(clause[1])] + x[abs(clause[2])] >= 1, f"Clause_{clauses.index(clause)}")

    prob.solve()

    # Obtener la solución
    solution = {i: x[i].varValue for i in variables}
    is_satisfiable = prob.status == pulp.LpStatusOptimal # manzo spanglish

    return is_satisfiable, solution

# Ejemplo de uso
if __name__ == "__main__":
    # Definir las cláusulas de la fórmula 3-SAT
    # Ejemplo: (x1 OR NOT x2 OR x3) AND (NOT x1 OR x2 OR x4) AND (x2 OR NOT x3 OR x5)
    clauses = [
        [1, -2, 3],
        [-1, 2, 4],
        [2, -3, 5]
    ]

    satisfiable, assignment = solve_3sat_minimum(clauses)

    if satisfiable:
        print("La fórmula es satisfactoria.")
        print("Asignación de variables (True = 1, False = 0):")
        for var, value in assignment.items():
            print(f"x{var}: {'True' if value == 1 else 'False'}")
    else:
        print("No se encontró solución satisfactoria.")

# perdón buch, nunca supe que es 3-SAT
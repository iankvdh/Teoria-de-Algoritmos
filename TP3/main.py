from algoritmos.backtracking import mostrar_resultados_ruta_abs_bt
from algoritmos.validador import mostrar_resultados_ruta_abs_validador
from algoritmos.aproximacion import mostrar_resultados_ruta_abs_aprox

if __name__ == "__main__":
    print("----- TP3 - TDA - 2C 2024 -----")
    print("Indique qué desea ejecutar:")
    print("1) Backtracking")
    print("2) Programación Lineal")
    print("3) Validador")
    print("4) Aproximación")
    while True:
        opcion = int(input("Ingrese una opción (1-4): "))
        if opcion in [1, 2, 3, 4]:
            break
        else:
            print("Opción no válida.")
    if opcion == 1:
        while True:
            ruta_abs_bt = input("Ingrese la ruta absoluta del archivo para ejecutar con Backtracking: ")
            if ruta_abs_bt.endswith(".txt"):
                break
            else:
                print("Opción no válida.")
        mostrar_resultados_ruta_abs_bt(ruta_abs_bt)
    elif opcion == 2:
        while True:
            ruta_abs_pl = input("Ingrese la ruta absoluta del archivo para ejecutar con Programación Lineal: ")
            if ruta_abs_pl.endswith(".txt"):
                break
            else:
                print("Opción no válida.")
        # mostrar_resultados_ruta_abs_pl(ruta_abs_pl)
        print("Funcionalidad no implementada.")
    elif opcion == 3:
        while True:
            ruta_abs_validador = input("Ingrese la ruta absoluta del archivo de Validador: ")
            ruta_abs_validador_resultados = input("Ingrese la ruta absoluta del archivo de Resultados Validador: ")
            if ruta_abs_validador.endswith(".txt"):
                break
            else:
                print("Opción no válida.")
        mostrar_resultados_ruta_abs_validador(ruta_abs_validador, ruta_abs_validador_resultados)
    elif opcion == 4:
        while True:
            ruta_abs_aprox = input("Ingrese la ruta absoluta del archivo para ejecutar con Aproximación: ")
            if ruta_abs_aprox.endswith(".txt"):
                break
            else:
                print("Opción no válida.")
        mostrar_resultados_ruta_abs_aprox(ruta_abs_aprox)
    else:
        print("Vuelva a ejecutar el programa.")


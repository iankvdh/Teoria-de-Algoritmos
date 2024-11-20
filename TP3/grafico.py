import sys
from algoritmos.bt_tiempo_vs_matriz import bt_mostrar_tiempo_vs_matriz
from algoritmos.aprox_tiempo_vs_matriz import aprox_tiempo_vs_matriz
from algoritmos.aprox_cota import aprox_cota

"""
Ejecuta los gráficos correspondientes según la opción seleccionada.
"""
def ejecutar_graficos():
    if len(sys.argv) > 1:
        grafico = sys.argv[2]
        if grafico == "BT_tiempo_vs_matriz":
            bt_mostrar_tiempo_vs_matriz()
        elif grafico == "BT_tiempo_vs_barcos":
            pass
        elif grafico == "APROX_tiempo_vs_matriz":
            aprox_tiempo_vs_matriz()
        elif grafico == "APROX_cota":
            aprox_cota()
        else:
            print("Opción no válida.")
    else:
        print("Por favor, ejecute directamente el archivo {ejecutar_graficos.sh}.")

ejecutar_graficos()
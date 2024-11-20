import sys
from algoritmos.bt_tiempo_vs_matriz import bt_mostrar_tiempo_vs_matriz

"""
echo "Seleccione qué gráfico desea ejecutar:"
echo "1) BACKTRACKING: Tiempo de ejecución vs Tamaño de Matriz"
echo "2) BACKTRACKING: Tiempo de ejecución vs Tamaño de Barcos"
echo "3) BACKTRACKING: Tiempo de ejecución vs Cantidad de Barcos"
echo "4) BACKTRACKING vs. PROGRAMACIÓN LINEAL"

read -p "Ingrese una opción (1-5): " opcion

case $opcion in
    1)
        py grafico.py --grafico BT_tiempo_vs_matriz
        ;;
    2)
        py grafico.py --grafico BT_tiempo_vs_barcos
        ;;
    3)
        py grafico.py --grafico BT_tiempo_vs_cant_barcos
        ;;
    4)
        py grafico.py --grafico BT_vs_PL
        ;;
    *)
        echo "Opción no válida"
        ;;
esac

"""
def ejecutar_graficos():
    if len(sys.argv) > 1:
        grafico = sys.argv[2]
        if grafico == "BT_tiempo_vs_matriz":
            bt_mostrar_tiempo_vs_matriz()
        elif grafico == "BT_tiempo_vs_barcos":
            pass
        elif grafico == "BT_tiempo_vs_cant_barcos":
            pass
        elif grafico == "BT_vs_PL":
            pass
        else:
            print("Opción no válida.")
    else:
        print("Por favor, ejecute directamente el archivo {ejecutar_graficos.sh}.")

ejecutar_graficos()
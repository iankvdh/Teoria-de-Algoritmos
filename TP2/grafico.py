import sys
from src.auxiliares import *
from src.lectura_archivos import monedas_desde_archivos
from src.jugar_n_juegos import jugar_n_juegos
from src.cant_vs_tiempo import mostrar_cantidad_vs_tiempo
from src.cant_vs_puntos import mostrar_cantidad_vs_puntos
from src.variabilidad import mostrar_tiempo_vs_variabilidad
from src.reconstruccion_vs_tiempo import reconstruccion_vs_tiempo

def ejecutar_graficos():
    """
    Función que se encarga de ejecutar los gráficos según los argumentos pasados por
    consola. Si no se pasan argumentos, se imprime un mensaje de error.
    """
    if len(sys.argv) > 1:
        grafico = sys.argv[2]
        if grafico == "tiempo_vs_cantidad":
            #tamaños, listas = monedas_desde_archivos()
            mostrar_cantidad_vs_tiempo()
        elif grafico == "puntos_vs_cantidad":
            tamaños, listas = monedas_desde_archivos()
            _, puntos_sofia, puntos_mateo = jugar_muchos_arreglos(listas)
            mostrar_cantidad_vs_puntos(tamaños, puntos_sofia, puntos_mateo)
        elif grafico == "victorias_sofia":
            if len(sys.argv) > 3:
                n = int(sys.argv[4])
                jugar_n_juegos(n)
            else:
                jugar_n_juegos()
        elif grafico == "tiempo_vs_variabilidad":
            mostrar_tiempo_vs_variabilidad()
        elif grafico == "reconstruccion_vs_tiempo":
            #tamaños, listas = monedas_desde_archivos()
            reconstruccion_vs_tiempo()
        else:
            print("Opción no válida.")

    else:
        print("Por favor, ejecute directamente el archivo {ejecutar_graficos.sh}.")

ejecutar_graficos()

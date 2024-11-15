from batalla_naval import Batalla_Naval
import time
import os

def leer_inputs(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        lineas = file.readlines()

    demandas_filas = []
    demandas_columnas = []
    barcos = []
    seccion = 0  

    for linea in lineas:
        linea = linea.strip()
        if linea.startswith('#'):
            continue

        # Si encuentro linea vacia salto a la siguiente seccion
        if linea == '':
            seccion += 1
            continue

        if seccion == 0:
            demandas_filas.append(int(linea))
        elif seccion == 1:
            demandas_columnas.append(int(linea))
        elif seccion == 2:
            barcos.append(int(linea))

    return demandas_filas, demandas_columnas, barcos


def leer_resultados_esperados(nombre_archivo, inputs):
    resultados_esperados = {}
    with open(nombre_archivo, 'r') as file:
        lineas = file.readlines()
        
    for i, linea in enumerate(lineas):
        if inputs in linea:
            posiciones = []
            i += 1  # Mover a la siguiente línea para empezar a procesar
            while 'Demanda cumplida' not in lineas[i]:
                i += 1

            demanda_cumplida = int(lineas[i].split(":")[1].strip())
            demanda_total = int(lineas[i + 1].split(":")[1].strip())

            resultados_esperados['demanda_cumplida'] = demanda_cumplida
            resultados_esperados['demanda_total'] = demanda_total
            break

    return resultados_esperados['demanda_cumplida'], resultados_esperados['demanda_total']




def main():
    def leer_archivos(carpeta):
        archivos = os.listdir(carpeta)
        archivos_validos = [
            archivo for archivo in archivos
            if ":Zone.Identifier" not in archivo
                and 'Resultados Esperados.txt' not in archivo
                and 'Resultados Esperados Tablero.txt' not in archivo
                and '30_25_25.txt' not in archivo ################################################################################################
                and archivo.endswith('.txt')
        ]
        return archivos_validos


    # Ejemplo de uso
    carpeta = 'data'
    archivos = leer_archivos(carpeta)



    for archivo in archivos:
        demandas_filas, demandas_columnas, barcos = leer_inputs('data/' + archivo)
        demanda_cumplida_esperada, demanda_total = leer_resultados_esperados('data/' + 'Resultados Esperados.txt', archivo)


        print("----------------------------", archivo ,"----------------------------")
        print("demanda_cumplida_esperada:", demanda_cumplida_esperada)
        print("demanda_total:", demanda_total)
        start_time = time.time()
        batalla_naval = Batalla_Naval(demandas_filas, demandas_columnas, barcos)
        end_time = time.time()  

        print("Demanda cumplida: ", batalla_naval.get_optimal_demand())
        print(f"tiempo de ejecucion:, {end_time - start_time} segundos")
        print()
        batalla_naval.print_solution()
        print("-------------------------------------------------------------------")

main()




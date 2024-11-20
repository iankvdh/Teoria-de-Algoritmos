import os

CARPETA = 'data'

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
            i += 1
            while 'Demanda cumplida' not in lineas[i]:
                if "None" in lineas[i]:
                    posiciones.append(None)
                elif ":" in lineas[i]:
                    pos = lineas[i].strip().split(":")[1].strip()
                    if pos:
                        if "-" in pos:
                            inicio, fin = pos.split(" - ")
                            inicio = tuple(map(int, inicio.strip("()").split(", ")))
                            fin = tuple(map(int, fin.strip("()").split(", ")))
                            posiciones.append((inicio, fin))
                        else:
                            coord = tuple(map(int, pos.strip("()").split(", ")))
                            posiciones.append(coord)
                i += 1


            demanda_cumplida = int(lineas[i].split(":")[1].strip())
            demanda_total = int(lineas[i + 1].split(":")[1].strip())
            
            resultados_esperados['posiciones'] = posiciones
            resultados_esperados['demanda_cumplida'] = demanda_cumplida
            resultados_esperados['demanda_total'] = demanda_total
            break

    return resultados_esperados['posiciones'], resultados_esperados['demanda_cumplida'], resultados_esperados['demanda_total']

def leer_archivos(carpeta):
    archivos = os.listdir(carpeta)
    archivos_validos = [
        archivo for archivo in archivos
        if ":Zone.Identifier" not in archivo
            and 'Resultados Esperados.txt' not in archivo
            and 'Resultados Esperados Tablero.txt' not in archivo
            and '30_25_25.txt' not in archivo # se evita este archivo
            and archivo.endswith('.txt')
    ]
    return archivos_validos


def leer_todos_archivos(carpeta):
    archivos = os.listdir(carpeta)
    archivos_validos = [
        archivo for archivo in archivos
        if ":Zone.Identifier" not in archivo
            and 'Resultados Esperados.txt' not in archivo
            and 'Resultados Esperados Tablero.txt' not in archivo
            and archivo.endswith('.txt')
    ]
    return archivos_validos

def leer_resultados_validador():
    carpeta = 'data_validador'
    archivos = os.listdir(carpeta)
    archivos_validos = [
        archivo for archivo in archivos
        if ":Zone.Identifier" not in archivo
            and 'Resultados Validador.txt' not in archivo
            and archivo.endswith('.txt')
    ]
    return archivos_validos     
    

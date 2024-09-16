def leer_numeros_desde_txt(nombre_archivo):
    nombre_archivo = 'data/' + nombre_archivo

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().strip()  
        numeros_str = contenido.split(';')  
        numeros = [int(num) for num in numeros_str]  
    return numeros

def modelo_lineal(x, m, b):
    return m * x + b

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c
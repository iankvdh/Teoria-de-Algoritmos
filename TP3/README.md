# TP3 - Diversión NP-Completa

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de  para resolver un Problema NP-Completo, así como el análisis de posibles aproximaciones.

---

## **Índice**
1. [Estructura del Proyecto](#estructura-del-proyecto)  
2. [Requisitos](#requisitos)  
3. [Formato de los Archivos](#formato-de-los-archivos)  
   - [Archivo de Entrada](#1-archivo-de-entrada)  
   - [Archivo de Resultados](#2-archivo-de-resultados-esperados-y-validados)  
4. [Cómo Ejecutar el Programa](#cómo-ejecutar-el-programa)  
   - [Backtracking](#1-backtracking)  
   - [Programación Lineal (PL)](#2-programación-lineal-pl)  
   - [Validador](#3-validador)  
5. [Notas](#notas)  

---

## **Estructura del Proyecto**

```
📁 TP3/
│
├── 📂 algoritmos/                # Contiene las implementaciones de los algortimos pepidos en el enunciado
├── 🖼️ img/                       # Carpeta para almacenar las imágenes generadas
├── 📄 Informe_TP3.pdf            # Informe detallado del proyecto
├── 📑 README.md                  # Documentación del proyecto
```

## Requisitos

Antes de ejecutar algun algoritmo, asegúrese de tener instalados los siguientes requisitos:

- **Python 3.x**
- **Librerías Python:**
  - `matplotlib`
  - `numpy`
  - `scipy`

Puede instalar estas dependencias como se detalla en [README.md](../README.md).

-----------------

## **Formato de los Archivos**

### 1. **Archivo de entrada**
- Contiene:
  - Demandas de las filas.
  - Demandas de las columnas.
  - Largos de los barcos.
- Las secciones de filas y columnas están separadas por una línea en blanco.

**Ejemplo:**
```txt
# ejemplo del archivo 10_10_10.txt
3
2
2
4
2
1
1
2
3
0

1
2
1
3
2
2
3
1
5
0

3
1
1
2
4
2
1
3
1
2
```

---

### 2. **Archivo de resultados esperados y validados**
- Contiene información sobre los barcos colocados y las demandas cumplidas.
  
**Ejemplo:**
```txt
10_10_10.txt
Posiciones:
0: (0, 8) - (3, 8)
1: (0, 6) - (2, 6)
2: (8, 3) - (8, 5)
3: (3, 0) - (3, 1)
4: (3, 3) - (4, 3)
5: (7, 7) - (7, 8)
6: (0, 2)
7: (4, 5)
8: (5, 1)
9: (6, 4)
Demanda cumplida: 40
Demanda total: 40
```

> ⚠️ **Importante**: Si desea que su archivo de entrada sea integrado en la ejecución de gráficos, deberá agregarlo a la carpeta `/data`. 

---

## **Cómo Ejecutar el Programa**

### 1. **Backtracking**
1. Seleccione la opción `1` en el menú.
2. Ingrese la **ruta absoluta** del archivo de entrada que desea analizar. 
   - El archivo debe estar en formato `.txt`.
3. El programa procesará el archivo y mostrará los resultados en la consola.

**Ejemplo de ejecución:**
```bash
$ python main.py
----- TP3 - TDA - 2C 2024 -----
Indique qué desea ejecutar:
1) Backtracking
2) Programación Lineal
3) Validador
Ingrese una opción (1-3): 1
Ingrese la ruta absoluta del archivo de Backtracking: /ruta/a/10_10_10.txt
# Resultados procesados mostrados en la consola.
```

---

### 2. **Programación Lineal (PL)**
1. Seleccione la opción `2` en el menú.
2. Ingrese la **ruta absoluta** del archivo de entrada.
   - Actualmente, el método está desactivado (requiere implementación de `mostrar_resultados_ruta_abs_pl`).

**Ejemplo de ejecución:**
```bash
$ python main.py
----- TP3 - TDA - 2C 2024 -----
Indique qué desea ejecutar:
1) Backtracking
2) Programación Lineal
3) Validador
Ingrese una opción (1-3): 2
Ingrese la ruta absoluta del archivo de Programación Lineal: /ruta/a/10_10_10.txt
# Resultados procesados mostrados en la consola.
```

---

### 3. **Validador**
1. Seleccione la opción `3` en el menú.
2. Ingrese las rutas absolutas de:
   - El archivo de entrada (tablero y demandas).
   - El archivo de resultados esperados.
3. El programa comparará las demandas con los resultados del archivo y mostrará si son correctos.

**Ejemplo de ejecución:**
```bash
$ python main.py
----- TP3 - TDA - 2C 2024 -----
Indique qué desea ejecutar:
1) Backtracking
2) Programación Lineal
3) Validador
Ingrese una opción (1-3): 3
Ingrese la ruta absoluta del archivo de Validador: /ruta/a/10_10_10.txt
Ingrese la ruta absoluta del archivo de Resultados Validador: /ruta/a/resultados_10_10_10.txt
# Resultados de validación mostrados en la consola.
```

---

## **Notas**
- **Errores comunes:**
  - Ingresar rutas incorrectas o archivos que no terminan en `.txt`.
  - Archivos con formatos no compatibles.
- **Mensajes de error:** El programa mostrará advertencias en caso de errores en los formatos o rutas.


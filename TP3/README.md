# TP3 - Diversión NP-Completa

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de  para resolver un Problema NP-Completo, así como el análisis de posibles aproximaciones.

## Estructura del proyecto

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

## **Cómo ejecutar los conjuntos de datos**

Este proyecto permite procesar y validar archivos de datos para resolver problemas de distribución utilizando dos métodos principales: **backtracking** y **validador**. A continuación, se detallan las instrucciones para ejecutar ambos métodos, así como los formatos requeridos para los archivos de entrada y salida.

---

### **Ejecutar con el método Backtracking**

#### **1. Preparar el entorno**
1. Clone este repositorio o descargue los archivos directamente. Asegúrese de que todos los archivos necesarios estén presentes en su directorio de trabajo.
2. Consulte el archivo [README.md](../README.md) original para verificar los requisitos previos y configuraciones.

#### **2. Colocar archivos de entrada**
- Los archivos de entrada deben estar ubicados en la carpeta `data/`.
- Cada archivo debe cumplir con el **formato de entrada** especificado más abajo.

#### **3. Ejecutar desde la terminal**
Abra una terminal y ejecute el programa usando el comando adecuado, por ejemplo:
```bash
python backtracking.py
```

---

### **Ejecutar con el método Validador**

#### **1. Preparar el entorno**
1. Clone este repositorio o descargue los archivos directamente.
2. Verifique que todos los archivos necesarios están presentes, como se detalla en [README.md](../README.md).

#### **2. Colocar archivos de entrada**
- Los archivos de entrada deben estar ubicados en la carpeta `data_validador/`.
- Cada archivo debe cumplir con el **formato de entrada** especificado más abajo.

#### **3. Ejecutar desde la terminal**
Ejecute el programa usando el siguiente comando en la terminal:
```bash
python validador.py 
```

---

### **Formato de los archivos de entrada**

Los archivos de entrada deben tener la extensión `.txt` y estar estructurados de la siguiente manera:

1. **Formato del archivo de entrada:**
   - El archivo contiene:
     - `n` líneas iniciales con las demandas de las filas.
     - `m` líneas siguientes con las demandas de las columnas.
     - `k` líneas finales con los largos de los barcos.
   - Las secciones de filas y columnas están separadas por una **línea en blanco**.

   **Ejemplo de archivo de entrada:**
   ```
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

2. **Formato de los resultados esperados y validados:**
   - Cada archivo de resultados debe seguir este formato:
     - Nombre del archivo analizado: `<nombre_archivo>.txt`.
     - Posiciones de los barcos en el formato:
       `Índice: (fila_inicio, columna_inicio) - (fila_fin, columna_fin)`
     - Los barcos de una sola celda se representan como:
       `Índice: (fila, columna)`
     - Indicadores de demanda cumplida y total.

   **Ejemplo de archivo de resultados:**
   ```
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

---

### **Notas importantes**
1. **Comentarios en los archivos de entrada:**
   - Las líneas que comienzan con `#` son ignoradas por el programa.
2. **Estructura de carpetas:**
   - Todos los archivos de entrada deben estar en las carpetas correspondientes (`data/` para Backtracking y `data_validador/` para Validador).
3. **Resultados esperados:**
   - Asegúrese de incluir un archivo de resultados esperados para cada archivo de entrada.

---


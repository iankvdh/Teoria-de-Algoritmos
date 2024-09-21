# TP1 - Los Algoritmos Greedy son juegos de niños

Este proyecto implementa una serie de gráficos y simulaciones para analizar el rendimiento y comportamiento de un algoritmo que simula juegos entre Sophia y Mateo. Se han desarrollado gráficos que permiten visualizar:

1. **Tiempo de ejecución vs. Cantidad de elementos**  
2. **Puntos de Sophia y Mateo vs. Cantidad de elementos**  
3. **Veces que ganó Sophia vs. Cantidad de juegos simulados**  

## Estructura del proyecto

```
📁 TP1/
│
├── 📂 data/                      # Contiene archivos de texto con los datos de entrada
├── 🖼️ img/                       # Carpeta para almacenar las imágenes generadas
├── 📈 grafico.py                 # Código principal para generar gráficos
├── ⚙️ implementacion_optima.py   # Implementación del algoritmo Greedy utilizado en las simulaciones
├── 📄 Informe_TP1.pdf            # Informe detallado del proyecto
├── 📑 README.md                  # Documentación del proyecto
└── ▶️ ejecutar_graficos.sh       # Script bash para ejecutar los gráficos
```

### Requisitos

Antes de ejecutar el script, asegúrese de tener instalados los siguientes requisitos:

- **Python 3.x**
- **Librerías Python:**
  - `matplotlib`
  - `numpy`
  - `scipy`

Puede instalar estas dependencias como se detalla en [README.md](../README.md):

### Cómo ejecutar el programa

#### 1. Clonar el repositorio o descargar los archivos

Primero, asegúrese de que todos los archivos necesarios estén presentes en su directorio de trabajo, como se detalla en [README.md](../README.md).

#### 2. Ejecución desde la terminal

##### Formato de los archivos de entrada

Los archivos de entrada **deben estar en formato `.txt`** y deben ser situados en la carpeta **data**. Además deben contener **únicamente valores numéricos** separados por `;`. Asegúrate de que no haya otros caracteres, como letras o símbolos, en el archivo. El programa ignorará cualquier línea de comentario que comience con `#`.

##### Ejemplo de archivo de entrada válido:
```
406;691;451;628;950;324;906;34;345;647;589;585;728;338;598;362;999;227;248;863;852;344;166;153;778
```
Para ejecutar el programa pasando por parámetro un archivo con los datos de monedas, sigue los siguientes pasos:

1. Abre la terminal y navega al directorio donde está el archivo `main.py`.

2. Ejecuta el siguiente comando, reemplazando `nombre_archivo.txt` por el nombre del archivo de entrada (que debe estar ubicado en la carpeta `data`):

   ```bash
   python main.py nombre_archivo.txt
   ```

#### Detalles de la Ejecución:
Al ejecutar el programa, este procesará el archivo, simulará el juego y devolverá la secuencia de jugadas junto con el total de monedas obtenidas por Sophia y Mateo.

El archivo de entrada no requiere que conozcas la solución esperada. El propósito de este programa es resolver el problema y determinar qué jugador obtiene la mayor cantidad de monedas con una estrategia óptima.

#### Ejemplo de salida:
   ```bash
      Primera moneda para Sophia
      Última moneda para Mateo
      ...
      Primera moneda para Sophia
      Total de Sophia: 7328
      Total de Mateo: 6682
   ```

### Cómo ejecutar los gráficos

#### 1. Dar permisos de ejecución al script

Antes de ejecutar el script `.sh`, asegúrese de otorgarle permisos de ejecución. Desde la terminal, navegue al directorio del proyecto y ejecute:

```
chmod +x ejecutar_graficos.sh
```

#### 2. Ejecutar el script

Para ejecutar el script y seleccionar el gráfico deseado, simplemente ejecute el archivo `.sh` desde la terminal de la siguiente manera:

```
./ejecutar_graficos.sh
```

Se le presentarán tres opciones para generar gráficos:

1. **Tiempo de ejecución vs Cantidad de elementos:**  
   Genera un gráfico que muestra el tiempo que tarda el algoritmo en ejecutarse en función de la cantidad de elementos en la lista.

2. **Puntos de Sophia y Mateo vs Cantidad de elementos:**  
   Muestra un gráfico con los puntos acumulados por Sophia y Mateo para distintas cantidades de elementos en la lista.

3. **X victorias de Sophia vs Cantidad de juegos simulados:**  
   Simula `n` juegos y muestra un gráfico con las veces que ganó Sophia.

#### 3. Simulación personalizada

Si elige la opción 3 para simular los juegos de Sophia y Mateo, se le pedirá que ingrese la cantidad de juegos a simular. Puede dejar el campo vacío para usar un valor predeterminado (1000) o ingresar un número entero positivo menor o igual a 10,000. En caso de ingresar un valor mayor a 10,000, se mostrará un mensaje de error.

```
Ingrese la cantidad de juegos a simular (o deje en blanco para valor por defecto): 
```

#### 4. Ejemplo de Ejecución

```
Seleccione qué gráfico desea ejecutar:
1) Tiempo de ejecución vs Cantidad de elementos
2) Puntos de Sophia y Mateo vs Cantidad de elementos
3) X victorias de Sophia vs Cantidad de juegos simulados
Ingrese una opción (1-3): 1
```

#### Notas adicionales

- Asegúrese de tener todos los archivos de datos necesarios en la carpeta `data/`, ya que los gráficos dependen de ellos.
- En caso de que no se generen los gráficos o haya algún error en la ejecución, consulte los permisos de los archivos y asegúrese de tener instaladas las dependencias correctamente y estar en el directorio adecuado.

# TP2 - Programación Dinámica For The Win

Este proyecto proporciona un archivo `main.py` que implementa un algoritmo por programación dinámica para resolver el **juego de las monedas**, un juego competitivo entre dos jugadores (Sophia y Mateo) donde ambos eligen monedas alternadamente de una fila con el objetivo de maximizar la suma de las monedas que obtienen. Los jugadores pueden elegir únicamente la primera o la última moneda en cada turno, y se asume que Sophia juega de manera óptima y Mateo siempre tomará la moneda de mayor valor que se encuentre en los extremos. El algoritmo desarrollado permite determinar la secuencia de decisiones óptimas que Sophia debe tomar para garantizar su victoria, considerando todas las posibles jugadas de Mateo.

Además, el proyecto incluye una serie de gráficos y simulaciones que permiten analizar el rendimiento y comportamiento del algoritmo en los enfrentamientos entre Sophia y Mateo. Estos gráficos visualizan:

1. **Tiempo de ejecución vs. Cantidad de elementos**: Muestra cómo varía el tiempo que tarda el algoritmo en ejecutarse a medida que aumenta la cantidad de monedas.
2. **Puntos de Sophia y Mateo vs. Cantidad de elementos**: Compara la suma total de puntos obtenidos por cada jugador en función del número de monedas en la fila.
3. **Veces que ganó Sophia vs. Cantidad de juegos simulados**: Visualiza la frecuencia con la que Sophia gana a medida que se simulan más juegos.
4. **Tiempo de ejecución vs Variabilidad de elementos**: Evalúa cómo afecta la variabilidad en los valores de las monedas al tiempo de ejecución del algoritmo.
5. **Tiempo de ejecución de la Reconstrucción vs Cantidad de elementos**: Analiza el tiempo necesario para reconstruir la secuencia de decisiones óptimas a medida que aumenta la cantidad de monedas.

Este enfoque no solo permite comprender la solución óptima para Sophia, sino también estudiar el comportamiento general del algoritmo en diferentes escenarios, proporcionando una visión detallada de su eficiencia y resultados en el contexto del juego de las monedas.

## Índice

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Requisitos](#requisitos)
3. [Posibles ejecuciones](#posibles-ejecuciones)
   - [Cómo ejecutar el programa](#cómo-ejecutar-el-programa)
   - [Cómo ejecutar los gráficos](#cómo-ejecutar-los-gráficos)
4. [Notas adicionales](#notas-adicionales)

## Estructura del proyecto

```
📁 TP2/
│
├── 📂 data/                      # Contiene archivos de texto con los datos de entrada
├── 🖼️ img/                       # Carpeta para almacenar las imágenes generadas
├── 📂 src/                       # Contiene las implementaciones auxiliares
├── 📈 grafico.py                 # Código principal para generar gráficos
├── ⚙️ main.py                    # Implementación del algoritmo desarrollado por Programación Dinámica 
├── 📄 Informe_TP2.pdf            # Informe detallado del proyecto
├── 📑 README.md                  # Documentación del proyecto
└── ▶️ ejecutar_graficos.sh       # Script bash para ejecutar los gráficos
```

## Requisitos

Antes de ejecutar el script, asegúrese de tener instalados los siguientes requisitos:

- **Python 3.x**
- **Librerías Python:**
  - `matplotlib`
  - `numpy`
  - `scipy`

Puede instalar estas dependencias como se detalla en [README.md](../README.md).

-----------------

### Posibles ejecuciones:

1. [Cómo ejecutar el programa con un set de datos](#cómo-ejecutar-el-programa)
2. [Cómo ejecutar los gráficos de las simulaciones](#cómo-ejecutar-los-gráficos)

-----------------
### Cómo ejecutar el programa

#### 1. Clonar el repositorio o descargar los archivos

Primero, asegúrese de que todos los archivos necesarios estén presentes en su directorio de trabajo, como se detalla en [README.md](../README.md).

#### 2. Ejecución desde la terminal

#### Formato de los archivos de entrada

Los archivos de entrada **deben estar en formato `.txt`** y pueden estar ubicados en cualquier carpeta, pero es necesario que al ejecutar el programa se proporcione la **ruta absoluta** del archivo. Además, deben contener **únicamente valores numéricos** separados por `;`. Asegúrate de que no haya otros caracteres, como letras o símbolos, en el archivo. El programa ignorará cualquier línea de comentario que comience con `#`.

> ⚠️ **Importante**: Si desea que su archivo de entrada sea integrado en la ejecución de gráficos, deberá agregarlo a la carpeta `/data`. 

> Para ejecutar los gráficos, lea la sección [Cómo ejecutar los gráficos](#cómo-ejecutar-los-gráficos).

#### Ejemplo de ejecución de un archivo de entrada válido:

```
455;852;725;410;835;239;404;462;629;587;171;604;826;838;384;336;21;125;378;217
```

Para ejecutar el programa pasando por parámetro un archivo con los datos de monedas, sigue los siguientes pasos:

1. Abre la terminal y navega al directorio donde está el archivo `main.py`.

2. Ejecuta el siguiente comando, reemplazando `<ruta_set_datos>` por la ruta **absoluta** del archivo de entrada:

   ```bash
   py main.py <ruta_set_datos>
   ```

#### Detalles de la ejecución:

Al ejecutar el programa, este procesará el archivo, simulará el juego y devolverá la secuencia de jugadas junto con el total de monedas obtenidas por Sophia y Mateo.

El archivo de entrada no requiere que conozcas la solución esperada. El propósito de este programa es resolver el problema y determinar qué jugador obtiene la mayor cantidad de monedas con una estrategia óptima.

#### Ejemplo de salida:
   ```bash
      Sophia debe agarrar la ultima (217) 
      Mateo agarra la primera (455)
      [...]
      Mateo agarra la ultima (21)
      ---------------------
      Total de Sophia: 5234
      Total de Mateo: 4264
   ```

-----------------
### Cómo ejecutar los gráficos

#### 1. Clonar el repositorio o descargar los archivos

Primero, asegúrese de que todos los archivos necesarios estén presentes en su directorio de trabajo, como se detalla en [README.md](../README.md).

#### 2. Dar permisos de ejecución al script

Antes de ejecutar el script `.sh`, asegúrese de otorgarle permisos de ejecución. Desde la terminal, navegue al directorio del proyecto y ejecute:

```
chmod +x ejecutar_graficos.sh
```

#### 3. Ejecutar el script

Para ejecutar el script y seleccionar el gráfico deseado, simplemente ejecute el archivo `.sh` desde la terminal de la siguiente manera:

```
sh ejecutar_graficos.sh
```

Se le presentarán tres opciones para generar gráficos:

1. **Tiempo de ejecución vs Cantidad de elementos:**  
   Genera un gráfico que muestra el tiempo que tarda el algoritmo en ejecutarse en función de la cantidad de elementos en la lista.

2. **Puntos de Sophia y Mateo vs Cantidad de elementos:**  
   Muestra un gráfico con los puntos acumulados por Sophia y Mateo para distintas cantidades de elementos en la lista.

3. **X victorias de Sophia vs Cantidad de juegos simulados:**  
   Simula `n` juegos y muestra un gráfico con las veces que ganó Sophia.

4. **Tiempo de ejecución vs Variabilidad de elementos**: 
   Evalúa cómo afecta la variabilidad en los valores de las monedas al tiempo de ejecución del algoritmo.

5. **Tiempo de ejecución de la Reconstrucción vs Cantidad de elementos**: 
   Analiza el tiempo necesario para reconstruir la secuencia de decisiones óptimas a medida que aumenta la cantidad de monedas.

#### Simulación personalizada

Si elige la opción 3 para simular los juegos de Sophia y Mateo, se le pedirá que ingrese la cantidad de juegos a simular. Puede dejar el campo vacío para usar un valor predeterminado (1000) o ingresar un número entero positivo menor o igual a 10,000. En caso de ingresar un valor mayor a 10,000, se mostrará un mensaje de error.

```
Ingrese la cantidad de juegos a simular (o deje en blanco para valor por defecto): 
```

#### Ejemplo de Ejecución

```
Seleccione qué gráfico desea ejecutar:
1) Tiempo de ejecución vs Cantidad de elementos
2) Puntos de Sophia y Mateo vs Cantidad de elementos
3) X victorias de Sophia vs Cantidad de juegos simulados
4) Tiempo de ejecución vs Variabilidad de elementos
5) Tiempo de ejecución de la Reconstruccion vs Cantidad de elementos
Ingrese una opción (1-5): 1
```

#### Notas adicionales

- Los graficos se generan con set de datos randoms, puede modificar los límites de los respectivos valores en las constantes de cada archivo dedicado a un gráfico.
- En caso de que no se generen los gráficos o haya algún error en la ejecución, consulte los permisos de los archivos y asegúrese de tener instaladas las dependencias correctamente y estar en el directorio adecuado.

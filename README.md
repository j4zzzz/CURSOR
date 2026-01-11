# CURSOR

# Cursor con Python: desarrollo inteligente con IA

Este repositorio contiene el entregable final del curso **"Python + Cursor: Smarter Development with AI"** de Santander Open Academy.

## Objetivo
El propósito de este código es demostrar la capacidad de utilizar **Cursor (AI Powered IDE)** para acelerar el desarrollo de software, la generación de pruebas y la documentación.


# Ejercicios

Este repositorio contiene los ejercicios prácticos realizados durante el curso de **Santander Open Academy** sobre desarrollo asistido por IA.


### 1. Reto: Números Primos (`/Ej1_primos`)
Ejercicio para poner a prueba la capacidad de optimización de la IA.
* **Flujo de trabajo:**
    1. Escribí la función base manualmente.
    2. Solicité a Cursor: *"Optimiza la función para que sea más rápida"*.
    3. Resultado: Implementación del límite de raíz cuadrada (`sqrt(n)`).

### 2. Proyecto: Contador de Palabras (`/Ej2_contador`)
Mini-proyecto siguiendo el tutorial paso a paso del curso.
* **Funcionalidades:**
    * Lectura de archivos de texto local.
    * Uso de Expresiones Regulares (`re`) sugeridas por la IA para limpiar el texto.
    * Conteo de frecuencias usando `collections.Counter`.
* **Manejo de Errores:** Se implementó `try-except` para capturar casos donde el archivo no existe, siguiendo las sugerencias del chat de Cursor.

## Experiencia con el Flujo de Trabajo en Cursor
Siguiendo la metodología del curso, apliqué el siguiente ciclo:
1. **Escritura manual** del esqueleto del código.
2. Uso de **Ctrl+K** para generar el código repetitivo (boilerplate) del manejo de archivos.
3. Uso del **Chat** para entender cómo usar la librería `re` (Regex).
4. Ejecución en terminal integrada para validar resultados.

## Cómo probar el código
1. Navega a la carpeta del contador:
   `cd Ej2_contador`
2. Ejecuta el script:
   `python contador_palabras.py`
3. Cuando pida el archivo, escribe: `texto_prueba.txt`


---

## 🛠 Ejercicios Adicionales de Consolidación

Para reforzar el aprendizaje, se realizaron tres ejercicios extra abarcando lógica, algoritmos y ciencia de datos.

### 3. Ejercicio A: Calculadora Interactiva (`/ejercicio_calculadora`)
* **Reto:** Crear un bucle infinito que solo termine con el comando "salir".
* **Aporte de la IA:** * Pregunté al chat: *"¿Cómo repito un ciclo hasta que el usuario ponga 'salir'?"*.
    * Cursor sugirió la estructura `while True` con un `break` condicional.
    * Ayudó a implementar el manejo de errores `try-except` para inputs no numéricos.

### 4. Ejercicio B: FizzBuzz (`/ejercicio_fizzbuzz`)
* **Reto:** Algoritmo clásico de entrevistas técnicas.
* **Aporte de la IA:** * Probé la capacidad de **autocompletado (Tab)**.
    * Solo escribí el encabezado del loop `for` y Cursor sugirió correctamente toda la lógica de los módulos `% 3` y `% 5`.

### 5. Ejercicio C: Análisis de Datos (`/ejercicio_datos`)
* **Reto:** Manipulación de CSV y generación de gráficas.
* **Aporte de la IA:** * Escribió el código para importar `pandas` y cargar el CSV.
    * Generó automáticamente el código de `matplotlib` para crear un gráfico de dispersión (scatter plot) con etiquetas correctas, algo que manualmente requiere recordar mucha sintaxis específica.

---
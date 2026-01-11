import re
from collections import Counter
import sys

# Proyecto: Contador de palabras
# Planificación realizada en Cursor:
# 1. Pedir al usuario la ruta de un archivo.
# 2. Leer contenido.
# 3. Separar palabras.
# 4. Contar total.
# 5. Mostrar frecuencias.

def analizar_archivo():
    # Paso 1: Pedir ruta
    archivo = input("Introduce la ruta del archivo de texto (ej: texto_prueba.txt): ")

    try:
        # Paso 2: Leer archivo (Cursor sugirió encoding utf-8)
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()
            
    except FileNotFoundError:
        print("Error: El archivo especificado no existe.")
        sys.exit(1)

    # Paso 3: Separar en palabras usando Regex (Sugerencia de IA)
    palabras = re.findall(r"\w+", texto.lower())

    # Paso 4: Contar total
    total_palabras = len(palabras)
    print(f"\n--- Resultados ---")
    print(f"Total palabras encontradas: {total_palabras}")

    # Paso 5: Frecuencias con Counter
    if total_palabras > 0:
        contador = Counter(palabras)
        mas_comunes = contador.most_common(10)

        print("\nPalabras más frecuentes:")
        for palabra, freq in mas_comunes:
            print(f"- {palabra}: {freq}")

if __name__ == "__main__":
    analizar_archivo()
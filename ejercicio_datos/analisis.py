    import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio C: Análisis de Datos Básico
# Objetivo: Usar Cursor para generar código de Pandas y Matplotlib.

def analizar_datos():
    # Prompt usado: "Lee el archivo datos.csv usando pandas"
    try:
        df = pd.read_csv('datos.csv')
        
        print("--- Estadísticas Básicas (Generadas por Pandas) ---")
        # Prompt: "Calcula media y desviación estándar de las columnas"
        print(df.describe())

        # Prompt: "Genera un scatter plot de ventas vs gastos"
        plt.figure(figsize=(8, 6))
        plt.scatter(df['ventas'], df['gastos'], color='blue', alpha=0.5)
        plt.title('Análisis de Ventas vs Gastos')
        plt.xlabel('Ventas')
        plt.ylabel('Gastos')
        plt.grid(True)
        
        print("\nGenerando gráfico...")
        plt.show()

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'datos.csv'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    analizar_datos()
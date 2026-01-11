import math

# Reto: Determinar si un número es primo
# Código generado con asistencia de Cursor y optimizado bajo sugerencia

def es_primo(n):
    """
    Verifica si n es primo.
    Optimización sugerida por IA: Iterar solo hasta la raíz cuadrada de n.
    """
    if n <= 1:
        return False
    
    # La IA sugirió usar int(math.sqrt(n)) + 1 para eficiencia
    limite = int(math.sqrt(n)) + 1
    
    for i in range(2, limite):
        if n % i == 0:
            return False
            
    return True

# Bloque de prueba sugerido por la IA
if __name__ == "__main__":
    numeros_prueba = [2, 3, 4, 17, 20, 97]
    for num in numeros_prueba:
        resultado = "Es primo" if es_primo(num) else "No es primo"
        print(f"El número {num}: {resultado}")
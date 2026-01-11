# Ejercicio A: Calculadora Simple
# Objetivo: Probar loops infinitos y manejo de errores con ayuda de Cursor.

def calculadora():
    print("--- Calculadora Asistida por IA ---")
    print("Escribe 'salir' en la operación para terminar.")

    # Cursor sugirió usar un loop 'while True' para mantener el programa vivo
    while True:
        operacion = input("\nIngresa operación (+, -, *, /) o 'salir': ").lower()

        if operacion == 'salir':
            print("Saliendo de la calculadora...")
            break

        if operacion not in ['+', '-', '*', '/']:
            print("Operación no válida.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Lógica generada para manejar las operaciones
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                # Cursor sugirió manejar la división por cero aquí
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2
            
            print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: Por favor ingresa números válidos.")

if __name__ == "__main__":
    calculadora()
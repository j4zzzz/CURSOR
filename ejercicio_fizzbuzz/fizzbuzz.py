# Ejercicio B: FizzBuzz
# Objetivo: Dejar que la IA autocomplete la lógica del bucle for.

def fizzbuzz():
    print("--- FizzBuzz (1 al 50) ---")
    
    # Escribí "for i in range(1, 51):" y Cursor generó el resto:
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
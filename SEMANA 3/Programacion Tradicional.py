# Comparación de Programación Tradicional y POO en Python

# --- Programación Tradicional ---
# Código utilizando estructuras de funciones

def ingresar_temperaturas():
    """Solicita al usuario que ingrese las temperaturas diarias."""
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio semanal de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

# Flujo principal del programa (Programación Tradicional)
print("--- Programación Tradicional ---")
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")


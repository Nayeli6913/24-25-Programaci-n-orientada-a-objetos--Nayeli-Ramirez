# --- Programación Orientada a Objetos (POO) ---
# Código utilizando el paradigma de POO

class ClimaSemanal:
    """Clase que representa la información del clima semanal."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Permite al usuario ingresar las temperaturas diarias."""
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Calcula el promedio semanal de temperaturas."""
        return sum(self.temperaturas) / len(self.temperaturas)

# Flujo principal del programa (POO)
print("\n--- Programación Orientada a Objetos ---")
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio_poo = clima.calcular_promedio()
print(f"El promedio semanal de temperaturas es: {promedio_poo:.2f} °C")

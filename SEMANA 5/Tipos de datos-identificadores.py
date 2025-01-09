# Programa que calcula el área de un círculo dado su radio.
# El área es calculada usando la fórmula A = π * radio^2.
# Además, convierte el área de metros cuadrados a centímetros cuadrados.

import math

def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo dada su radio.
    """
    # Usamos la fórmula A = π * radio^2
    area = math.pi * radio ** 2
    return area

def convertir_a_centimetros_cuadrados(area_metros_cuadrados):
    """
    Convierte el área de metros cuadrados a centímetros cuadrados.
    """
    area_centimetros_cuadrados = area_metros_cuadrados * 10000  # 1 metro cuadrado = 10000 cm²
    return area_centimetros_cuadrados

# Solicitar al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo en metros: "))

# Calcular el área en metros cuadrados
area_metros = calcular_area_circulo(radio)

# Convertir el área a centímetros cuadrados
area_centimetros = convertir_a_centimetros_cuadrados(area_metros)

# Mostrar los resultados
print(f"El área del círculo con radio {radio} metros es: {area_metros:.2f} metros cuadrados.")
print(f"El área en centímetros cuadrados es: {area_centimetros:.2f} cm².")

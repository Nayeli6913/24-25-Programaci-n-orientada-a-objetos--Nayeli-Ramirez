# Clase base: Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público

    def descripcion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"

    def mover(self):
        return "El vehículo está en movimiento"


# Clase derivada: Coche (hereda de Vehículo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Herencia
        self.__num_puertas = num_puertas  # Atributo privado (encapsulación)

    # Método para acceder al atributo encapsulado
    def get_num_puertas(self):
        return self.__num_puertas

    # Método sobrescrito (polimorfismo)
    def mover(self):
        return f"El coche {self.marca} está conduciendo por la carretera"


# Clase derivada: Bicicleta (hereda de Vehículo)
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Atributo público específico de Bicicleta

    # Método sobrescrito (polimorfismo)
    def mover(self):
        return f"La bicicleta {self.marca} está siendo pedaleada por el ciclista"


# Instancias y demostración
if __name__ == "__main__":
    # Crear un vehículo genérico
    vehiculo = Vehiculo("Genérico", "2023")
    print(vehiculo.descripcion())
    print(vehiculo.mover())

    # Crear un coche
    coche = Coche("Mazda", "Corolla", 4)
    print(coche.descripcion())
    print(f"El coche tiene {coche.get_num_puertas()} puertas")
    print(coche.mover())

    # Crear una bicicleta
    bicicleta = Bicicleta("Giant", "Escape 3", "Montaña")
    print(bicicleta.descripcion())
    print(bicicleta.mover())

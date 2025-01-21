class Moto:
    def __init__(self, marca, modelo):
        # Constructor: inicializa los atributos del objeto
        self.marca = marca
        self.modelo = modelo
        print(f"Una moto {self.marca} {self.modelo} ha sido creada.")

    def __del__(self):
        # Destructor: limpia los recursos o muestra un mensaje cuando el objeto se destruye
        print(f"La moto {self.marca} {self.modelo} ha sido destruida.")

# Crear un objeto de la clase Moto
mi_moto = Moto("Suzuki", "Grand Vitara ")

# Destruir el objeto explícitamente (aunque Python lo maneja automáticamente)
del mi_moto

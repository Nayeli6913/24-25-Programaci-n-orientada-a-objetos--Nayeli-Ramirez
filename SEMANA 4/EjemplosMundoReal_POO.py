# Clase que representa una cuenta de inversión
class CuentaInversion:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, tasa_interes=0.01):
        """
        Inicializa los atributos de la cuenta de inversión.
        :param numero_cuenta: Número único de la cuenta.
        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto, 0).
        :param tasa_interes: Tasa de interés mensual (por defecto, 1%).
        """
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
        self.tasa_interes = tasa_interes

    def depositar(self, cantidad):
        """
        Añade dinero al saldo de la cuenta.
        :param cantidad: Monto a depositar.
        """
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "El monto a depositar debe ser mayor a cero."

    def retirar(self, cantidad):
        """
        Retira dinero del saldo de la cuenta.
        :param cantidad: Monto a retirar.
        """
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        elif cantidad > 0:
            self.saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "El monto a retirar debe ser mayor a cero."

    def agregar_rendimiento(self):
        """
        Agrega rendimientos al saldo basado en la tasa de interés mensual.
        """
        rendimiento = self.saldo * self.tasa_interes
        self.saldo += rendimiento
        return f"Rendimiento agregado: ${rendimiento:.2f}. Nuevo saldo: ${self.saldo:.2f}"

    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        return f"Saldo actual de la cuenta {self.numero_cuenta}: ${self.saldo}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta de inversión
    cuenta = CuentaInversion("345678901", "Carlos Torres", 5000, 0.02)

    # Mostrar saldo inicial
    print(cuenta.mostrar_saldo())

    # Realizar un depósito
    print(cuenta.depositar(1500))

    # Intentar un retiro mayor al saldo
    print(cuenta.retirar(7000))

    # Realizar un retiro válido
    print(cuenta.retirar(2000))

    # Agregar rendimiento mensual
    print(cuenta.agregar_rendimiento())

    # Mostrar saldo final
    print(cuenta.mostrar_saldo())

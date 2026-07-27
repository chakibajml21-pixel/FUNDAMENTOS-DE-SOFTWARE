# banco_central.py
# Semana 6 - Patron de diseno SINGLETON.
#
# Problema: en la Fintech Quantum Core NO queremos que se cree un "Banco Central"
# nuevo cada vez que alguien hace un pago (eso causaria caos con los saldos y
# gastaria memoria). Necesitamos UNA sola instancia en todo el sistema.
#
# Solucion: el patron Singleton garantiza una unica instancia y un punto de
# acceso global a ella.
#
# Para ejecutar:  python banco_central.py


# gestor_banco.py
# Semana 6 - Patrón de Diseño Singleton
#
# Este ejemplo representa el administrador principal del sistema bancario.
# Solo puede existir un único GestorBanco durante la ejecución del programa,
# ya que toda la información de clientes, cuentas y transacciones debe ser
# compartida por el mismo objeto.

class GestorBanco:
    """Singleton que administra toda la información del banco."""

    # Única instancia del sistema
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            # Estos atributos solo se crean una vez
            cls._instancia.clientes = []
            cls._instancia.cuentas = []
            cls._instancia.transacciones = []

        return cls._instancia

    # ==========================
    # Métodos del sistema
    # ==========================

    def agregar_cliente(self, nombre):
        self.clientes.append(nombre)
        print(f"Cliente '{nombre}' registrado correctamente.")

    def agregar_cuenta(self, numero):
        self.cuentas.append(numero)
        print(f"Cuenta {numero} creada.")

    def registrar_transaccion(self, descripcion):
        self.transacciones.append(descripcion)
        print("Transacción registrada.")

    def mostrar_resumen(self):
        print("\n========== RESUMEN DEL BANCO ==========")
        print("Clientes registrados:", len(self.clientes))
        print("Cuentas creadas:", len(self.cuentas))
        print("Transacciones realizadas:", len(self.transacciones))


# ==========================================
# Demostración del patrón Singleton
# ==========================================

if __name__ == "__main__":

    gestor1 = GestorBanco()
    gestor2 = GestorBanco()

    print("ID del gestor1:", id(gestor1))
    print("ID del gestor2:", id(gestor2))
    print("¿Son el mismo objeto?", gestor1 is gestor2)

    print("\n--- Registrando información ---")

    gestor1.agregar_cliente("Carlos Gómez")
    gestor2.agregar_cliente("Laura Martínez")

    gestor1.agregar_cuenta("1001")
    gestor2.agregar_cuenta("1002")

    gestor1.registrar_transaccion("Depósito de $500.000")
    gestor2.registrar_transaccion("Retiro de $120.000")

    gestor1.mostrar_resumen()

    print("\nClientes:", gestor2.clientes)
    print("Cuentas:", gestor2.cuentas)
    print("Transacciones:", gestor2.transacciones)

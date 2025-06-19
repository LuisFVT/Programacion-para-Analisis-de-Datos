import json

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación: {self.numero} - Tipo: {self.tipo} - Precio: ${self.precio} - Estado: {estado}"

    def to_dict(self):
        return {
            "numero": self.numero,
            "tipo": self.tipo,
            "precio": self.precio,
            "disponible": self.disponible
        }

class Persona:
    def __init__(self, nombre, apellido, metodo_pago):
        self.nombre = nombre
        self.apellido = apellido
        self.metodo_pago = metodo_pago

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido} - Método de pago: {self.metodo_pago}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, metodo_pago):
        super().__init__(nombre, apellido, metodo_pago)
        self.reserva = []

    def agregar_reserva(self, habitacion):
        self.reserva.append(habitacion)

    def reservas_info(self):
        return [f"{hab.numero} ({hab.tipo}) - ${hab.precio}" for hab in self.reserva]

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.clientes = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [hab for hab in self.habitaciones if hab.disponible]
        if disponibles:
            print("\n--- Habitaciones disponibles ---")
            for hab in disponibles:
                print(hab)
        else:
            print("No hay habitaciones disponibles actualmente.")
        return disponibles

    def reservar_habitacion(self, cliente, numero_habitacion):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion and h.disponible), None)
        if habitacion:
            habitacion.disponible = False
            cliente.agregar_reserva(habitacion)
            print(f"\n✅ Reserva exitosa para {cliente.nombre} {cliente.apellido}:")
            print(f"  Habitación: {habitacion.numero} - Tipo: {habitacion.tipo} - Precio: ${habitacion.precio}")
            print(f"  Método de pago: {cliente.metodo_pago}")
            self.guardar_reserva_json(cliente, habitacion)
        else:
            print("❌ No se pudo realizar la reserva. Verifique el número de habitación o la disponibilidad.")

    def guardar_reserva_json(self, cliente, habitacion):
        reserva = {
            "cliente": {
                "nombre": cliente.nombre,
                "apellido": cliente.apellido,
                "metodo_pago": cliente.metodo_pago
            },
            "habitacion": habitacion.to_dict()
        }
        try:
            with open("reservas.json", "r", encoding="utf-8") as f:
                reservas = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            reservas = []

        reservas.append(reserva)
        with open("reservas.json", "w", encoding="utf-8") as f:
            json.dump(reservas, f, ensure_ascii=False, indent=4)

    def mostrar_resumen_reservas(self):
        print("\n--- Resumen de Reservas ---")
        try:
            with open("reservas.json", "r", encoding="utf-8") as f:
                reservas = json.load(f)
            if not reservas:
                print("No hay reservas registradas.")
                return
            for i, r in enumerate(reservas, 1):
                c = r["cliente"]
                h = r["habitacion"]
                print(f"{i}. {c['nombre']} {c['apellido']} - Habitación {h['numero']} ({h['tipo']}) - ${h['precio']}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No hay reservas registradas.")

    def cargar_reservas(self):
        try:
            with open("reservas.json", "r", encoding="utf-8") as f:
                reservas = json.load(f)
            for r in reservas:
                numero = r["habitacion"]["numero"]
                habitacion = next((h for h in self.habitaciones if h.numero == numero), None)
                if habitacion:
                    habitacion.disponible = False
        except (FileNotFoundError, json.JSONDecodeError):
            pass

# --- Interfaz para el usuario ---
def main():
    hotel = Hotel("Hotel Python")

    # Inicialización de habitaciones
    hotel.habitaciones = [
        Habitacion(101, "Simple", 50),
        Habitacion(102, "Doble", 80),
        Habitacion(103, "Suite", 120),
        Habitacion(104, "Triple", 100),
        Habitacion(105, "Familiar", 150),
        Habitacion(201, "Simple", 55),
        Habitacion(202, "Doble", 85),
        Habitacion(203, "Suite", 130),
        Habitacion(204, "Triple", 110),
        Habitacion(205, "Familiar", 160)
    ]

    # Cargar reservas anteriores y actualizar disponibilidad
    hotel.cargar_reservas()

    print("🛎️ Bienvenido al sistema de reservas del Hotel Python.")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    metodo_pago = input("Ingrese su método de pago: ")

    cliente = Cliente(nombre, apellido, metodo_pago)
    hotel.registrar_cliente(cliente)

    disponibles = hotel.mostrar_habitaciones_disponibles()
    if not disponibles:
        return

    try:
        numero_habitacion = int(input("\nIngrese el número de la habitación que desea reservar: "))
    except ValueError:
        print("Número de habitación inválido.")
        return

    hotel.reservar_habitacion(cliente, numero_habitacion)

    hotel.mostrar_resumen_reservas()

if __name__ == "__main__":
    main()

class Plato:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def mostrar_informacion(self):
        print(f"\n🍽️ Tipo de plato: {self.nombre}")
        print(f"💰 Precio: {self.precio} MXN")
        print(f"📄 Descripción: {self.descripcion}")

class ArrozFrito(Plato):
    def __init__(self, precio, descripcion, ingredientes):
        super().__init__("Arroz Frito", precio, descripcion)
        self.ingredientes = ingredientes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"🥗 Ingredientes: {', '.join(self.ingredientes)}")

class ChowFan(Plato):
    def __init__(self, precio, descripcion, tipo_arroz):
        super().__init__("Chow Fan", precio, descripcion)
        self.tipo_arroz = tipo_arroz

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"🍚 Tipo de arroz: {', '.join(self.tipo_arroz)}")

# --- Interacción con el usuario ---
print("📋 Crear un nuevo plato")
tipo = input("Tipo de plato (ArrozFrito / ChowFan): ").strip()

precio = input("Precio (MXN): ")
descripcion = input("Descripción del plato: ")

if tipo.lower() == "arrozfrito":
    ingredientes = input("Ingredientes (separados por comas): ").split(",")
    plato = ArrozFrito(precio, descripcion, [i.strip() for i in ingredientes])
elif tipo.lower() == "chowfan":
    tipo_arroz = input("Tipo de arroz (separado por comas): ").split(",")
    plato = ChowFan(precio, descripcion, [t.strip() for t in tipo_arroz])
else:
    print("❌ Tipo no válido.")
    plato = None

# Mostrar información
if plato:
    plato.mostrar_informacion()

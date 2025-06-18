import json
import os

class Plato:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def mostrar_informacion(self):
        print(f"\n🍽️ Plato: {self.nombre}")
        print(f"💰 Precio: {self.precio} MXN")
        print(f"📄 Descripción: {self.descripcion}")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "descripcion": self.descripcion
        }

class ArrozFrito(Plato):
    def __init__(self, precio, descripcion, ingredientes):
        super().__init__("Arroz Frito", precio, descripcion)
        self.ingredientes = ingredientes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"🥗 Ingredientes: {', '.join(self.ingredientes)}")

    def to_dict(self):
        data = super().to_dict()
        data["ingredientes"] = self.ingredientes
        return data

class ChowFan(Plato):
    def __init__(self, precio, descripcion, tipo_arroz):
        super().__init__("Chow Fan", precio, descripcion)
        self.tipo_arroz = tipo_arroz

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"🍚 Tipo de arroz: {', '.join(self.tipo_arroz)}")

    def to_dict(self):
        data = super().to_dict()
        data["tipo_arroz"] = self.tipo_arroz
        return data

def guardar_plato_json(plato, archivo="platos.json"):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            platos = json.load(f)
    else:
        platos = []

    platos.append(plato.to_dict())

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(platos, f, ensure_ascii=False, indent=4)

def mostrar_todos_los_platos(archivo="platos.json"):
    if not os.path.exists(archivo):
        print("📂 No hay platos guardados aún.")
        return

    with open(archivo, "r", encoding="utf-8") as f:
        platos = json.load(f)

    print("\n📖 Lista de platos guardados:")
    for i, plato in enumerate(platos, 1):
        print(f"\n🔹 Plato #{i}")
        print(f"Tipo: {plato['nombre']}")
        print(f"Precio: {plato['precio']} MXN")
        print(f"Descripción: {plato['descripcion']}")
        if "ingredientes" in plato:
            print(f"Ingredientes: {', '.join(plato['ingredientes'])}")
        if "tipo_arroz" in plato:
            print(f"Tipo de arroz: {', '.join(plato['tipo_arroz'])}")

def agregar_plato():
    print("\n📋 Agregar nuevo plato")
    print("1. Arroz Frito")
    print("2. Chow Fan")
    opcion = input("Selecciona el tipo de plato (1 o 2): ")

    if opcion not in ["1", "2"]:
        print("❌ Opción inválida.")
        return

    try:
        precio = float(input("💰 Precio (MXN): "))
    except ValueError:
        print("❌ El precio debe ser un número.")
        return

    descripcion = input("📄 Descripción: ")

    if opcion == "1":
        ingredientes = input("🥗 Ingredientes (separados por comas): ").split(",")
        plato = ArrozFrito(precio, descripcion, [i.strip() for i in ingredientes])
    else:
        tipo_arroz = input("🍚 Tipo de arroz (separado por comas): ").split(",")
        plato = ChowFan(precio, descripcion, [t.strip() for t in tipo_arroz])

    plato.mostrar_informacion()
    guardar_plato_json(plato)
    print("✅ Plato guardado exitosamente.")

# --- Menú principal ---
def menu():
    while True:
        print("\n========= MENÚ =========")
        print("1. Agregar un plato")
        print("2. Ver platos guardados")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_plato()
        elif opcion == "2":
            mostrar_todos_los_platos()
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()

class Carro: 
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año

    def encender(self):
        print(f"El carro {self.marca} {self.modelo} está encendido.")

class Deportivo(Carro):
    def __init__(self, marca, modelo, color, año, velocidad_max, caballos_fuerza):
        Carro.__init__(self, marca, modelo, color, año)
        self.velocidad_max = velocidad_max
        self.caballos_fuerza = caballos_fuerza

    def describir(self):
        print(f"Deportivo: {self.marca} {self.modelo}, Color: {self.color}, Año: {self.año}, "
              f"Velocidad máxima: {self.velocidad_max} km/h, Caballos de fuerza: {self.caballos_fuerza}")

class Electrico(Carro):
    def __init__(self, marca, modelo, color, año, autonomia, tiempo_carga):
        Carro.__init__(self, marca, modelo, color, año)
        self.autonomia = autonomia
        self.tiempo_carga = tiempo_carga

    def describir(self):
        print(f"Eléctrico: {self.marca} {self.modelo}, Color: {self.color}, Año: {self.año}, "
              f"Autonomía: {self.autonomia} km, Tiempo de carga: {self.tiempo_carga} h")

class Hibrido(Deportivo, Electrico):
    def __init__(self, marca, modelo, color, año, velocidad_max, caballos_fuerza, autonomia, tiempo_carga, modo_hibrido):
        Carro.__init__(self, marca, modelo, color, año)
        self.velocidad_max = velocidad_max
        self.caballos_fuerza = caballos_fuerza
        self.autonomia = autonomia
        self.tiempo_carga = tiempo_carga
        self.modo_hibrido = modo_hibrido

    def describir(self):
        print(f"Híbrido: {self.marca} {self.modelo}, Color: {self.color}, Año: {self.año}, "
              f"Velocidad máxima: {self.velocidad_max} km/h, Caballos de fuerza: {self.caballos_fuerza}, "
              f"Autonomía: {self.autonomia} km, Tiempo de carga: {self.tiempo_carga} h, "
              f"Modo híbrido: {self.modo_hibrido}")

# Instancias de carros deportivos
deportivos = [
    Deportivo("Ferrari", "488 Spider", "Rojo", 2022, 330, 670),
    Deportivo("Lamborghini", "Huracán EVO", "Amarillo", 2021, 325, 640),
    Deportivo("Porsche", "911 Turbo S", "Negro", 2023, 330, 650),
    Deportivo("McLaren", "720S", "Naranja", 2020, 341, 710)
]

# Instancias de carros eléctricos
electricos = [
    Electrico("Tesla", "Model S", "Blanco", 2022, 652, 1.5),
    Electrico("Nissan", "Leaf", "Gris", 2020, 270, 7.5),
    Electrico("BMW", "i3", "Azul", 2019, 246, 6),
    Electrico("Hyundai", "Ioniq 5", "Plata", 2023, 480, 5)
]

# Instancias de carros híbridos
hibridos = [
    Hibrido("Toyota", "Prius", "Verde", 2021, 180, 121, 900, 3, "ECO"),
    Hibrido("Honda", "Insight", "Azul", 2020, 200, 151, 880, 2.5, "Normal"),
    Hibrido("Ford", "Fusion Hybrid", "Negro", 2019, 190, 188, 850, 3.5, "Sport"),
    Hibrido("Lexus", "UX 250h", "Gris", 2022, 177, 181, 870, 4, "EV Mode")
]

# Mostrar la descripción de todos los carros
print("=== CARROS DEPORTIVOS ===")
for d in deportivos:
    d.describir()

print("\n=== CARROS ELÉCTRICOS ===")
for e in electricos:
    e.describir()

print("\n=== CARROS HÍBRIDOS ===")
for h in hibridos:
    h.describir()

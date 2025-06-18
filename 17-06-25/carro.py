#clase base

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El carro {self.marca} {self.modelo} ha arrancado."

    def detener(self):
        return f"El carro {self.marca} {self.modelo} se ha detenido."

    def encender(self):
        print(f"El carro {self.marca} {self.modelo} se ha encendido.")

class Deportivo(Carro):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

    def describir(self):
        super().encender()
        print("Este es un carro deportivo con la velocidad máxima de", self.velocidad_maxima, "km/h, marca", self.marca, "y modelo", self.modelo)

class Electrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

    def describir(self):
        super().encender()
        print("Este es un carro eléctrico con una autonomía de", self.autonomia, "km, marca", self.marca, "y modelo", self.modelo)



carrito= Carro("Toyota", "Corolla")
carrito_deportivo = Deportivo("Porsche", "911", 320)
carrito_electrico = Electrico("BMW", "i3", 200)


# Demostración de métodos y atributos de los objetos

# Métodos de Carro base
print(carrito.arrancar())
print(carrito.detener())

# Métodos y atributos de Deportivo
print(carrito_deportivo.arrancar())
print(carrito_deportivo.detener())
carrito_deportivo.describir()
print(f"Velocidad máxima: {carrito_deportivo.velocidad_maxima} km/h")
print(f"Marca: {carrito_deportivo.marca}")
print(f"Modelo: {carrito_deportivo.modelo}")

# Métodos y atributos de Electrico
print(carrito_electrico.arrancar())
print(carrito_electrico.detener())
carrito_electrico.describir()
print(f"Autonomía: {carrito_electrico.autonomia} km")
print(f"Marca: {carrito_electrico.marca}")
print(f"Modelo: {carrito_electrico.modelo}")

# Atributos de Carro base
print(f"Marca base: {carrito.marca}")
print(f"Modelo base: {carrito.modelo}")

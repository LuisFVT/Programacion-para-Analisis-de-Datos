class Carro:
    def __init__(self, marca, modelo,):
        self.__marca = marca
        self.__modelo = modelo
        self.encendico = False

    def encender(self):
        self.encendido = True
        print(f"El carro {self.__marca} {self.__modelo} está encendido.")

    def apagar(self):
        self.encendido = False
        print(f"El carro {self.__marca} {self.__modelo} está apagado.")

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nueva_marca):
        if isinstance(nueva_marca, str):
            self.__marca = nueva_marca
        else:
            print("Marca Invalida.")

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, str):
            self.__modelo = nuevo_modelo
        else:
            print("Modelo Invalido.")  
    
class Electrico (Carro):
    def __init__(self, marca, modelo,bateria ):
        super().__init__(marca, modelo)
        self.__bateria = bateria

    def cargar(self, cantidad):
        if 0 < cantidad <= 100:
            self.__bateria = min(100, self.__bateria + cantidad)    
            print(f"Batería cargada al {self.__bateria}%")
        else:
            print("Cantidad de carga inválida. Debe ser entre 0 y 100.")    
    
    def mostrar_bateria(self):
        print(f"Batería actual: {self.__bateria}%")

tesla = Electrico("Tesla", "Model S", 80)   
tesla.mostrar_bateria()
tesla.encender()

tesla.set_marca ("Tesla Model X")

print(f"Marca del carro: {tesla.get_marca()}")  
tesla.cargar(20)
tesla.cargar(15)
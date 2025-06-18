class Plato:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def show_informacion(self):
        print(f"Plato: {self.get_nombre()} - Precio: {self.get_precio()} MXN")

class ArrozFrito(Plato):
    def __init__(self, ingredientes, precio):
        super().__init__("Arroz Frito", precio)
        self.ingredientes = ingredientes  

    def show_informacion(self):
        super().show_informacion()
        print(f"Ingredientes: {', '.join(self.ingredientes)}")

class ChowFan(Plato):
    def __init__(self, tipo_de_arroz, precio):
        super().__init__("Chow Fan", precio)
        self.tipo_de_arroz = tipo_de_arroz

    def show_informacion(self):
        super().show_informacion()
        print(f"Tipo de Arroz: {', '.join(self.tipo_de_arroz)}")

# Objetos y llamada a métodos
platito = ArrozFrito(["Arroz", "Verduras", "Salsa de soya"], 100)
platito2 = ChowFan(["Arroz integral", "Verduras", "Salsa de soya"], 120)

platito.show_informacion()
print()  # Separador
platito2.show_informacion()

class Animal:  # Define una clase base llamada Animal.
    def sonido(self):  # Método que debería ser implementado por las subclases.
        pass  # No hace nada (método abstracto).

class Capibara(Animal):  # Define una clase Capibara que hereda de Animal.
    def __init__(self, nombre, peso, edad):  # Constructor con nombre, peso y edad.
        self.nombre = nombre  # Asigna el nombre al atributo de instancia.
        self.peso = peso  # Asigna el peso al atributo de instancia.
        self.edad = edad  # Asigna la edad al atributo de instancia.

    def sonido(self):  # Implementa el método sonido para Capibara.
        return "¡Chillido, gruñido sonido de capibara!"  # Devuelve el sonido característico.

    def nadar(self, minutos):  # Método para nadar.
        return f"{self.nombre} nadó por {minutos} minutos."  # Devuelve un mensaje.

    def comida(self):  # Método para obtener la comida favorita.
        return "Hierba y vegetación acuática"

# Creamos un capibara
capi = Capibara("Panchito", 50, 3)  # Instancia un objeto Capibara.

# Probamos sus métodos
print(f"Sonido: {capi.sonido()}")  # Imprime el sonido del capibara.
print(capi.nadar(10))  # Imprime el resultado de nadar 10 minutos.
print(capi.comida())  # Imprime la comida favorita del capibara.

# Mostramos sus atributos
print(f"\nDatos de {capi.nombre}:")  # Imprime el nombre del capibara.
print(f"- Peso: {capi.peso} kg")  # Imprime el peso.
print(f"- Edad: {capi.edad} años")  # Imprime la edad.

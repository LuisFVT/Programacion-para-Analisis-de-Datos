class Novio:
    def __init__(self, nombre, lugares_visitados):  
        self.nombre = nombre  # Asigna el nombre al atributo de instancia.
        self.lugares = lugares_visitados  # Asigna los lugares visitados al atributo de instancia.

        self.contador_ana = 0

    def revisar_fidelidad(self):
        print(f"\n  Analizando las salidas de {self.nombre}:...")
        for lugar in self.lugares:
            if lugar.lower() == "cafetería ana":
                self.contador_ana += 1

        print("\n Resumen final")
        print(f"  {self.nombre} ha visitado la Cafetería Ana {self.contador_ana} veces.")

        if self.contador_ana > 5:
            print("\n Alerta: sospecho, puede que sea infiel")
        elif self.contador_ana > 3:
            print("\n Alerta: sospecho, puede que sea infiel")
        elif self.contador_ana > 1:
            print("\n Puede que sea casualidad, pero no me convence del todo")
        else:
            print("\n Todo en orden, no hay sospechas de infidelidad")

            lugares = [
                "casa de ana",
                "gimnasio",
                "casa de ana",
                "casa de ana",
                "casa de ana",
                "uni",
                "parque",
            ]
            mi_novio = Novio("Juan", lugares)  # Crea una instancia de la clase Novio con nombre y lugares visitados.
            mi_novio.revisar_fidelidad()
            

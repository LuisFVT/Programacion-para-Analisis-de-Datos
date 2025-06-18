class Figura:
    def perimetro(self):
        pass

class Rectangulo(Figura): # type: ignore
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
        
miraRectangulo = Rectangulo (100, 100)
print(miraRectangulo.perimetro())       



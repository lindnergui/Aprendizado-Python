from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    @abstractmethod
    def perimetro(self):
        """Soma de todos os lados"""
        pass
    @abstractmethod
    def area(self):
        """Soma da área"""
        pass

class Quadrado(Poligono):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f'A Área do quadrado é igual a: {self.lado ** 2:.2f} | '
    
    def perimetro(self):
        return f'O perímetro do quadrado é igual a: {self.lado * 4:.2f}'
    
class Circulo(Poligono):

    def __init__(self, raio):
        self.raio = raio
    
    def perimetro(self):
        return f'O perímetro do círculo é igual a: {2 * pi * self.raio:.2f}'
    
    def area(self):
        return f'A Área do círculo é igual a: {pi * self.raio ** 2:.2f} | '
    
class Retangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return f'O perímetro do retângulo é igual a: {2 * (self.base + self.altura):.2f}' 
    
    def area(self):
        return f'A área do retângulo é igual a: {self.base * self.altura:.2f} | '
    
p1 = Quadrado(4)
p2 = Retangulo(4, 5)
p3 = Circulo(4)

print(p1.area(), p1.perimetro())
print(p2.area(), p2.perimetro())
print(p3.area(), p3.perimetro())







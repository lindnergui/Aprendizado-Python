from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass

class moto(Transporte):
    def __init__(self, distancia, fator, frete):
        super().__init__(distancia, frete)
        self.fator = fator


    def calc_frete(self):
        return f'Frete da moto: {(self.distancia * self.frete) * self.fator}'
    
class caminhao(Transporte):
    def __init__(self, distancia, fator, frete):
        super().__init__(distancia, frete)
        self.fator = fator
    
    def calc_frete(self):
        if self.distancia < 50:
            return 'Imposível calcular frete abaixo de 50KM'
        else:
            return f'Frete do caminhão: {(self.distancia * self.frete) * self.fator}'
        
class drone(Transporte):
    def __init__(self, distancia, fator, frete):
        super().__init__(distancia, frete)
        self.fator = fator

    def calc_frete(self):
        if self.distancia > 10:
            return 'Impossível calcular frete acima de 10KM'
        else:
            return f'Frete do drone: {(self.distancia * self.frete) * self.fator}'
    
v1 = moto(30, 0.5, 10)
print(v1.calc_frete())

v2 = caminhao(60, 1.20, 5)
print(v2.calc_frete())

v3 = drone(5, 9.5, 2)
print(v3.calc_frete())


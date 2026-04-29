#Preaparo do café:
#ferver água a 100 C
#agua pressurizada pelo café moído
#servir em xícara
#-------------PRONTO--------------
#Preparo do chá
#Ferver agua a 100 C
#Mergulhar sache na agua
#servir na caneca de porcelana
#--------PRONTO--------
#Preparo do leite
#Ferver água a 100 C 
#passar vapor pelo bico do leite
#servir em caneca com café
#--------PRONTO--------

from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self, preparar, ferver_agua):
        self.preparar = preparar
        self.ferver_agua = ferver_agua

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class cafe(BebidaQuente):
    def __init__(self, preparar, ferver_agua):
        super().__init__(preparar, ferver_agua) 

    def preparando_bebida(self):
        print(f'Preparando {self.preparar}...Ferva água a {self.ferver_agua} graus centígrados')
    
    def misturar(self):
        print('1 -> Água pressurizada pelo café moído')
    
    def servir(self):
        print('2 -> Servir em xícara')
    
class cha(BebidaQuente):
    def __init__(self, preparar, ferver_agua):
        super().__init__(preparar, ferver_agua)

    def preparando_bebida(self):
        print(f'Preparando {self.preparar}...Ferva água a {self.ferver_agua} graus centígrados')

    def misturar(self):
        print('1 -> Mergulhar sachẽ na água')

    def servir(self):
        print('2 -> Servir na caneca de porcelana')
class leite(BebidaQuente):
    def __init__(self, preparar, ferver_agua):
        super().__init__(preparar, ferver_agua)

    def preparando_bebida(self):
        print(f'Preparando {self.preparar}...Ferva água a {self.ferver_agua} graus centígrados')
    
    def misturar(self):
        print('1 -> Passar vapor pelo bico do leite')

    def servir(self):
        print('2 -> Servir em xícara já com café')

b1 = cafe('Café', 100)
b1.preparando_bebida()
b1.misturar()
b1.servir()
print('----------BEBIDA PRONTA----------')

b2 = cha('Chá', 100)
b2.preparando_bebida()
b2.misturar()
b2.servir()
print('----------BEBIDA PRONTA----------')

b3 = leite('Leite', 100)
b3.preparando_bebida()
b3.misturar()
b3.servir()
print('----------BEBIDA PRONTA----------')
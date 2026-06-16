#Declaração de classe
class Gafanhoto:
    """

Essa classe cria um gafanhoto que é uma pessoa
que tem nome e idade.

    """
    def __init__(self, nome = '', idade = 0): #Método  construtor
        #Atributos de instância
        self.nome = nome
        self.idade = idade
        
    #Métodos de identação
    def aniversário(self):
        self.idade += 1
    
    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} é Gafanhoto(a) e tem idade = {self.idade} anos de idade"
#Declaração de objetos
g1 = Gafanhoto('Guilherme', 18)
g1.aniversário()
#print(g1)
print(g1.__dict__) #Atributo
print(g1.__getstate__()) #Método

g2 = Gafanhoto('Mauro', 25)
print(g2)
print(g1.__getstate__())

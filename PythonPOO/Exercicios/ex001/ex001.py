#Declaração de classe
class Gafanhoto:
    def __init__(self): #Método  construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0
        
    #Métodos de identação
    def aniversário(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"
#Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Guilherme'
g1.idade = 18
g1.aniversário()

print(g1.mensagem())
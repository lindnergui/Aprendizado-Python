from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True

    def tampar(self):
        self.tampada = True
    def destampar(self):
        self.tampada = False

    def escrever(self, frase):
        if self.tampada:
            print('A caneta está tampada')
        else:
            print(f'[{self.cor}] {frase}[/{self.cor}]')

c1 = Caneta('red')


c1.destampar()
c1.escrever('olá')



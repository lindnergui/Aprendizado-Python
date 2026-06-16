from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome: str, preço: float):
        self.nome: str = nome
        self.preço: float = preço
    
    def etiqueta(self):
        return Panel(f'{self.nome}------R${self.preço}', title='Produto')

p1 = Produto('Geladeira', 1500,)
p2 = Produto('Iphone', 5000)

print(p1.etiqueta())
print(p2.etiqueta())
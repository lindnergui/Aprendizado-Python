from rich import print
from rich.panel import Panel

class churrasco:
#Cada pessoa come 400g
#Preço de R$82,90
    def __init__(self, pessoas):
        self.pessoas = pessoas

    def conta(self):
        carne = self.pessoas * 0.4
        custo = 82.9 * carne
        preço = custo / self.pessoas
        return Panel(f'''
                                Existem [blue]{self.pessoas} pessoas[/] nesse churrasco.
                                A quantidade de carne a ser comprada é de [red]{carne:.2f}KG[/].
                                O custo total é de [green]R${custo:.2f}[/].
                                O preço que cada um terá que pagar é de [green]R${preço:.2f}[/]''', title='churrasco')
c1 = churrasco(10)
print(c1.conta())



from rich import print

class Livro:
    def __init__(self, livro: str, paginas: int, avancar_paginas: int):
        self.livro = livro
        self.paginas = paginas
        self.avancar_paginas = avancar_paginas
        self.soma = 0

    def passagem_paginas(self):
        print(f'Você está lendo o livro [green]{self.livro}[/]')
        proxima_pagina = self.soma + self.avancar_paginas
        if proxima_pagina <= self.paginas:
            self.soma += self.avancar_paginas
            return '[red]-->[/]' * self.avancar_paginas
        elif self.soma < self.paginas:
            paginas_restantes = self.paginas - self.soma
            self.soma = self.paginas
            return '[red]-->[/]' * paginas_restantes + '[yellow](Você chegou ao fim!!)[/]'
        else:
            return 'O livro [green]já foi encerrado[/]'

l1 = Livro('Memórias Póstumas de Brás Cubas', 50, 4)
print(l1.passagem_paginas())
print(l1.passagem_paginas())
print(l1.passagem_paginas())
print(l1.passagem_paginas())
print(l1.passagem_paginas())

 
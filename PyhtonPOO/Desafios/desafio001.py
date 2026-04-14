from rich import print
class Funcionario:

    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome: str = nome
        self.setor: str = setor
        self.cargo: str = cargo

    def __str__(self) -> str:
        return f'Olá, sou o funcionário {self.nome} e trabalho no setor de {self.setor}, no cargo de {self.cargo}' 
c1 = Funcionario('Guilherme', 'Administração', 'Gerente')
print(c1)

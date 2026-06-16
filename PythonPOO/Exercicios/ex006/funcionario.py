from pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = ''
        self.setor = ''
    def bater_ponto(self):
        print(f'{self.nome} acabou de bater ponto')
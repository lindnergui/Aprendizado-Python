from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome, salario = 0, sal_bruto = 0, sal_min = 1612, inss = 7.5):
        self.nome = nome
        self.salario = salario
        self.sal_bruto = sal_bruto
        self.inss = inss
        self.sal_min = sal_min
    
    @abstractmethod
    def calc_sal(self):
        pass
    def analisar_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, valor_hora, nome, horas_trab, sal_min = 1612):
        super().__init__(nome = nome, sal_min = sal_min )
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab
        return self.salario
    
    def analisar_sal(self):
        return self.salario / self.sal_min
    
class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto,  sal_min = 1612, inss = 7.5):
        super().__init__(nome = nome, sal_bruto = sal_bruto, sal_min = sal_min, inss = inss)
        
    def calc_sal(self):
        desconto = (self.sal_bruto * self.inss) / 100
        self.salario = self.sal_bruto - desconto
        return self.salario
        
    def analisar_sal(self):
        return self.salario / self.sal_min
    
f1 = Horista(10, 'Guilherme', 45)
salario_horista = f1.calc_sal()
salarios_minH = f1.analisar_sal()
texto = Panel(f'O(a) funcionário(a) [bold blue]{f1.nome}[/] ganha [bold green]R${salario_horista}[/] reais por hora. O equivalente a [yellow]{salarios_minH:.2f} salários mínimos[/].')
print(texto)

f2 = Mensalista('Andreia', 10000)
salario_mensalista = f2.calc_sal()
salarios_minM = f2.analisar_sal()
texto = Panel(f'O(a) funcionário(a) [bold blue]{f2.nome}[/] ganha [bold green]R${salario_mensalista}[/] reais por mês. O equivalente a [yellow]{salarios_minM:.2f} salários mínimos[/].')
print(texto)

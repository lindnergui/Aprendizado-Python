from Módulos.Moeda import Dobro
from Módulos.Moeda import Metade
from Módulos.Moeda import Menor

num = int(input('Digite um número: '))
print(f'O dobro do valor é de {Dobro.dobro(num)}')
print(f'A metade do valor é de {Metade.metade(num)}')
print(f'45% do valor é equivalente a {Menor.menor(num)}')


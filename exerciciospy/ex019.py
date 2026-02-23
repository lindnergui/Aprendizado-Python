
from random import choice
alu1 = str(input('Primeiro aluno'))
alu2 = str(input('Segundo aluno'))
alu3 = str(input('Terceiro aluno'))
lista = [alu1, alu2, alu3]
escolhido = choice(lista)
print('O aluno escolhido é {}'.format(escolhido))

from random import shuffle 
alu1 = str(input('Digite o primeiro aluno'))
alu2 = str(input('Digite o segundo aluno'))
alu3 = str(input('Digite o terceiro aluno'))
alu4 = str(input('Digite o quarto aluno'))
lista = [alu1, alu2, alu3, alu4]
num = shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
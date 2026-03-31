import random
numero = random.randint(0, 5)
escolhido = int(input('Escolha um número de 0 a 5: '))
if numero == escolhido:
    print('Você acertou!!!')
else:
    print('Infelizmente você errou')
print(f'O número escolhido por mim era {numero}')
from random import randint
numero = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os número gerados foram: {numero}')
print(f'O maior valor sorteado foi: {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')
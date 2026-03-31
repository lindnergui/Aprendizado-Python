from random import randint
from time import sleep
resp = int(input('Quantos jogos deseja fazer: '))
jogos = []
lista = []
total = 1
while total <= resp:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-'*40)
print(f'Sorteando {resp} jogos')
print('-'*40)
for i, c in enumerate(jogos):
    print(f'Jogo {i+1}: {c}')
    sleep(1)
print('-'*30, '< BOA SORTE >', '-'*30)
from random import randint
from time import sleep
from operator import itemgetter
dados = {}
cont = 0
jogador = 1
while cont <= 3:
    valor = randint(1 ,6)
    print(f'Jogador{jogador} tirou {valor}..')
    dados[f'jogador{jogador}'] = valor
    cont += 1
    jogador += 1
    sleep(1)
print('='*20)
print('RANKING DOS JOGADORES')
print('='*20)
ranking = sorted(dados.items(),key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}..')
    sleep(1)
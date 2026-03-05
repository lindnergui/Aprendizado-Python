from random import randint
consecutivas = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    while jogador < 0:
        jogador = int(input('Por favor, um número positivo: '))
    parouimpar = str(input('Escolha Par |P| ou ímpar |I|: ')).strip().upper()
    while parouimpar not in 'PI':
        parouimpar = str(input('Escolha Par |P| ou ímpar |P|: ')).strip().upper()
    print(f'Eu escolhi {computador}, você {jogador}, o resultado é {total}')
    if total % 2 == 0 and parouimpar == 'P':
        print('Você ganhou!!')
        consecutivas += 1
    elif total % 2 == 1 and parouimpar == 'P':
        print('Eu ganhei!!!')
        break
    elif total % 2 == 0 and parouimpar == 'I':
        print('Eu ganhei!!!')
        break
    elif total % 2 == 1 and parouimpar == 'I':
        print('Você ganhou!!!')
        consecutivas += 1
print(f'Você ganhou {consecutivas} consecutivas.')
    
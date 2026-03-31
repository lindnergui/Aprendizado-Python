from random import choice
lista = ['pedra', 'papel', 'tesoura']
jogada = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).strip().lower()
escolha = choice(lista)
if jogada == 'papel' and escolha == 'tesoura':
    print(f'Eu escolhi {escolha} e você {jogada}, eu ganhei!! :)')
elif jogada == 'tesoura' and escolha == 'papel':
    print(f'Eu escolhi {escolha} e você {jogada}, você ganhou!! :(')
elif jogada == 'pedra' and escolha == 'papel':
    print(f'Você escolheu {jogada}, e eu escolhi {escolha}, eu ganhei!! :)')
elif jogada == 'papel' and  escolha == 'pedra':
    print(f'Eu escolhi {escolha} e você escolheu {jogada}, você ganhou!! :(')
elif jogada == 'tesoura' and escolha == 'pedra':
    print(f'Eu escolhi {escolha} e você escolheu {jogada}, eu ganhei!! :)')
elif jogada == 'pedra' and escolha == 'tesoura':
    print(f'Você escolheu {jogada}, e eu escolhi {escolha}, você ganhou!! :(')
print('Vamos denovo?')
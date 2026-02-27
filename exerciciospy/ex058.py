from random import randint
c = 0
numero = randint(1, 5)
escolha = int(input('Digite um numero de 0 a 5: '))
if numero == escolha:
    print('')
else:
    while numero != escolha:
        print(f'Eu escolhi {numero} e você escolheu {escolha}')
        c += 1
        escolha = int(input('Escolha outro número: '))
print(f'foram necessárias {c} tentativas, parabéns!!!!')
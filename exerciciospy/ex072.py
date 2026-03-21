

num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove','Vinte')
while True:
    escolha = int(input('Escolha um número de 0 a 20: '))
    if escolha >= 0 and escolha <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num_extenso[escolha]}')
from random import randint
numeros = []
numerosQ = []
def sorteia():
    for _ in range (5):
        numeros.append(randint(1, 999))
    print(f'Os números sorteados foram: {numeros}')
def somaPar():
    soma = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
            numerosQ.append(numeros[i])
        else:
            print(f'{numeros[i]} é um valor ímpar')
    print(f'A soma dos números pares é {soma}, {numerosQ}')
sorteia()
somaPar()
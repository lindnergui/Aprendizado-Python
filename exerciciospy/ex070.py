soma = 0
maisdemil = 0
menor = 100000000
nome = ''
while True:
    produto = int(input('Digite o valor de um produto: '))
    while produto < 0:
        produto = int(input('Digite o valor de um produto: '))
    nome = input('Digite o nome do produto: ')
    soma += produto
    if produto > 1000:
        maisdemil += 1
    if produto < menor:
        menor = produto
        barato = nome
    cont = str(input('Gostaria de inscrever mais preços? |S|/|N|: ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Gostaria de inscrever mais preços? |S|/|N|: ')).strip().upper()
    if cont == 'N':
        break
print(f'A soma total vale {soma}')
print(f'{maisdemil} produtos custam mais de mil reais')
print(f'O produto mais barato custa R${menor} e se chama {barato}')
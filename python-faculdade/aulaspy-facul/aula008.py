import sys
preco = float(input('Qual o preço desse produto? '))
lucro70 = preco + (preco * 70) / 100
lucro50 = preco + (preco * 50) / 100
lucro40 = preco + (preco * 40) / 100
lucro30 = preco + (preco * 30) / 100
if preco < 0:
    print('Valor inválido')
    sys.exit()
if preco < 10:
    print(f'O preço tem um lucro de 70% (R${lucro70:.2f})')
elif preco >= 10 and preco < 30:
    print(f'O preço tem lucro de 50% (R${lucro50:.2f})')
elif preco >= 30 and preco < 50:
    print(f'O preço tem lucro de 40% (R${lucro40:.2f})')
else:
    print(f'O preço tem lucro de 30% (R{lucro30:.2f})')
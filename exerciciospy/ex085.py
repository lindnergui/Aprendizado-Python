valores = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Os pares são: {valores[0]}')
print(f'Os ímpares são: {valores[1]}')

valores = [[], [], [], []]
valor = 0
somapares = 0
somaterceiro = 0
maior = 0
for x in range(0, 3):
    valor = int(input(f'Digite um valor para a posição (0 x {x})'))
    valores[1].append(valor)
    if valor % 2 == 0:
        valores[0].append(valor)
        somapares += valor
    if x == 2:
        somaterceiro += valor
for y in range(0 ,3):
    valor = int(input(f'Digite um valor para a posição (1 x {y})'))
    valores[2].append(valor)
    if valor % 2 == 0:
        valores[0].append(valor)
        somapares += valor
    if y == 2:
        somaterceiro += valor
    if y == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
for z in range(0, 3):
    valor = int(input(f'Digite um valor para a posição (2 x {z})'))
    valores[3].append(valor)
    if valor % 2 == 0:
        valores[0].append(valor)
        somapares += valor
    if z == 2:
        somaterceiro += valor
print('-' * 40)
print(f'          |{valores[1][0]}| |{valores[1][1]}| |{valores[1][2]}|')
print(f'          |{valores[2][0]}| |{valores[2][1]}| |{valores[2][2]}|')
print(f'          |{valores[3][0]}| |{valores[3][1]}| |{valores[3][2]}|')
print('-'*40)  
print(f'A soma de todos os pares é de: {somapares}')
print(f'A soma de todos na terceria coluna é de: {somaterceiro}')
print(f'O maior valor da segunda linha é de: {maior}')
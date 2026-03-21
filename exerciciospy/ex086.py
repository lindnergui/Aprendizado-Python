valores = [[], [], []]
for x in range(0, 3):
    valores[0].append(int(input(f'Digite o valor da posição (0, {x})')))
for y in range(0, 3):
    valores[1].append(int(input(f'Digite um valor na posição (1, {y})')))
for z in range(0, 3):
    valores[2].append(int(input(f'Digite um valor na posição (2, {z})')))
print(f'|{valores[0][0]}| |{valores[0][1]}| |{valores[0][2]}|')
print(f'|{valores[1][0]}| |{valores[1][1]}| |{valores[1][2]}|')
print(f'|{valores[2][0]}| |{valores[2][1]}| |{valores[2][2]}|')
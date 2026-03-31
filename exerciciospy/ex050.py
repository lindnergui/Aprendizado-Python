soma = 0
for c in range(0, 7, 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os pares é {soma}.')
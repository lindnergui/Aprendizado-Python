num = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    resp = str(input('Deseja continuar? S/N: ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Inválido, digite considerando S/N: ')).upper().strip()
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if resp == 'N':
        break
print(f'Lista original: {num}')
print(f'Lista com numeros pares: {pares}')
print(f'Lista com números ímpares: {impares}')

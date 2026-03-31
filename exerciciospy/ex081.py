valores = []
soma5 = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Deseja adicionar outro valor? S/N: ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Inválido, digite considerando S (sim) ou N (não): ')).upper().strip()
    if n == 5:
        soma5 += 1
    if resp == 'N':
        break
quantidade = len(valores) + 1
print(f'A quantidade de números é {len(valores)}')
print(f'Os números em ordem decrescente são: {sorted(valores, reverse=True)}')
print(f'O valor 5 aparece {soma5} vezes na lista')

num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não adicionando..')
    resp = str(input('Quer continuar? S/N: ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Inválido, considere como resposta S (sim) ou N (não)')).upper().strip()
    if resp == 'N':
        break
num.sort()
print(f'Os valores em ordem crescente são: {num}')
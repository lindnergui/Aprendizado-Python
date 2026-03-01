a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 0
termoatual = a1
print('Os 10 primeiros termos são: ')
while c <= 10:
    print(f'{termoatual}', end=' | ')
    termoatual += razao
    c += 1
cont = 1
c2 = 0
while cont != 0:
    c2 = 1
    cont = int(input('Deseja adicionar mais alguns termos? | 0 | para parar e outro numero para continuar: '))
    while c2 <= cont:
        print(f'{termoatual}', end=' | ')
        termoatual += razao
        c2 += 1
print('FIM')
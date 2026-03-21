a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 0
termoatual = a1
print('Os 10 primeiros termos são: ')
while c <= 10:
    print(f'{termoatual}', end=' | ')
    termoatual += razao
    c += 1
print('FIM')
expressao = str(input('Digite a expressão: '))
cont = 0
for  caractere in expressao:
    if caractere == '(':
        cont += 1
    elif caractere == ')':
        cont -= 1
    if cont < 0:
        print('ERRO')
        break
if cont == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
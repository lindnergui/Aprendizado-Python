import sys
valor = int(input('Digite 1 para domingo até 7 para sábado: '))
if valor < 1 or valor > 7:
    print('número inválido')
    sys.exit()
elif valor == 1:
    print('Domingo')
elif valor == 2:
    print('Segunda-Feira')
elif valor == 3:
    print('Terça-feria')
elif valor == 4:
    print('Quarta-Feira')
elif valor == 5:
    print('Quinta-Feira')
elif valor == 6:
    print('Sexta-Feira')
elif valor == 7:
    print('Sábado')
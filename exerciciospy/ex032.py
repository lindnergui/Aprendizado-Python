ano = int(input('Qual o ano em que estamos analisando aqui?'))
teste = int(0)
if ano % 4 == 0:
    teste = teste + 1
else:
    teste = teste + 0
if ano % 100 != 0:
    teste = teste + 1
else:
    teste = teste + 0
if ano % 400 == 0:
    teste = teste + 1
else:
    teste = teste + 0
if teste >= 2:
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')
    
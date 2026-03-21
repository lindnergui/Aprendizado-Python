ano = int(input('Digite um ano que deseja saber se é bissexto: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')
 
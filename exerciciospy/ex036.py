valor = float(input('Digite o valor da casa '))
salario = float(input('Digite o valor total de seu salário mensal '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
tempo = anos * 12
prestacao = valor / tempo
if prestacao > (salario * 30) / 100:
    print('Infelizmente seu empréstimo é inviável pois excede 30% de seu salário.')
else:
    print(f'A prestação mensal total deverá ser de R${prestacao:.2f} ao longo de {tempo} meses ({anos} anos)')
dias = int(input('Digite a quantidade de dias rodados'))
km = float(input('Digite a quantidade de KM rodados'))
valor = (dias*60) + (0.15*km)
print('O valor total a ser pago é de R${:.2f}'.format(valor))
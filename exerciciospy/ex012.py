valor = float(input('Digite quanto custa seu produto em R$'))
desconto = (valor*5)/100
print('Seu valor de {} com 5% de desconto é R${:.2f}'.format(valor, valor-desconto))
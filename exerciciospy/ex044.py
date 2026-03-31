from random import randint
valor = randint(1, 200)
pagamento = str(input('Digite sua forma de pagamento: ')).lower().strip().replace(' ', '').replace('à', 'a').replace('á', 'a')
avista = valor - ((valor * 10) / 100)
avistac = valor - ((valor * 5) / 100)
cartao2 = valor
cartao3 = valor + ((valor * 20) / 100)
if pagamento == 'cheque' or pagamento == 'avista':
    print(f'Seu valor com 10% de desconto é de R${avista}')
elif pagamento == 'cartao' or pagamento == 'cartão':
    print(f'Seu valor com 20% de desconto é de R${avistac}')
elif pagamento == '2xnocartao' or pagamento == '2xnocartão':
    print(f'Seu valor é de R${cartao2}')
elif pagamento == '3xoumais':
    print(f'Seu valor com 20% de juros é de R${cartao3}')
print(f'O valor original era de R${valor}')
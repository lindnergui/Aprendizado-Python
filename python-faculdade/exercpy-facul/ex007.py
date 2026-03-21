import sys
saldo = float(input('Digite seu saldo bancário: '))
semlimite = saldo
limite500 = saldo * 0.08
limite1000 = saldo * 0.15
if saldo < 0:
    print('Erro, saldo negativado')
    sys.exit()
elif saldo < 500:
    print(f'Seu limite é de R${semlimite}')
elif saldo > 500 and saldo < 1000:
    print(f'Seu limite é de R${limite500:.2f}')
else:
    print(f'Seu limite é de R$ {limite1000:.2f}')
    
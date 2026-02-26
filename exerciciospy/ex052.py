n = int(input('Numero que quer saber se é  primo'))
teste = 0
for c in range(1, n+1):
    if n % c  == 0:
        teste += 1
if teste == 2:
    print('Este número é primo')
else:
    print('Este número não é primo')
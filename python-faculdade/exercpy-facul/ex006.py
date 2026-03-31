from math import sqrt
import sys
a = int(input('Digite um valor para o A: '))
b = int(input('Digite um valor para o B: '))
c = int(input('Diigte um valor para o C: '))
if a == 0:
    print('valor de A inválido, considere diferente de zero')
    sys.exit()
delta = b**2 - 4 * a * c
if delta <= 0:
    print(f'Valor de delta inválido ({delta})')
    sys.exit()
else: 
    print(f'Delta é {delta}, a equação possui duas raízes reais.')
x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)
print(f'As raízes de sua equação são: {x1:.2f} e {x2:.2f}')    
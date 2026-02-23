from math import sqrt, floor
cato = float(input('Digite o valor do cateto oposto'))
cata = float(input('Digite o valor do cateto adjacente'))
hip = (cato**2) + (cata**2)
res = sqrt(hip)
print('O valor da hipotenusa de {} com {} é igual a {}'.format(cato, cata, floor(res)))
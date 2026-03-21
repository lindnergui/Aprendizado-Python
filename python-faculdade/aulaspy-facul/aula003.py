#Volume de uma esfera

from math import sqrt, fabs

#raio = float(input("Digite o valor do raio"))
#volume = (4 * pi * raio**3) / 3
#print(f"O valor do seu volume é de {volume:.2f}")

a = 4
b = 5

print((sqrt((a + 3 * b)/(b + 1)) + b**5) + sqrt(sqrt(a) + 1)/(b + 3 * a + b * (a**5)) - 1)

print((6 * a * b**a + 1) - (a + 3 * b)/(a+b-1)/fabs(2*b-a**3-1))

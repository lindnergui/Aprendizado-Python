from math import fabs
valor1 = int(input('Digite um valor'))
valor2 = int(input('Digite um segundo valor'))
soma = valor1 + valor2
dif = valor1 - valor2
media = (valor1 + valor2) / 2
dist = fabs(valor1 - valor2)
maior = (valor1 + valor2 + fabs(valor1 - valor2)) / 2
menor =  (valor1 + valor2 - fabs(valor1-valor2)) / 2
print(f'A soma entre os dois é {soma}')
print(f'A diferença entre os dois é {dif}')
print(f'A média entre os dois é {media}')
print(f'A distância entre os dois é {dist}')
print(f'O maior valor é {maior}')
print(f'O menor entre os dois é {menor}')

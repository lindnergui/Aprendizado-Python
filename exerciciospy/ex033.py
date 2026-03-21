num1 = float(input('Digite seu primeiro número '))
num2 = float(input('Digite seu segundo número '))
num3 = float(input('Digite seu terceiro número '))
maior = num1
menor = num3
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num1 < menor:
    menor = num1
if num2 < menor:
    menor = num2
print(f'Seu maior número é o {maior}')
print(f'Seu menor número é o {menor}')
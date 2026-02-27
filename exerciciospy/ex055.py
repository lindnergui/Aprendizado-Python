maior = 0
menor = 1000000
for c in range(0, 6):
    peso = float(input('Digite seu peso atual em KG: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é de {maior}KG e o menor peso é de {menor}KG')
from datetime import date
menor18 = 0
maior18 = 0
for c in range(0, 8):
    nasc = int(input('Digite seu nascimento'))
    idade = date.today().year - nasc
    if idade < 18:
        menor18 += 1
    else:
        maior18 += 1
print(f'Do total, {maior18} atingiram a maoridade, e {menor18} não atingiram')
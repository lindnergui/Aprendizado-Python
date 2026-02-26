a1 = int(input('Digite o primeiro termo dessa PA: '))
razao = int(input('Qual a razão dela?: '))
soma = 0
print('Primeiros 10 termos são: ')
for c in range(1, 11):
    soma = razao * c
    print(soma)
print('FIM')
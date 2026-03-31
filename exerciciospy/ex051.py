a1 = int(input('Digite o primeiro termo dessa PA: '))
razao = int(input('Qual a razão dela?: '))
print('Primeiros 10 termos são: ')
for c in range(a1, a1 + 10 * razao, razao):
    print(c)
print('FIM')
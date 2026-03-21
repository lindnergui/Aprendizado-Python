soma = 0
maior = 0
nomedovelho = ''
mulheresnovas = 0
for c in range(0, 4):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade atual em anos: '))
    sexo = int(input('''
        Digite seu sexo: |1| MASCULINO  |2| FEMININO      '''))
    soma += idade
    if idade > maior and sexo == 1:
        maior = idade
        nomedovelho = nome
    if sexo == 2 and idade < 20:
        mulheresnovas += 1
media = soma / 4
print(f'A média de idade é de {media}')
print(f'O homem mais velho se chama {nomedovelho} e tem {maior} anos')
print(f'No total, {mulheresnovas} mulheres tem menos de 20 anos.')
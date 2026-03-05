menos18 = 0
homens = 0
mulheres20 = 0
while True:
    idade = int(input('Digite a idade de uma pessoa: '))
    sexo = str(input('Digite o sexo de uma pessoa, |M| - masculino ou |F| - feminino: ')).strip().upper()
    while idade < 0 or idade > 150:
       idade = int(input(f'Sua idade é inválida ({idade}), redigite: '))
    while sexo not in ['F', 'M']:
       sexo = str(input(f'Seu sexo inserido é inválido ({sexo}), redigite considerando |M| ou |F|: ')).strip().upper()
    if sexo == 'M':
       homens += 1
    if idade > 18:
       menos18 += 1
    if idade < 20 and sexo == 'F':
       mulheres20 += 1 
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'O total de pessoas com mais de 18 é de {menos18}, a quantidade de homens é de {homens}, e a quantidade de mulheres com menos de 20 anos é de {mulheres20}.')
       

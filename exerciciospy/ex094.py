pessoas = {}
lista = []
maiores_media = []
cont = 's'
soma = 0
soma_media = 0
mulheres = 0
soma_maiores = 0
while True:
    soma += 1
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o nome da pessoa: '))
    pessoas['Idade'] = int(input('Digite a idade da pessoa: '))
    pessoas['Sexo'] = str(input('Digite o sexo da pessoa: |M| ou |F|: ')).strip().upper()
    soma_media += pessoas['Idade']
    if pessoas['Sexo'] == 'F':
        mulheres += 1
    media = soma_media / soma
    if pessoas['Idade'] > media:
        maiores_media.append(pessoas['Nome'])
        soma_maiores += 1
    lista.append(pessoas.copy())
    print('-'*30)
    cont = str(input('Deseja adicionar mais? |S| ou |N|: ')).upper().strip()
    if cont == 'N':
        break
if soma == 1:
   print('No total, 1 pessoa foi cadatrada..')
else:
   print(f'No total, {soma} pessoas foram cadastradas..') 
print(f'A média das idades é de {media:.2f}..')
if mulheres == 1:
    print('1 mulher foi cadastrada..')
else:
    print(f'No total, {mulheres} mulheres foram cadastradas..')
if soma_maiores == 1:
    print(f'Uma pessoa tem a idade maior que a média.., com ela sendo: {maiores_media}')
elif soma_maiores == 0:
    print('Nenhuma pessoa possui idade maior que a média.')
else:
    print(f'No total, {soma_maiores} pessoas tem idade maior que a média, sendo elas: {maiores_media}')
    
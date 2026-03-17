from datetime import date
ficha = {}
dataatual = date.today()
anoatual = dataatual.year
while True:
    ficha['Nome'] = str(input('Digite seu nome: '))
    adn = int(input('Digite seu ano de nascimento: '))
    ficha['Idade'] = anoatual - adn
    ficha['ctps'] = int(input('Digite o número da CTPS (0 caso não tenha): '))
    if ficha['ctps'] == 0:
        break
    else:
        ficha['Contratação'] = int(input('Digite seu ano de contratação: '))
        ficha['Salário'] = float(input('Digite seu salário: '))
        aposentadoria = anoatual - ficha['Contratação']
        if aposentadoria > 35:
            ficha['Aposentadoria'] = print('Vocẽ já tem a constribuição necessária para aposentadoria')
            aposentar = 35 - aposentadoria
            ficha['Aposentadoria'] = ficha['Idade'] + aposentar
        else:
            print(f'Você tem {aposentadoria} anos de constribuição. ')
            aposentar = 35 - aposentadoria
            ficha['Aposentadoria'] = ficha['Idade'] + aposentar
        for k, v in ficha.items():
            print(f'{k} tem valor {v}')
for k, v in ficha.items():
    print(f'{k} tem valor {v}')
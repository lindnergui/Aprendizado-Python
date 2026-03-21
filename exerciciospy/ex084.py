pessoas = []
principal = []
mai = men = 0
while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(float(input('Digitre seu Peso: ')))
    if len(principal) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    principal.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? |S| / |N|: :')).upper().strip()
    if resp == 'N':
        break
print(f'Você registrou {len(principal)}')
print(f'O maior peso foi de: {mai}KG, e ficou com: ', end='')
for p in principal:
    if p[1] == mai:
        print(f'{p[0]}. ', end='')
print(f'O menor peso foi de: {men}, e ficou com: ', end='')
for p in principal:
    if p[1] == men:
        print(f' {p[0]}. ', end='')
altura = float(input('Digite aqui sua altura em metros: '))
genero = int(input('Digite aqui seu gênero, utilize 1 para masculino e 2 para feminino: '))
pesohomem= 72.7 * altura - 58
pesomulher = 62.1 * altura - 44
if genero == 1:
    print(f'Seu peso ideal masculino é de {pesohomem:.2f}KG')
elif genero == 2:
    print(f'Seu peso ideal feminino é de {pesomulher:.2f}KG')
else:
    print('Gênero inválido, peso não calculado')
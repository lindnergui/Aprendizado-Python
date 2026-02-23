dist = int(input('Digite a distância de sua viagem até aqui em KM '))
if dist <= 200:
    print(f'O valor total a se pagar é R${dist*0.5}')
else:
    print(f'o valor total é R${dist*0.45}')
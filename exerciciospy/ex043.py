altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso atual em KG: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 > imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
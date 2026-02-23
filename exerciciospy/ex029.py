import random
vel = random.randint(20, 200)
if vel > 80:
    print(f'O carro está {(vel-80)}KM acima da média!!({vel}KM), o valor da multa é de R${(vel-80)*7}')
else:
    print(f'Velocidade de {vel}KM, prossiga')
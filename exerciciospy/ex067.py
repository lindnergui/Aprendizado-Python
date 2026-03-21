num = 0
c = 0
while True:
    num = int(input('Quer ver a tabuada de qual número? |negativo| para parar: '))
    if num < 0:
        break
    while c <= 10:
        print(f'{num} x {c} = {num * c}')
        c += 1
print('Encerrando..')
valor = int(input('Digite o valor em segundos: '))
horas = valor // 3600
minuto = valor % 3600
minutos = minuto // 60
segundo = minutos % 60
print(f'{valor} segundos tem {horas:} horas, {minutos} minutos e {segundo} segundos.')

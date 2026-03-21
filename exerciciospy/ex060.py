num = int(input('Digite um número que deseja saber o fatorial: '))
c = num
fat = 1
while c > 1:
    fat = fat * c
    c -= 1
print(f'O fatorial de {num} é {fat}')

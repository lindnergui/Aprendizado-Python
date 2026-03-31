nota1 = float(input('Digite o valor da primeira nota'))
nota2 = float(input('Digite o valor da segunda nota'))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média está ruim!! Estude mais')
elif media > 5 < 6:
    print('Você está em um nível mediano!! Busque melhorar')
else:
    print('Você está com uma média muito boa!! Parabéns')
print(f'Sua média é de {media:.2f}')
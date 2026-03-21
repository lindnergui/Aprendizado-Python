valores = (
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: '))
)
print(f'O valor 9 apareceu: {valores.count(9)}')
if 9 in valores:
    posicao = valores.index(3) + 1
    print(f'O valor 3 está na posição: {posicao}')
else: 
    print('Valor 3 não disponível')
for n in valores:
    if n % 2 == 0:
        print(n)

    
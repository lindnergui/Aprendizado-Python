frase = str(input('Digite a frase que você quiser: ')).lower().replace(' ', '')
if frase == frase[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')
palavras = ('Aprender', 'Programar', 'Estudar', 'Computador', 'Sol', 'Nuvem',
    'Celular', 'Teclado', 'Mouse', 'Jogo', 'Estante', 'Livro')
for palavra in palavras:
    print(f'A palavra {palavra.upper()} tem como vogais: ')
    for v in palavra:
        if v.lower() in 'aeiou':
            print(v)
    
    
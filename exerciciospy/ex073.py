tabela = ('Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense',
'athletico parananese', 'Bragantino', 'Grêmio', 'Chappecoense', 'Mirassol',
'Coritiba', 'Santos', 'Botafogo', 'Vitória', 'Remo', 'Atletico GO', 'Internacional', 'Cruzeiro', 'Vasco')
while True:
    print('''
    a) 5 primeiras colocações
    b) Os ultimos 4 colocados
    c) Ordem alfabética
    d) Em que posição está o Flamengo''')
    escolha = str(input('Digite sua escolha, 0 para parar: ')).upper().strip()
    if escolha not in 'ABCD0':
        print('Digite opções vaĺidas entre a, b, c ou d: ')
    if escolha == 'A':
        print(f'Os 5 primeiros colocados são: {tabela[0:6]}')
    elif escolha == 'B':
        print(f'Os últimos 4 colocados são: {tabela[16:21]}')
    elif escolha == 'C':
        print(f'A ordem alfabética é: {sorted(tabela)}')
    elif escolha == 'D':
        print(f'O flamengo está na posição número: {tabela.index('Flamengo') + 1}')
    elif escolha == '0':
        break
print('FIM do programa')
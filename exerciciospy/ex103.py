def ficha(jogador='', gols=''):
    jogador = str(input('Digite o nome do jogador: ')).strip()
    gols = str(input('Quantos gols ele marcou?: ')).strip()
    if jogador == '':
        jogador = '<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if gols == 0 or gols == '':
        gols = 'nenhum'

    return f'O jogador {jogador} fez {gols} gols.'
print(ficha())
jogadores = {}
lista = []
total_gols = 0
resp = 's'
while True:
    cont = 0
    jogadores['Nome'] = str(input('Digite o nome do jogador: '))
    jogadores['Partidas'] = int(input('Digite quantas partidas o mesmo jogou: '))
    lista.append(jogadores.copy())
    while cont < jogadores['Partidas']:
        quantidade_gols = int(input(f'Quantos gols ele fez na partida {cont+1}: '))
        cont += 1
        total_gols += quantidade_gols
    resp = str(input('Deseja continuar? |S| |N|: ')).strip().upper()
    if resp == 'N':
        break
gols = {}
gols_partida = []
partidas = 0
cont = 0
soma = 0
gols['Nome'] = str(input('Qual o nome do jogador: '))
total_partidas = int(input('Quantas partidas ele jogou?: '))
partidas = total_partidas
gols['Partida'] = total_partidas
while cont < partidas:
    g_partida = int(input(f'Quantos gols na partida {cont + 1}?: '))
    gols_partida.append(g_partida)
    cont += 1
    soma += g_partida
gols['Gols'] = gols_partida[:]
gols['Total'] = soma
print('-'*30)
print(f'O jogador {gols['Nome']} jogou {gols['Partida']} partidas.')
for i, c in enumerate(gols['Gols']):
    print(f'  ==>> na partida {i+1} fez {c} gols')
print(f'No total foram {gols['Total']} gols')
    
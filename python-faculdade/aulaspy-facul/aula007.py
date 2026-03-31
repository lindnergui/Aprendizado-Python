#horafim = int(input('Em qual hora esse jogo foi encerrado'))
#minfim = int(input('Em qual minuto esse jogo foi encerrado'))
#conini = (horaini * 60) + minini
#confim = (horafim * 60) + minfim
#duracao = confim - conini
#if duracao < 0:
#    duracao += 1440
#duracaohoras = duracao // 60 
#duracaominutos = duracao % 60
#f duracao > 1440:
    #print('Esse jogo ultrapassa 24 horas')
#else:
#    print(f'A duração é de {duracao} min ou {duracaohoras} horas e {duracaominutos} minutos')

valor = input('Digite um número inteiro de 4 dígitos')
if len(valor) != 4:
    print('Erro, seu código não tem 4 dígitos')
else:
    if valor[::-1] == valor: 
        print('Esse número é colidio')
    else:
        print('Esse número não é colidio')
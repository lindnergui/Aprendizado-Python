def interactive_help():
    while True:
        print('-' * len('SISTEMA DE AJUDA PyHELP'))
        print('SISTEMA DE AJUDA PyHELP')
        print('-' * len('SISTEMA DE AJUDA PyHELP'))
        cmd = input('Função ou Biblioteca, digite fim para sair: ').lower().strip()
        if cmd == 'fim':
            print('-' * 30)
            print('ATÉ LOGO!!!')
            break
        else:
            help(cmd)
            print('Digite [q] para sair')
interactive_help()
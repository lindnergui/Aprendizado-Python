def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('\033[31mDigite um valor INTEIRO válido: \033[m')
def LeiaFloat():
    while True:
        try:
            num = float(input('Digite um número real: '))
            return num
        except ValueError:
            print('\033[31mDigite um valor REAL válido: \033[m')


def linha(tam = 42):
    return '-' * tam
    
    
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua opção: ')
    return opc
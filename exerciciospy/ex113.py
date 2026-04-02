def LeiaInt():
    while True:
        try:
            num = int(input('Digite um valor inteiro: '))
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
print(LeiaInt())
print(LeiaFloat())
def leiaInt(n = 0):
    n = input('Digite um número inteiro: ')

    if n.isnumeric():
        return f'Sucesso, você digitou um número inteiro: {n}'
    else:
        return '\033[31mErro, você não digitou um número inteiro.\033[m'

print(leiaInt())
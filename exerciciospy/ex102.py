
def fatorial(n, show=True):
    """
    Calcula o fatorial de um número.

    :param n: O número a ser calculado.
    :param show: Se True, mostra o cálculo passo a passo.
    :return: O valor do fatorial.
    """

    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c}', end='')
            else:
                print(f'{c} x', end=' ')
    return f' = {f}'
print('-' * 30)

print(fatorial(5))

print(fatorial(6, False))


def resumo(num, dobro, menor, metade):
    if num.is_integer():
        num = int(num)

    print('-' * (len('RESUMO DO VALOR') + 4))
    print('  RESUMO DO VALOR')
    print('-' * (len('RESUMO DO VALOR') + 4))
    print(f'Valor analisado:   R${num}')
    print(f'Dobro do valor:    R${dobro}')
    print(f'Metade do valor:   R${metade}')
    print(f'45% do valor:      R${menor}')
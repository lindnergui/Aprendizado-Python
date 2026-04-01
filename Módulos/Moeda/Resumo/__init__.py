def resumo(num, dobro, menor, metade):
    if num.is_integer():
        num = int(num)
    else:
        while True:
            if num.replace('.', '', 1).isdigit():
                num = float(num)
                break
            else:
                num = input('Digite um valor válido: ')
    print('-' * (len('RESUMO DO VALOR') + 4))
    print('  RESUMO DO VALOR')
    print('-' * (len('RESUMO DO VALOR') + 4))
    print(f'Valor analisado:   R${num}')
    print(f'Dobro do valor:   R${dobro}')
    print(f'Metade do valor:   R${metade}')
    print(f'45% do valor:   R${menor}')
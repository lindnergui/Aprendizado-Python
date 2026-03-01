num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um segundo valor: '))
maior = num1
menu = 0
while menu != 5:
    print('''
            |1| SOMAR
            |2| MULTIPLICAR
            |3| MAIOR
            |4| NOVOS NUMEROS
            |5| SAIR DO PROGRAMA|
                        ''')
    menu = int(input('Qual a sua opção'))
    if menu == 1:
        print(f'A soma é {num1 + num2}')
    elif menu == 2:
        print(f'A multiplicação é de {num1 * num2}')
    elif menu == 3:
        if num2 > num1:
            maior = num2
            print(f'O maior é {maior}')
    elif menu == 4:
        num1 = int(input('Redigite seu primeiro numero: '))
        num2 = int(input('Redigite seu segundo número: '))
    elif menu == 5:
        print('Finalizando..')
    else: 
        print('Opção inválida. Tente novamente')
print('=-=' * 10)
print('Fim do programa')
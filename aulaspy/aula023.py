try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except ZeroDivisionError:
    print('Divisão por zero é inviável.')
except ValueError:
    print('Digite apenas números inteiros.')
except Exception as e:
    print(f'Ocorreu um erro: {e.__class__}')
else:
    print(f'O resultado da divisão é: {r:.2f}')
finally:
    print('Volte sempre :)')
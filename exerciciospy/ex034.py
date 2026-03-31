salario = float(input('Digite seu salário'))
aumento15 = (salario*15)/100
aumento10 = (salario*10)/100
if salario > 1250:
    print(f'Seu aumento é de 10%, totalizando {salario + aumento10:.2f}')
else:
    print(f'Seu aumento é de 15%, totalizando {salario + aumento15:.2f}')
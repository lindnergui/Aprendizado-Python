while True:
    cedulas50 = 50
    cedulas20 = 20
    cedulas10 = 10
    cedulas1 = 1
    valor = int(input('Informe o valor inteiro que deseja sacar: '))
    c50 = valor // cedulas50
    resto = valor % 50
    c20 = resto // cedulas20
    resto = resto % 20
    c10 = resto // cedulas10
    resto = resto % 10
    c1 = resto
    break
print(f'''  
    {c50} cédulas de 50
    {c20} cédulas de 20
    {c10} cédulas de 10
    {c1} cédulas de 1
    ''')
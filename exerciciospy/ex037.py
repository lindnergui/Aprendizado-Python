valor = int(input('Digite aqui um número sem vírgulas '))
escolha = input('Digite 1 para binário. Digite 2 para Octal. Digite 3 para hexadecimal ')
if escolha == '1':
    print(bin(valor)[2:])
elif escolha == '2':
    print(oct(valor)[2:])
else:
    print(hex(valor)[2:])
print('Tenha uma boa noite')
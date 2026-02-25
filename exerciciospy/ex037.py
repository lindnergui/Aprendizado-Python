valor = int(input('Digite aqui um número sem vírgulas '))
escolha = input('Digite 1 para binário. Digite 2 para Octal. Digite 3 para hexadecimal ')
if escolha == '1':
    print(bin(valor))
elif escolha == '2':
    print(oct(valor))
else:
    print(hex(valor))
print('Tenha uma boa noite')
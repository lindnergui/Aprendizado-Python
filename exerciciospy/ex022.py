nome = str(input('Digite seu nome'))
maiusculas = (nome.upper())
minusculas = (nome.lower())
espacos = (nome.replace(' ', ''))
letrasse = (len(espacos))
separar = (nome.split())
letras = separar[0]
total = (len(letras))
#------------------------------------------------
print('Seu nome com maiusculas é {}'.format(maiusculas))
print('Seu nome com minúsculas é {}'.format(minusculas))
print('O total de letras sem espaços é {}'.format(letrasse))
print('Seu primeiro nome tem {} letras'.format(total))
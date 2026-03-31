sexo = str(input('Digite seu sexo (M|F)'))
while sexo not in ('MmFf'):
    sexo = str(input('Dado inválido, digite seu sexo novamente (M ou F): '))
print('Gênero obtido com sucesso')
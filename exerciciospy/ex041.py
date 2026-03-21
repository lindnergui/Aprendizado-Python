from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - nascimento
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
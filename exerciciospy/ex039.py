from datetime import date

ano = int(input("Digite o ano de seu nascimento"))
atual = date.today().year
idade = atual - ano
if idade > 18:
    print(f'Voce está fora do prazo, aliste-se já!! Você está {idade - 18} anos atrasado')
elif idade == 18:
    print('É hora de se alistar!!Você já completou 18')
else:
    print(f'Você ainda não chegou na hora de se alistar!! Faltam {18 - idade} anos')

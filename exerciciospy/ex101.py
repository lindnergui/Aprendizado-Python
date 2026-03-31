
from datetime import date


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 16 and idade < 18 or idade > 65:
        return "O voto é FACULTATIVO"
    elif idade >= 18:
        return "O voto é OBRIGATÓRIO"
    else:
        return "O voto é NEGADO"


ano_nascimento = int(input("Qual ano você nasceu? "))
print(voto(ano_nascimento))

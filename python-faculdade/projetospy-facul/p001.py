meses = 0
mes_maior = ""
mes_menor = ""
nome_atual = ""
c = 1
temp = 0
soma = 0
temp33 = 0
maior = -61
menor = 51
# validação de todos os dados:
while c <= 12:
    print(f"Dados {c}:", "-" * 60)
    meses = int(
        input("Digite o mês do ano, considerando 1 - Janeiro / 12 - Dezembro: ")
    )
    while meses <= 0 or meses > 12:
        meses = int(
            input(
                "Dado de mês inválido, digite considerando 1 - Janeiro / 12 - Dezembro: "
            )
        )
    temp = float(input("Digite a temperatura do mês no intervalo de -60 a +50: "))
    while temp < -60 or temp > 50:
        temp = float(
            input(
                "Dado de temperatura inválido, digite considerando o intervalo de -60 e +50: "
            )
        )
    # Identificação do mẽs
    if meses == 1:
        nome_atual = "Janeiro"
    elif meses == 2:
        nome_atual = "Fevereiro"
    elif meses == 3:
        nome_atual = "Março"
    elif meses == 4:
        nome_atual = "Abril"
    elif meses == 5:
        nome_atual = "Maio"
    elif meses == 6:
        nome_atual = "Junho"
    elif meses == 7:
        nome_atual = "Julho"
    elif meses == 8:
        nome_atual = "Agosto"
    elif meses == 9:
        nome_atual = "Setembro"
    elif meses == 10:
        nome_atual = "Outubro"
    elif meses == 11:
        nome_atual = "Novembro"
    else:
        nome_atual = "Dezembro"
    # Dados de media, soma...
    if temp > 33:
        temp33 += 1
    if temp > maior:
        maior = temp
        mes_maior = nome_atual
    if temp < menor:
        menor = temp
        mes_menor = nome_atual
    c += 1
    soma += temp
print(f"A média de todas as temperaturas é de: {soma / 12:.2f}")
print(f"O total de meses com temperatura maior que 33 graus é de {temp33}")
print(f"O mês de maior temperatura é o de {mes_maior} e tem {maior} C°")
print(f"O mês de menor temperatura é o de {mes_menor} e tem {menor} C°")

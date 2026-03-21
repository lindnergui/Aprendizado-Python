num = int(input('Digite um valor: '))
cont = 1
soma = 0
soma += num
c = 1
maior = num
menor = num
while cont == 1:
    cont = int(input('Quer continuar a digitar? |1| - sim / |2| - não: '))
    if cont != 1 and cont != 2 or cont == '':
        while cont != 1 and cont != 2:
            cont = int(input('Valor inválido, redigite considerando: |1| - sim / |2| - não: '))
    elif cont == 2 and c == 1:
        print(f'A média é {num}, o maior é {num} e não existe menor')
    elif cont == 1:
        num = int(input('Digite outro valor: '))
        c += 1
        soma += num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    elif cont == 2:
        media = soma / c
        print(f'A média entre todos é: {media}, o maior valor é {maior}, e o menor é {menor}')
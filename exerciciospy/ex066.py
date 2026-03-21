num = 0
soma = 0
c = 0
while True:
    num = int(input('Digite um valor, |999| para parar: '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'A soma foi de {soma}, e a quantidade foi de {c}')
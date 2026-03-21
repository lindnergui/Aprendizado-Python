num = 0
qt = 0
soma = 0
while num != 999:
    num = int(input('Digite um valor qualquer, digite |999| para parar: '))
    soma += num
    qt += 1
print(f'A quantidade de números digitados foi de: {qt - 1}, e a soma entre eles é de: {soma - 999}.')
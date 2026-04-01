from Módulos.Utilidades.moeda import dobro, metade, menor, resumo
num = input('Digite um valor: ')
num = num.replace(',', '.')
while True:
    if num.replace('.', '', 1).isdigit():
        num = float(num)
        resumo.resumo(num, dobro.dobro(num), menor.menor(num), metade.metade(num))
        break
    else:
        print('Digite apenas números!')
        num = input('Digite um valor: ')
        num = num.replace(',', '.')

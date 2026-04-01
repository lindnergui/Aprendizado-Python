from Módulos.Utilidades.moeda import dobro, menor, metade, resumo

num = float(input('Digite um valor: '))
resumo.resumo(num, dobro.dobro(num, show=False), menor.menor(num, show=False), metade.metade(num, show=False))

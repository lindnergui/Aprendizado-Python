from Módulos.Moeda import Dobro, Menor, Metade, Resumo

num = float(input('Digite um valor: '))
Resumo.resumo(num, Dobro.dobro(num, show=False), Menor.menor(num, show=False), Metade.metade(num, show=False))


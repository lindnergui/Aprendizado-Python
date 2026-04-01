from Módulos.Moeda import Dobro, Menor, Metade

num = float(input("Digite um valor: "))
print(f"O dobro do valor R${num} é de R${Dobro.dobro(num)}")
print(f"A metade do valor R${num} é de R${Metade.metade(num)}")
print(f"45% de R${num} é equivalente a R${Menor.menor(num)}")

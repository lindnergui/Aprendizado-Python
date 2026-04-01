from Módulos.Moeda import Dobro, Menor, Metade

num = float(input("Digite um valor: "))
print(f"O dobro do valor R${num} é de {Dobro.dobro(num, show=True)}")
print(f"A metade do valor R${num} é de {Metade.metade(num, show=True)}")
print(f"45% de R${num} é equivalente a {Menor.menor(num, show=True)}")
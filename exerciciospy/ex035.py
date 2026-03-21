reta1 = int(input("Digite o comprimento de uma reta"))
reta2 = int(input("Digite o comprimento de outra reta"))
reta3 = int(input("Digite o comprimento da terceira reta"))
teste = int(0)
if reta1 + reta2 > reta3:
    teste = teste + 1
if reta1 + reta3 > reta2:
    teste = teste + 1
if reta2 + reta3 > reta1:
    teste = teste + 1
if teste == 3:
    print("Podem formar um triângulo")
else:
    print("Não podem formar um triângulo")

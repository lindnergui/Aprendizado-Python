num = int(input("Quanto numeros deseja saber na sequencia de Fibonnaci?: "))
num1 = 0
num2 = 1
c = 3
print(f"{num1} - {num2}",end=" - ")
while c <= num:
    num3 = num1 + num2
    print(f"{num3}",end=" - ")
    num1 = num2
    num2 = num3
    c += 1
print("FIM")

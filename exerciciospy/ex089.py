ficha = []
while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar? |S| |N|: ")).upper().strip()
    while resp not in "SN":
        resp = str(input("Inválido, considere |S| ou |N|: "))
    if resp == "N":
        break
print("-" * 40)
for i, a in enumerate(ficha):
    print(f"{i} ---- {a[0]} ---- {a[2]:.2f}")
while True:
    print("-" * 40)
    opc = int(input("Ver notas individuais de qual aluno? (999) interrompe: "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")

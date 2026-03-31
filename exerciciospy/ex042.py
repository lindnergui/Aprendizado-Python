reta1 = int(input('Digite o comprimento de uma reta'))
reta2 = int(input('Digite o comprimento da segunda reta'))
reta3 = int(input('Digite o comprimento da terceria reta'))
teste = 0
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas podem formar um triãngulo')
    teste += 1
else:
    print('Não podem formar um triãngulo')
    teste += 0
if teste == 1 and reta1 == reta2 == reta3:
    print('Triângulo equilátero')
elif teste == 1 and reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('Triângulo isósceles')
elif teste == 1:
    print('Triângulo escaleno')
    
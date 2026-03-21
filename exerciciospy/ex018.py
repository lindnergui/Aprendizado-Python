from math import sin, cos, tan, radians
angulo = int(input('Digite seu ângulo inteiro'))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)
print('O seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}'.format(seno, cosseno, tangente))
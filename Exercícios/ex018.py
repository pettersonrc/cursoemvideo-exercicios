from math import sin, cos, tan, radians
a = int(input('Digite o valor do ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(seno, cosseno, tangente))
from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(co**2 + ca**2)
print('O comprimento da hipotenusa desse triângulo retângulo é igual a: {:.2f}'.format(h))
def area(x, y):
    a = x * y
    print(f'A área de um terreno {x:.1f}x{y:.1f} é de {a:.1f}m quadrados')


print(' Controle de terrenos')
print('----------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

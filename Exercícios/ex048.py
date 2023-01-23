s = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += 1
        s += c
print('A soma entre os números ímpares, mútiplos de três, de 1 até 500 é {}!'.format(s))
print('{} números foram solicitados.'.format(n))

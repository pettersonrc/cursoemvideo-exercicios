from time import sleep
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculado {}!...'.format(n))
sleep(1)
print('{}! = '.format(n), end='')
while c > 0:
    if c > 1:
        print('{} x '.format(c), end='')
    else:
        print('{} = '.format(c), end='')
    f *= c
    c -= 1
print(f)

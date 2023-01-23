print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c1 = 0
total = 10
while c1 < 10:
    print(n, end=' -> ')
    n += r
    c1 += 1
print('ACABOU')
c2 = 1
while c2 != 0:
    c2 = int(input('\nVocê gostaria de mostrar mais quantos termos? '))
    c1 = 0
    while c2 > c1:
        print(n, end=' -> ')
        n += r
        c1 += 1
        total += 1
print('Progressão finalizada, {} números foram exibidos'.format(total))

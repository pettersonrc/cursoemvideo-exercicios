print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print(n, end=' -> ')
    n += r
    c += 1
print('ACABOU')

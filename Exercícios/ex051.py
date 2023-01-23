print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(n, end=' -> ')
    n += r
print('ACABOU')

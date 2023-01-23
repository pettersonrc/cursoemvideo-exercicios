n = int(input('Digite um número para ver sua tabuada: '))
print('-='*8)
print('  TABUADA DO {}'.format(n))
print('-='*8)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, c*n))

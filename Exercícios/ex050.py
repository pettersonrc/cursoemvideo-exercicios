s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos {} números PARES digitados é: {}!'.format(cont, s))

n = s = t = 0
while n != 999:
    n = int(input('Digite um número, (999 se quiser parar): '))
    if n != 999:
        t += 1
        s = s + n
print('A soma entre os {} números digitados é {}!'.format(t, s))

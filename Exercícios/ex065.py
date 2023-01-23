continuar = 'S'
s = c = maior = menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = s / c
print('Você digitou {} números, e a média entre eles foi {:.2f}!'.format(c, m))
print('O maior valor foi {} e o menor foi {}!'.format(maior, menor))

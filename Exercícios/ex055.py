maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa (Kg): '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('MAIOR PESO: {:.1f}Kg'.format(maior))
print('MENOR PESO: {:.1f}Kg'.format(menor))

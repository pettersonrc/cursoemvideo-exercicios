d = int(input('Distância da viagem em KM: '))
p = d * 0.50 if d <= 200 else d * 0.45
print('O preço da sua passagem é R${:.2f}!'.format(p))
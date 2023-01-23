km = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o carro foi alugado? '))
r = (d * 60) + (km * 0.15)
print('Com {}km rodados e {} dias alugados, o cliente deverá pagar R${:.2f}!'.format(km, d, r))


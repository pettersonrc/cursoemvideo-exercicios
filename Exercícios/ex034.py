s = float(input('Digite o salário do funcionário? R$'))
if s > 1250:
    sn = s + (s/100)*10
    print('O funcionário que ganhava R${:.2f} agora ganha R${:.2f}!'.format(s, sn))
else:
    sn = s + (s/100)*15
    print('O funcionário que ganhava R${:.2f} agora ganha R${:.2f}!'.format(s, sn))

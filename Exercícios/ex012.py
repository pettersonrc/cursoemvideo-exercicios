P = float(input('Qual o preço do produto? R$'))
NP = P - (P * 5/100)
print('O produto que custava R${:.2f}, agora custa R${:.2f} com 5% de desconto!'.format(P, NP))

S = float(input('Digite o salário atual do funcionário R$'))
NS = S + (S * 15/100)
print('Um funcionário que ganhava {:.2f}, recebeu um aumento de 15%!, seu novo salário equivale a R${:.2f}!'.format(S, NS))
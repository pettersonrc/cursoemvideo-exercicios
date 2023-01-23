casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos a casa será financiada: '))
prestacao = (casa/anos)/12
print('Você deverá pagar R${:.2f} por mês durante {} anos para comprar a casa.'.format(prestacao, anos))
if prestacao > salario/100*30:
    print('O empréstímo foi {}NEGADO{}!'.format('\033[1;31m', '\033[m'))
else:
    print('O empréstimo pode ser {}CONCEDIDO{}!'.format('\033[1;32m', '\033[m'))

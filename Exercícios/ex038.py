n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O {}PRIMEIRO{} valor é maior!'.format('\033[1;34m', '\033[m'))
elif n2 > n1:
    print('O {}SEGUNDO{} valor é maior!'.format('\033[1;35m', '\033[m'))
else:
    print('Não existe valor maior, os dois são {}IGUAIS{}!'.format('\033[1;31m', '\033[m'))

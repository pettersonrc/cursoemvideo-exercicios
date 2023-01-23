n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m < 5.0:
    print('Portanto o aluno está {}REPROVADO{}!'.format('\033[1;31m', '\033[m'))
elif (m >= 5.0) and (m < 7):
    print('Portanto o aluno está em {}RECUPERAÇÃO{}!'.format('\033[1;35m', '\033[m'))
elif m >= 7:
    print('Portanto o aluno está {}APROVADO{}!'.format('\033[1;32m', '\033[m'))

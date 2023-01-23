si = 0  # soma da idade do grupo
mi = 0  # maior idade do homem
contf = 0  # contador de mulheres com menos de 20 anos
nhomem = ''  # nome do homem mais velho
for c in range(1, 5):
    print('-='*10)
    print('     {} PESSOA     '.format(c))
    print('-='*10)
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    si += idade
    if idade > mi:
        mi = idade
    print('''ESCOLHA O SEXO
[0] MULHER
[1] HOMEM
[2] OUTRO''')
    sexo = int(input('OPÇÃO: '))
    if (sexo == 1) and (mi == idade):
        nhomem = nome
    if (sexo == 0) and (idade < 20):
        contf = contf + 1
m = si/4
print('A MÉDIA DE IDADE DO GRUPO É DE {:.0f} ANOS'.format(m))
print('O NOME DO HOMEM MAIS VELHO SE CHAMA {}'.format(nhomem))
print('{} MULHERES TEM MENOS DE 20 ANOS'.format(contf))

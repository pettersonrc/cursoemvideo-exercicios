H = float(input('Qual a altura da parede? '))
L = float(input('Qual a largura da parede? '))
A = L*H
LT = A/2
print('Para uma parede de {}m de altura e {}m de largura, a área é equivalente a {:.2f}m quadrados\nVocê precisará de {:.2f}L de tinta para pintá-la!'.format(H, L, A, LT))

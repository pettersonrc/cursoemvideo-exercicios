from random import choice
from time import sleep
print('-=-'*10)
print('     VAMOS JOGAR JOKENPÔ!')
print('-=-'*10)
print('FAÇA SUA JOGADA \n[1] TESOURA\n[2] PAPEL\n[3] PEDRA')
jogador = int(input('OPÇÃO: '))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')
sleep(0.8)
opcoes = ['TESOURA', 'PAPEL', 'PEDRA']
maquina = choice(opcoes)
print('-=-'*15)
if maquina == 'TESOURA' and jogador == 1:
    print('Eu escolhi {} e você escolheu TESOURA, tivemos um {}EMPATE{}!'.format(maquina, '\033[35m', '\033[m'))
elif maquina == 'TESOURA' and jogador == 2:
    print('Eu escolhi {} e você escolheu PAPEL, você {}PERDEU{}!'.format(maquina, '\033[31m', '\033[m'))
elif maquina == 'TESOURA' and jogador == 3:
    print('Eu escolhi {} e você escolheu PEDRA, você {}VENCEU{}!'.format(maquina, '\033[32m', '\033[m'))
elif maquina == 'PAPEL' and jogador == 1:
    print('Eu escolhi {} e você escolheu TESOURA, você {}VENCEU{}!'.format(maquina, '\033[32m', '\033[m'))
elif maquina == 'PAPEL' and jogador == 2:
    print('Eu escolhi {} e você escolheu PAPEL, tivemos um {}EMPATE{}!'.format(maquina, '\033[35m', '\033[m'))
elif maquina == 'PAPEL' and jogador == 3:
    print('Eu escolhi {} e você escolheu PEDRA, você {}PERDEU{}!'.format(maquina, '\033[31m', '\033[m'))
elif maquina == 'PEDRA' and jogador == 1:
    print('Eu escolhi {} e você escolheu TESOURA, você {}PERDEU{}!'.format(maquina, '\033[31m', '\033[m'))
elif maquina == 'PEDRA' and jogador == 2:
    print('Eu escolhi {} e você escolheu PAPEL, você {}VENCEU{}!'.format(maquina, '\033[32m', '\033[m'))
elif maquina == 'PEDRA' and jogador == 3:
    print('Eu escolhi {} e você escolheu PEDRA, tivemos um {}EMPATE{}!'.format(maquina, '\033[35m', '\033[m'))
print('-=-'*15)

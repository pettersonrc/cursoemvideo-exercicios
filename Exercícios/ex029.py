vel = float(input('Qual a velocidade do seu carro no momento? '))
if vel > 80:
    m = (vel - 80)*7
    print('Você ultrapassou o limite de velocidade que é de 80Km/h e será MULTADO!!, a multa custará R${:.2f}.'.format(m))
else:
    print('Sua velocidade está de acordo com a lei.')
print('Tenha um bom dia! Dirija com segurança!')
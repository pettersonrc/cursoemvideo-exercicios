peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)
if imc < 18.5:
    print('IMC: {:.1f}, Você está ABAIXO do peso ideal, {}CUIDADO{}!'.format(imc, '\033[1;31m', '\033[m'))
elif 18.5 <= imc < 25:
    print('IMC: {:.1f}, Você está no seu peso ideal, PARABÉNS!'.format(imc))
elif 25 <= imc < 30:
    print('IMC: {:.1f}, Você está em SOBREPESO'.format(imc))
elif 30 <= imc < 40:
    print('IMC: {:.1f}, Você está em OBESIDADE'.format(imc))
else:
    print('IMC: {:.1f}, Você está em Obesidade Mórbida, {}CUIDADO{}!'.format(imc, '\033[1;31m', '\033[m'))

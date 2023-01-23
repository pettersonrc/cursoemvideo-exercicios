frase = str(input('Digite uma frase qualquer: ')).upper().replace(' ', '')
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

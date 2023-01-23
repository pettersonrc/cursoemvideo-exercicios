frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra A aparece na sua frase {} vezes'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))
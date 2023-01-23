homem = pessoas = mulher20 = 0
while True:
    sexo = continuar = ' '
    print('-='*10)
    print('CADASTRE UMA PESSOA')
    print('-=' * 10)
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    print('-=' * 10)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Programa finalizado.')
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} com menos de 20 anos.')

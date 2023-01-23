dados = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    soma += pessoa['Idade']
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(dados)
print('-=' * 30)
print(dados)
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in dados:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

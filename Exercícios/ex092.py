from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (datetime.now().year - dados['Ano de contratação']))
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

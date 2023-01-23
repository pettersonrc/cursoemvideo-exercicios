from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = atual-ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    alistamento = 18 - idade
    alistamentofut = alistamento + atual
    print('Faltam {} ano/anos para você poder se alistar no serviço militar.'.format(alistamento))
    print('Seu alistamento será em {}'.format(alistamentofut))
elif idade == 18:
    print('É hora de se alistar no serviço militar.')
else:
    alistamento = idade - 18
    alistamentopas = atual - alistamento
    print('Já faz {} ano/anos que você deveria ter se alistado no serviço militar.'.format(alistamento))
    print('Seu alistamento foi em {}'.format(alistamentopas))

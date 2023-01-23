from ex115b.lib.interface import *
from time import sleep
from ex115b.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # OpçÃo de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)

from exercicio_115.lib.interface import *
from exercicio_115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar Pessoas', 'Encerrar Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Encerrando Sistema!')
        break
    else:
        cabecalho('\033[31mERRO! Opção Inválida\033[m')
    sleep(2)

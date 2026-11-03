from ex115.menu import *
from ex115.dados import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = interface(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('CADASTRANDO UMA PESSOA')
    elif resposta == 3:
        cabeçalho('SAINDO DO PROGRAMA...')
        break
print('Volte sempre!')
